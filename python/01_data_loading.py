import pandas as pd
from sqlalchemy import create_engine

# Replace this with your actual SQL Server instance name.
# Examples:
# SERVER = r"localhost"
# SERVER = r".\SQLEXPRESS"
# SERVER = r"DESKTOP-ABC123\SQLEXPRESS"
SERVER = r"localhost"
DATABASE = "GarmentProductivityDB"

connection_string = (
    "mssql+pyodbc://@"
    + SERVER
    + "/"
    + DATABASE
    + "?driver=ODBC+Driver+17+for+SQL+Server"
    + "&Trusted_Connection=yes"
)

engine = create_engine(connection_string)

query = """
SELECT *
FROM ProductionProductivity
"""

try:
    df = pd.read_sql(query, engine)
    print("Data loaded successfully!")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print(df.head())

    output_path = "data/processed/garment_productivity_sql.csv"
    df.to_csv(output_path, index=False)
    print("SQL data saved to processed folder.")
except Exception as e:
    print("Connection or query failed.")
    print(f"Error: {e}")
    print("\nCheck the SQL Server instance name and make sure the database/table exist.")
