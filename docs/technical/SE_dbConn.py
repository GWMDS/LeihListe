import pyodbc

"""stellt nur Verbindung mit DBS her"""
"""Database, uid und pwd mit s-nummer ersetzen"""
def getConn ():
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=141.56.2.46;"
                          "Database=ii24s87929;"
                          "uid=s87929;pwd=s87929")
    return cnxn
