# 22.05.26: Dev-Meeting 1

Wünsche/Kenntnisse:
- Franz:
  - Sprachen: Java (Prog II, TU Dresden), C (Prog I), JS, Grundkenntnisse Python
  - Wünsche:
    - Frontend: Vue.js
    - DB: MySQL (bevorzugt)
    - FastAPI läuft in Python
  - Datenbankkommunikation geht über ORM
- Marius:
  - SE II: FastAPI Erfahrung + Zugriff auf funktionierenden Code
  - Docker nicht auseinandergesetzt
  - Sprachen: C, C++, Python
  - für Backend FastAPI, Python einfach zu lernen
  - Frontend: Vue.js
  - Persistenz egal (schon für PostgreSQL was fertig)
  - Server Client
- Eric
  - Frontend: Vue.js mit Vuetify als Componentlibary (kenne ich bereits, relativ einfach) -> Adresse zum Backend in Umgebungsvariable (nicht hardcoden) 
  - Backend: Python mit sqlalchemy (hatten wir mal in Modul DB) & FastAPI (hat gute Onlineübersicht mit Endpunkten, welches automatisch erstellt wird)   
  - Persistenz: Irgendeine DB, die mit dem Backend gut funktioniert (MySQL, MS SQL Server, ...) -> Zugangsdaten in Umgebungsvariablen (nicht in dem Code packen) 
  - Empfehlenswert das Backend + DB zusammen auf einer VM in der HTW zu haben, damit alle auf dieselben Daten zugreifen können während der Entwicklung
  - vielleicht einfach MS SQL Server der HTW nutzen (hat Hr. Ringel empfohlen)
  - Frontend muss nicht zwingend auf der VM sein -> nur für Endpräsentation?
  - Nicht Code selber schreiben, wenn es dafür bereits gute Bibliotheken gibt (npm packages)
- Pascal:
  - Sprachen: C, Python, Java
  - eher Backend
  - sonst weniger Ahnung von Frontend
  - Wünsche: Python in Backend
- Kevin:
  - Sprachen: C, Java
  - minimale Erfahrung Vue.js
  - eher Interesse an Backend (Kenntnisse in PHP, Typescript)
  - ist auch für FastAPI, wenn es die anderen nutzen

---

- grobes Architekturschema (architecture.adoc):
  - Ausleihdienst, die eine Institution anbietet
  - Client/Server Arch.
  - zwei separate Stücke: API kommuniziert über HTTP Requests mit Frontend
  - Webapp (soll im Browser laufen)
  - erstmal nur vorgeschlagen

- => Entscheidung für Frontend: Vue.js (alle einig)

- Backend:
  - FastAPI
    - main.py: Lifespan Fkt., die ausgeführt wird bevor Serverstart -> z.B. für Testdaten
    - Router inkludieren in separaten Dateien
    - Swagger UI unter /docs
  - Node.js
    - JS Backendserver
    - hört auf Port 3000
    - JS kompliziert, deshalb eher nicht nutzen
  - Django
    - für Enterpriseanwendungen
    - robust mit vielen Einstellungen
    - FastAPI hat kleinere Lernkurve
- => Entscheidung für: FastAPI

- Persistenz:
  - PostgreSQL
    - Docker Compose (Image runterziehen)
    - in Container läuft DB, kann sich damit verbinden
    - sehr einfach (ein Befehl)
  - Pascal: Spike zu DB-Verbindung mit MS SQL Server der HTW
    - Hr. Toll Skript angepasst
    - komplex, da mit UI
    - umgeschrieben sodass Parameter über cmdline
    - VPN muss aktiv sein, um DB nutzen zu können (geht nicht ohne)
    - kann Skript nicht zeigen, da Multiboot -> wird in Discord hochgeladen
- => Entscheidung für: MS SQL (nervig mit VPN, aber jeder hat Zugriff auf dieselben Daten)
 
---

- Aufgabenbereiche:
  - Frontend: Eric, Franz
  - Backend: Pascal, Kevin
  
- Marius packt erstes Code-Grundgerüst ins Repo
- erste Interaktionen für Backend
- => Aufgabe: schon mal ein bisschen einlesen zu Aufgabenbereichen

- Jonas muss UserStories priorisieren für Prototyp
- Frage: nächstes Semester mit diesem Team? -> wohl nicht
- Domainmodell Review: schaut sich bald Marius an