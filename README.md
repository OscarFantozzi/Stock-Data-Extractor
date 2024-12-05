
# Stock Data Extractor

### 🚀 **About the Project**

This project is a Python application developed to extract, transform, and load (ETL) stock market data directly from an API into a SQL Server database. The main goal is to demonstrate skills in API integration, data handling with Python, and database storage for further analysis.

---

### ⚙️ **Features**

- Connects to a **financial API** to fetch historical stock data.
- Transforms the data into a **pandas DataFrame**.
- Loads the data into a **SQL Server database**.
- Follows best practices to ensure robust and reusable ETL processes.

---

### 🛠️ **Technologies Used**

- **Python**
  - Libraries: `pandas`, `requests`, `json`, `sqlalchemy`
- **Database**
  - SQL Server (using ODBC Driver 17)
- **API**
  - [Polygon.io](https://polygon.io/) for financial data.
- **ETL**
  - Data extraction, transformation, and loading with scalability in mind.

---

### 📄 **Workflow**

1. **Extraction:**
   - Connects to the Polygon.io API to fetch financial data based on a stock ticker (e.g., `AAPL`).
   - Checks available dates to ensure continuity in data capture.

2. **Transformation:**
   - Formats the data into a pandas DataFrame.
   - Adds an ingestion date column for traceability.

3. **Loading:**
   - Transformed data is uploaded to a SQL Server table.

---

### 🧩 **How to Run**

#### Prerequisites
- Python 3.8 or higher
- SQL Server database configured
- Required dependencies installed:

```bash
pip install pandas requests sqlalchemy pyodbc
```

#### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/api_stocks.git
   cd api_stocks
   ```

2. Set up your database:
   - Create a database called `stock_api`.
   - Ensure the `ODBC 17 for SQL Server` driver is installed.

3. Configure the `config.py` file:
   - Add your API key and SQL Server connection string in the file `config.py`. This file should look like this:
     ```python
     API_KEY = "your_api_key_here"
     DATABASE_URL = "mssql+pyodbc://your_server/stock_api?driver=ODBC+Driver+17+for+SQL+Server"
     ```

4. Run the main script:
   ```bash
   python main.py
   ```

---

### 📊 **Project Demonstration**

Example of data loaded into SQL Server:

| datetime       | volume | weighted average price | open price | close price | highest price | lowest price | number of transactions | ingestion_date        |
|----------------|--------|-------------------------|------------|-------------|---------------|--------------|-------------------------|-----------------------|
| 2024-11-01     | 10000  | 150.25                 | 148.50     | 152.00      | 155.00        | 147.50       | 500                   | 2024-12-05 10:00:00  |

---

### 📝 **What You Can Learn from This Project**

- **Connecting and consuming RESTful APIs:** Extracting data with authentication headers.
- **Data manipulation with pandas:** Cleaning and formatting data for analysis.
- **Database integration:** Using SQLAlchemy to connect and load data into SQL Server.
- **Automating ETL processes:** Creating scalable and reusable workflows.

---

### 🔧 **Potential Improvements**

- Add support for fetching data for multiple stocks simultaneously.
- Create a **Power BI dashboard** to visualize the data.
- Configure **Incremental Refresh** to optimize performance for large data volumes.

---

### 📬 **Contact**

Feel free to reach out if you have any questions or suggestions:

- **GitHub:** [OscarFantozzi](https://github.com/OscarFantozzi)
- **LinkedIn:** [Oscar Fantozzi](https://linkedin.com/in/oscarfantozzi)
