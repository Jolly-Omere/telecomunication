# src/main.py

import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connection parameters
connection_params = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME")
}

# Create engine to connect to PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}")

# SQL query to fetch data
sql_query = 'SELECT * FROM xdr_data LIMIT 5'

# Read data into Pandas DataFrame
df = pd.read_sql(sql_query, con=engine)

# Display the DataFrame
print(df)