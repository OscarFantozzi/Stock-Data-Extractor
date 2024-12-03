import pandas   as pd
import requests as r
import json
import logging
from sqlalchemy import create_engine
from datetime import datetime


class extractor:

    def __init__(self,name, id_job):

        self.name    = name
        self._id_job = id_job

    def get_data(self, stock_code, start_date, end_date):
        
        if not start_date or not end_date:

            raise ValueError('For polygon start_date and end_date must be provided.')

        api_key = 'EVETjm2IfJw2woLluVNJ55Kynkvzw17F'

        headers = {'Authorization' : f'Bearer {api_key}' }

        ticker = stock_code

        start_date = start_date

        end_date = end_date

        # api endpoint
        url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}'

        response = r.get(url, headers = headers)

        if response.status_code == 200:

            print(f'Connected: status {response.status_code}')

        else:

            print(f'Not connected: status {response.status_code}')

        # getting data
        data = json.loads(response.text)

        
        if data['queryCount'] == 0:

            print('Not Found')

        else:
            print('Data Retrieved')

        columns = [
            'volume',
            'weighted average price',
            'open price',
            'close price',
            'highest price',
            'lowest price',
            'Unix Msec timestamp',
            'number of transactions'
        ]

        df = pd.DataFrame( data['results'] )

        df.columns = columns

        return df
        

    def load_data_sql(self,df,server,database,table_name):
        
        server = server

        database = database

        conn_string= f'mssql+pyodbc://{server}/{ database }?driver=ODBC+Driver+17+for+SQL+Server'

        engine= create_engine( conn_string )

        df['ingestion_date'] = datetime.now() 

        df.to_sql( name = table_name , con = engine , if_exists= 'replace', index = False)

# ==================================================================================================================================================================================#

server = 'DESKTOP-U9M4TSR'

database = 'stock_api'        
        
table_name = 'stock_data'

# instance class
job1 = extractor('Job #1', '001')

# getting data
df = job1.get_data('AAPL', '2024-09-01','2024-11-29')

job1.load_data_sql(df,server,database,table_name)
        
print("Ingestion Succeed")
    
