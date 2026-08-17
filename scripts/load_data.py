import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL Connection Details


DB_USER = "postgres"
DB_PASSWORD = "47896" 
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "banking_db"


# Create Engine


engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print(" Connected to PostgreSQL Successfully!")


# Read CSV Files


customers = pd.read_csv("../data/customers.csv")
branches = pd.read_csv("../data/branches.csv")
accounts = pd.read_csv("../data/accounts.csv")
transactions = pd.read_csv("../data/transactions.csv")
loans = pd.read_csv("../data/loans.csv")

print(" CSV Files Loaded Successfully!")


# Convert Column Names to Lowercase


customers.columns = customers.columns.str.lower()
branches.columns = branches.columns.str.lower()
accounts.columns = accounts.columns.str.lower()
transactions.columns = transactions.columns.str.lower()
loans.columns = loans.columns.str.lower()

# Convert Date Columns


customers["dob"] = pd.to_datetime(customers["dob"])

accounts["openingdate"] = pd.to_datetime(
    accounts["openingdate"]
)

transactions["transactiondate"] = pd.to_datetime(
    transactions["transactiondate"]
)


# Upload Customers


print("Uploading Customers...")

customers.to_sql(
    "customers",
    engine,
    if_exists="append",
    index=False
)

print(" Customers Uploaded")


# Upload Branches


print("Uploading Branches...")

branches.to_sql(
    "branches",
    engine,
    if_exists="append",
    index=False
)

print(" Branches Uploaded")


# Upload Accounts


print("Uploading Accounts...")

accounts.to_sql(
    "accounts",
    engine,
    if_exists="append",
    index=False
)

print(" Accounts Uploaded")


# Upload Transactions


print("Uploading Transactions...")

transactions.to_sql(
    "transactions",
    engine,
    if_exists="append",
    index=False
)

print("Transactions Uploaded")


# Upload Loans


print("Uploading Loans...")

loans.to_sql(
    "loans",
    engine,
    if_exists="append",
    index=False
)

print(" Loans Uploaded")

print("\n ALL DATA IMPORTED SUCCESSFULLY ")