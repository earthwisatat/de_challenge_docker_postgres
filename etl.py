import pandas as pd
import psycopg2
from sqlalchemy import create_engine, Integer, String, Date, Numeric

# Reading Excel data
df_foodsales = pd.read_excel('de_challenge_data.xlsx', sheet_name='FoodSales', skiprows=1, usecols='A:I')

# Rename columns in case column name is not the same
df_foodsales.columns = ['id', 'date', 'region', 'city', 'category', 'product', 'qty', 'unitprice', 'totalprice']

# Drop Null Value
df_foodsales_wo_nan = df_foodsales.dropna(subset=['date'])

# Selecting data that's not column name
df_foodsales_wo_nan_col = df_foodsales_wo_nan[df_foodsales_wo_nan['id']!='ID']

# PostgreSQL Parameters
user    = 'root'
password    = 'DataEngineer_2023'
host    = 'localhost'
port    = '5432'
dbname  = 'challenge'

# Create a connection engine using SQLAlchemy
# https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#dialect-postgresql-psycopg2-connect
connection_str = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'
engine = create_engine(connection_str)

# Define data types for each column before to_sql
data_types = {
    'id': String(primary_key=True),
    'date': Date(),
    'region': String(),
    'city': String(),
    'category': String(),
    'product': String(),
    'qty': Integer(),
    'unitprice': Numeric(),
    'totalprice': Numeric()
}

# Insert data into SQL using connection engine
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html#pandas.DataFrame.to_sql
df_foodsales_wo_nan_col.to_sql('food_sales', con=engine, if_exists='replace', index=False, dtype=data_types)

# Close the connection engine
engine.dispose()