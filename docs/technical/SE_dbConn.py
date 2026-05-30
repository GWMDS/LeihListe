import pyodbc

# stellt nur Verbindung mit DBS her
# Database, uid und pwd mit s-nummer ersetzen
def getConn ():
    cnxn = pyodbc.connect("Driver={sql server};"
                          "Server=141.56.2.46;"
                          "Database=ixxxs12345;"	# Bsp.: ii24s12345 (ii...allg. Informatik; 24...Immatrikulationsjahr)
                          "uid=s12345;pwd=s12345")
    return cnxn
