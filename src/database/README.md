# Lokale Datenbank für Entwicklungszwecke

Docker ([Download-Link](https://www.docker.com/)) installieren, unter Linux idealerweise mit dem Package Manager.
In diesem Verzeichnis eine `.env` nach Vorbilder der `example.env` erstellen und dann den folgenden Befehl ausführen

```sh
docker compose up -d
```

Damit startet lokal eine PostgreSQL Datenbank, die von dem Backend angesprochen werden kann.

Zum überprüfen, ob die Datenbank läuft kann der Befehl

```sh
docker compose ps
```

genutzt werden.

Die Datenbank kann mit

```sh
docker compose down
```

gestoppt werden.

Sowohl für das Starten als auch das Stoppen ist es notwendig im Verzeichnis `database` zu sein.