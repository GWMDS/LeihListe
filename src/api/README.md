# Backend
In dieser README wird beschrieben, wie man den FastAPI-Server zum laufen bekommt

## Projekt Einrichtung

Python ([Download-Link](https://www.python.org/downloads/)) installieren, unter Linux idealerweise mit dem Package Manager.
Dann im Verzeichnis `api` den folgenden Befehl ausführen

```sh
python -m venv .venv
```

Unter Windows dann bei Benutzung von CMD

```
.venv\Scripts\activate.bat
```

oder bei Benutzung von PowerShell

```
.venv\Scripts\Activate.ps1
```

oder unter Linux/MacOS

```sh
source .venv/bin/activate
```

die virtuelle Umgebung aktivieren und mit dem folgenen Befehl die benötigten Packages installieren

```sh
pip install -r requirements.txt
```

Hat das alles funktioniert, sollte man sich jetzt in der aktivierten virtuellen Umgebung mit den installieren Packages befinden.

### Run and Hot-Reload for Development

Bevor der API-Server gestartet werden kann, sollte die Datenbank laufen! Siehe README.md im `database` Verzeichnis.
Der Server liefert **keinen** Fehler, wenn die Datenbank noch nicht läuft, da SQLModel mit einer lazy Connection arbeitet, die Verbindung zur Datenbank also nur herstellt, wenn sie wirklich gebraucht wird.

Danach

```sh
fastapi dev app/main.py
```

Dieser Server lädt bei Speichern von Änderungen in Code automatisch die Änderungen direkt in die Webseite. Hot-Reload ist nicht immer perfekt, manchmal muss man auch einfach den Server neustarten.
FastAPI hat eine Benutzeroberfläche integriert, die einen Überblick über die implementierten Endpunkte liefert. Mit dieser kann man auch explorativ testen.

## Entwicklung

Für die Entwicklung mit FastAPI stehen die [FastAPI Reference](https://fastapi.tiangolo.com/reference/) und die [FastAPI Tutorials](https://fastapi.tiangolo.com/tutorial) zur Verfügung. Für SQLModel gibt es die [SQLModel Tutorials](https://sqlmodel.tiangolo.com/tutorial/).