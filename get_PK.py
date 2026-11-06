import pyodbc
import pandas as pd
from itertools import combinations

# Database connection details
server = 'your_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'

# Establish the connection
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# The table to analyze
table_name = 'YourTableName'

# Fetch column names
query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"
columns_df = pd.read_sql(query, conn)
columns = columns_df['COLUMN_NAME'].tolist()

# Function to check if a combination of columns is unique
def is_unique_combination(combination):
    columns_str = ', '.join(combination)
    query = f"""
    SELECT COUNT(*) AS total_rows, COUNT(DISTINCT {columns_str}) AS unique_rows
    FROM {table_name}
    """
    result = pd.read_sql(query, conn)
    return result['total_rows'][0] == result['unique_rows'][0]

# Find all combinations of the columns
potential_primary_keys = []
for i in range(1, len(columns) + 1):
    for combo in combinations(columns, i):
        if is_unique_combination(combo):
            potential_primary_keys.append(combo)

# Output potential primary key combinations
if potential_primary_keys:
    print("Potential primary key combinations are:")
    for pk in potential_primary_keys:
        print(pk)
else:
    print("No unique column combinations found.")

# Close the database connection
conn.close()
