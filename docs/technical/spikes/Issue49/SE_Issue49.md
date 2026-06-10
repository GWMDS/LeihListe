# Spike: Verbindung mit MS SQL Server der Hochschule
## Leitfrage: Wie können wir uns mit der Bibliothek in einem Python Skript mit dem MS SQL Server der Hochschule von außerhalb verbinden und mit der DB interagieren

### Vorraussetzung
- VPN-Tunnel zur HTW (mittels Edu-VPN)
- Bibliothek für "pyodbc" muss installiert sein

### Beschreibung
- Skript baut erfolgreich Verbindung zum DBS-Server der Hochschul auf und macht eine Testabfrage

### Erkenntnis
- alle Teammitglieder müssen für Arbeit auf DB und Tests VPN-Tunnel nutzen
- Datenbanken aus "Datenbanksysteme 2" werden nach gewisser Zeit gelöscht -> müssten Verlängerung beantragen -> unnötige Abhängigkeit
- Skript ist online in Git Hub einsehbar, enthaelt jedoch Anmeldedaten

### Fazit
- Umstieg auf eine PostgreSQL Datenbank die jeder bei sich lokal nutzen kann
    -> keine Abhängigkeit von VPN-Tunnel
    -> eigene DBS werden nicht gelöscht
    -> jeder hat Anmeldedaten lokal auf seinem Rechner in separater Datei -> werden als Variablen übergeben
    -> jeder muss Docker insatllieren -> Anleitung bgereits vorhanden


```python
import pyodbc

# stellt nur Verbindung mit DBS her
# Database, uid und pwd mit s-nummer ersetzen
# Quelle Driver: https://learn.microsoft.com/de-de/troubleshoot/sql/database-engine/install/windows/odbc-driver-install-checking
def getConn ():
    cnxn = pyodbc.connect("Driver={sql server};"
                          "Server=141.56.2.46;"
                          "Database=ii24s87929;"
                          "uid=s87929;pwd=s87929")
    return cnxn
```

```python
# Datei fuer Verbindungsaufbau
from SE_dbConn import getConn

# Definitionsbereich
# Fkt. gibt Mitarbeiter zu gegebener MitID aus 
def getMitarbeiter(mitNr):

    # Abfrage in try-catch-Block um Absturz Programm bei fehlerhafter Abfrage zu vermeiden
    try:
        # hier kommt SQL Abfrage hinein
        cursor.execute('SELECT MitID, MitName, MitVorname, MitGebDat, MitJob, MitStundensatz, MitEinsatzort from Mitarbeiter where MitID = ?', (mitNr))
    except:
        print('Abfrage ist fehlerhaft')
        cursor.close()
        return

    # Leere Ergebnismenge abfangen
    if cursor.rowcount == 0:
        print('Kein Mitarbeiter gefunden')
        cursor.close()
        return 0

    # fuer Ausgabe Attribute von Mitarbeiter zustaendig (Zeile 25 muss genauso viele row[]-Angaben haben wie Attribute bei SQL-Befehl abgefragt werden)
    print('\nMitarbeiter:')
    liste_mit = [0]
    for row in cursor:
        print(row[0], ' - ', row[1], ' - ', row[2], ' - ', row[3], ' - ', row[4], ' - ', row[5], ' - ', row[6])
        liste_mit.append(int(row[0]))

    # schliesst Verbindung
    cursor.close()
    conn.close()

# Hier beginnt Programmcode
# baut Verbindung zum Hochschulserver auf
conn = getConn()
cursor = conn.cursor()

# Eingabeaufforderung fuer MitarbeiterID
mitNr = input("MitarbeiterID eingeben: ")
print(mitNr)

# ruft oben definierte Fkt. auf
getMitarbeiter(mitNr)
```