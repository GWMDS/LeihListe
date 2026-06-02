# Lokale Datenbank für Entwicklungszwecke

Docker ([Download-Link](https://www.docker.com/)) installieren, unter Linux idealerweise mit dem Package Manager.
Danach in diesem Verzeichnis mittels

```sh
touch .env
```

eine .env erstellen und nach Vorbild der example.env befüllen. Die .env ist in der .gitignore enthalten, wird also nicht getracked und sollte deshalb **nicht** im repo erscheinen.
Die genauen Zugangsdaten sind relativ irrelevant, sollten aber mit der .env im /api Verzeichnis übereinstimmen.
Danach folgenden Befel ausführen:

```sh
docker compose up -d
```

Dieser Befehl startet lokal einen Docker Container, in dem eine PostgreSQL-Datenbank läuft. Mit dieser kann sich dann das Backend verbinden.
Das -d Flag startet den Container im "detached mode", also im Hintergrund. Das kann weggelassen werden, ist aber angenehmer so.

Zum überprüfen, ob die Datenbank läuft kann der Befehl

```sh
docker compose ps
```
oder auch 

```sh
docker ps
```

genutzt werden.

Die Datenbank kann mit

```sh
docker compose down
```

gestoppt werden.

Sowohl für das Starten als auch das Stoppen ist es notwendig im Verzeichnis `database` zu sein.

## Tipp für die Entwicklung
Bei Anpassung des Datenschemas kann es sein, dass die Änderungen nicht in der Datenbank übernommen werden.
Für diesen Fall ist es sinnvoll, das volume der Datenbank zu löschen, damit es beim nächsten Start der Containers neu erstellt werden muss.

Mit
```sh
docker volume ls
```
listet man alle existierenden Docker volumes auf.

Mittels
```sh
docker volume rm <name>
```
kann das gewünschte volume dann gelöscht werden.