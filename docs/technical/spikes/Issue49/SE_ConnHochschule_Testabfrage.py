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
