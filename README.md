# Banking Data Engineering and Analytics Project

## Project Overview

This project is an end-to-end banking data analysis workflow that combines Python, PostgreSQL, SQL, and Power BI.

The project uses multiple banking datasets covering customers, branches, accounts, transactions, and loans. Python is used to load and prepare the data, PostgreSQL is used as the database layer, and Power BI is used to create an interactive dashboard for business analysis.

The project demonstrates a practical data workflow from raw CSV files to a database and finally to a business intelligence dashboard.

## Project Objectives

- Load multiple banking datasets into PostgreSQL using Python.
- Prepare and transform data before database loading.
- Organize banking data into separate business entities.
- Analyze accounts, customers, branches, loans, and transactions.
- Build a Power BI dashboard for business reporting.
- Demonstrate an end-to-end data engineering and analytics workflow.

## Technology Stack

- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- SQL
- Power BI
- Git
- GitHub
- CSV

## Project Architecture

```text
CSV Data Sources
      |
      v
Python + Pandas
      |
      | Data loading and basic transformation
      v
SQLAlchemy
      |
      v
PostgreSQL Database
      |
      | SQL / Data Analysis
      v
Power BI
      |
      v
Interactive Banking Dashboard
```

## Dataset

The project contains five datasets.

| Dataset | Records | Purpose |
|---|---:|---|
| Customers | 500 | Customer demographic and contact information |
| Branches | 20 | Branch, city, state and IFSC information |
| Accounts | 700 | Customer accounts and current balances |
| Transactions | 5,000 | Banking transactions and payment modes |
| Loans | 200 | Customer loans, amounts, interest rates and status |

All five datasets were checked during the project review and contain no missing values or duplicate rows.

## Dataset Details

### Customers

Contains customer-level information such as:

- Customer ID
- Customer name
- Gender
- Date of birth
- Mobile number
- Email
- City
- State
- Occupation

### Branches

Contains:

- Branch ID
- Branch name
- City
- State
- IFSC

The dataset contains 20 branches across Mumbai, Pune, Delhi, Bangalore and Hyderabad.

### Accounts

Contains:

- Account number
- Customer ID
- Branch ID
- Account type
- Opening date
- Current balance
- Account status

There are 700 accounts in the dataset.

Account types include:

- Savings
- Current

### Transactions

Contains:

- Transaction ID
- Account number
- Transaction date
- Transaction type
- Amount
- Payment mode

The dataset contains 5,000 transactions.

Payment modes include:

- NEFT
- UPI
- IMPS
- ATM
- Cash

### Loans

Contains:

- Loan ID
- Customer ID
- Loan type
- Loan amount
- Interest rate
- Loan status

The dataset contains 200 loans.

Loan types include:

- Gold
- Education
- Home
- Car
- Personal

## Python Data Loading Pipeline

The `load_data.py` script is responsible for loading the CSV files into PostgreSQL.

### Processing performed by the script

1. Establishes a PostgreSQL connection using SQLAlchemy.
2. Reads the five CSV files using Pandas.
3. Converts column names to lowercase.
4. Converts relevant date columns to datetime format.
5. Loads each dataset into PostgreSQL tables using Pandas `to_sql()`.

### PostgreSQL Tables

The Python script loads the following tables:

```text
customers
branches
accounts
transactions
loans
```

## Data Transformation

The Python pipeline performs the following transformations before loading:

```python
customers.columns = customers.columns.str.lower()
branches.columns = branches.columns.str.lower()
accounts.columns = accounts.columns.str.lower()
transactions.columns = transactions.columns.str.lower()
loans.columns = loans.columns.str.lower()
```

Date columns are converted using Pandas:

```python
customers["dob"] = pd.to_datetime(customers["dob"])

accounts["openingdate"] = pd.to_datetime(accounts["openingdate"])

transactions["transactiondate"] = pd.to_datetime(
    transactions["transactiondate"]
)
```

The cleaned DataFrames are then loaded into PostgreSQL using SQLAlchemy.

## Database Layer

PostgreSQL is used as the central database for the project.

The database contains separate tables for:

```text
customers
branches
accounts
transactions
loans
```

This structure separates the major banking entities and allows the data to be queried and analyzed using SQL.

## Power BI Dashboard

The project includes a Power BI dashboard built from the banking data.

The dashboard provides a high-level view of banking activity using KPI cards, charts and slicers.

### Dashboard KPIs

The provided dashboard view displays:

- Total Accounts
- Total Customers
- Total Balance
- Total Loan Amount

### Dashboard Visualizations

The dashboard includes:

- Customer count by city
- Account count by account type
- Current balance by branch
- Monthly transaction amount
- Loan count by loan type
- Transaction amount by payment mode

### Dashboard Filters

The dashboard provides filters for:

- City
- State
- Branch
- Account type

These filters allow users to interactively analyze different segments of the banking data.

## Dashboard Snapshot

The repository contains the Power BI dashboard file:

```text
output/banking.pbix
```

A dashboard view includes KPIs such as total customers, total accounts, total balance and total loan amount, along with branch, city, loan type, payment mode and monthly transaction analysis.

## Key Dataset Metrics

Based on the complete source datasets:

| Metric | Value |
|---|---:|
| Customers | 500 |
| Accounts | 700 |
| Branches | 20 |
| Transactions | 5,000 |
| Loans | 200 |
| Total account balance | 175,134,257 |
| Total loan amount | 495,415,244 |

The dashboard screenshot can display different values depending on the active filters. Therefore, dashboard KPI values should be interpreted according to the selected filter context.

## Analysis Areas

The project supports analysis across several banking dimensions.

### Customer Analysis

- Customer distribution by city
- Customer demographic information
- Occupation analysis
- Customer-to-account relationships

### Account Analysis

- Account types
- Account balances
- Account status
- Branch-level account information

### Transaction Analysis

- Transaction volume
- Transaction amounts
- Credit and debit transactions
- Payment mode analysis
- Monthly transaction trends

### Loan Analysis

- Loan distribution by type
- Loan amount
- Interest rate
- Active and closed loans
- Customer-level loan information

### Branch Analysis

- Branch distribution by city
- Branch-level balances
- State-level banking presence
- Branch performance analysis

## Project Structure

```text
Banking_Project/
|
├── data/
│   ├── accounts.csv
│   ├── branches.csv
│   ├── customers.csv
│   ├── loans.csv
│   └── transactions.csv
│
├── output/
│   └── banking.pbix
│
├── scripts/
│   └── load_data.py
│
├── requirements.txt.txt
└── README.md
```

## How to Run the Project

### Prerequisites

Install the following:

- Python 3.x
- PostgreSQL
- pgAdmin or another PostgreSQL client
- Power BI Desktop

### 1. Clone the Repository

```bash
git clone https://github.com/rushi-ahirrao/Banking_Project.git
cd Banking_Project
```

### 2. Create the PostgreSQL Database

Create a database named:

```text
banking_db
```

### 3. Install Python Dependencies

The Python script uses:

```text
pandas
sqlalchemy
psycopg2
```

Install the required packages:

```bash
pip install pandas sqlalchemy psycopg2-binary
```

### 4. Configure the Database Connection

Open:

```text
scripts/load_data.py
```

Update the PostgreSQL connection details with your own credentials:

```python
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "banking_db"
```

Do not commit database passwords or other credentials to GitHub.

### 5. Run the Data Loading Script

From the `scripts` directory:

```bash
cd scripts
python load_data.py
```

The script reads the CSV files from the `data` directory and loads them into PostgreSQL.

### 6. Open the Power BI Dashboard

Open:

```text
output/banking.pbix
```

Connect Power BI to the PostgreSQL database if required and refresh the data.

## SQL Analysis

Once the data is loaded into PostgreSQL, SQL can be used to perform analysis such as:

- Customer counts
- Account balances
- Branch-level analysis
- Transaction analysis
- Payment mode analysis
- Loan analysis
- Monthly trends
- Account type analysis

## Skills Demonstrated

### Data Engineering

- Data ingestion
- CSV processing
- Data transformation
- Database loading
- PostgreSQL
- Python-based ETL
- SQLAlchemy
- Structured data organization

### Data Analysis

- Aggregation
- Trend analysis
- Customer analysis
- Account analysis
- Loan analysis
- Transaction analysis
- Branch analysis

### Business Intelligence

- Power BI dashboard development
- KPI reporting
- Interactive filtering
- Data visualization
- Business-oriented reporting

## Important Security Note

The original Python script contains database connection credentials.

Before publishing or updating this project on GitHub, replace hard-coded credentials with environment variables or another secure configuration method.

For example:

```python
import os

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "banking_db")
```

Never upload real database passwords, API keys, tokens or other secrets to a public repository.

## Future Improvements

Potential improvements to make the project more production-oriented:

- Add a proper `requirements.txt` file.
- Move database credentials to environment variables.
- Add SQL schema and analytical queries to the repository.
- Add primary and foreign key constraints.
- Add data validation checks before loading.
- Add logging and error handling to the Python pipeline.
- Use a staging layer before loading production tables.
- Add incremental data loading instead of only appending data.
- Add automated data quality checks.
- Add more SQL analysis and documented business insights.
- Improve the Power BI data model with clearly defined relationships and measures.

## Project Outcome

This project demonstrates an end-to-end workflow in which raw banking CSV files are processed with Python, loaded into PostgreSQL, analyzed using SQL, and presented through an interactive Power BI dashboard.

It provides practical exposure to the core workflow used in data-oriented projects:

```text
Extract → Transform → Load → Analyze → Visualize
```

## Author

**Rushikesh Ahirrao**

GitHub: https://github.com/rushi-ahirrao/Banking_Project
