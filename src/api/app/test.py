import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=141.56.2.45;"
    "DATABASE=ii23s86306;"
    "UID=s86306;"
    "PWD=s86306;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;",
    timeout=5
)

print("Connected!")