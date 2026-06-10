# 04.06.26: Stakeholdermeeting 2

- Sprint 2 Ziele: Architecture.adoc, design.adoc wichtig
- durchgelesen oder zu kurzfristig?:
  - nicht geschafft

## Architektur

- C4 Modell: System was mit DB interagiert
- Nutzer, die mit System interagieren
- Laufzeitumgebung: Nutzer nutzt Browser für Oberfläche
- Browser kommuniziert mit Backend über API-Requests
- Backend schreibt auf DB
- API Server läuft *nicht* auf Docker Container
- DB liegt in Docker Container
- Verteilungsdiagramm noch nicht erstellt -> hat den ihre Gruppe auch nicht gemacht
- Vue.js Frontend, FastAPI Backend
- wir nutzen *nicht* DB der HTW
- Docker für Containerisierung
- Github Actions für CI/CD (Continous Integration, -Deployment)
-> testen ob Build geht, automatisches Skript, dass Produkt aufsetzt
- Architekturrelevante Anforderungen

--- 

- Frage: Nutzer irgendwie benachrichtigen/Pushbenachrichtungen -> externer Server?
  - -> Verknüpfung im Browser, für E-Mail Benachrichtigungen benötigt man externe Schnittstelle
  - -> im Scope, aber noch nicht geplant
- Frage: Architekturrelevante Anforderungen: langfristige Anforderungen?
  - -> könnte man reinnehmen, aber kann bisher noch nicht entschieden werden
  - -> sind Benachrichtigungen wirklich Architektur oder Thema Design?

- ADRs:
  - Webapp: Laufzeitumgebung als Browser mit UI
  - Relationale DB für Persistenz, zentral an einem Ort
  - Client/Server
  - Webframeworks (Vue.js), FastAPI
  - PostgreSQL
  - Docker zum Containerisieren

- Frage: Endpunkte der API hängen im Netz/Bösen greifen auf DB zu?
  - -> aktuell unsicher, bisher keine Authentifizierung
  - -> nicht vorhergesehen im Prototypen, Login ist aber vorgesehen

- Frage: Bilder von Produkten in DB
  - -> noch nicht festgeschrieben ob wir Bilder speichern
  - -> gibt auch noch anderen Lösungen außer DB (hier könnte sich was an Architektur ändern)

- Frage: Walking Skeleton?
  - -> man kann alles sepearat starten, aber noch keine Funktionalität über die verschiedenen Schichten
  - -> Aufgaben formuliert, PR dazu braucht noch mehr Reviews

## Design

- sonst noch beim Miroboard Verleihworkflow hinzugefügt (hatten vorher nur Ausleihworkflow)
- Ausleihbare Gegenstände + Details dazu
- Wer hats ausgeliehen + Prüfung, ob zurückgegeben
- Button sind Gegenstände
- Gegenstände hinzufügen/löschen

---

- Bedienung schön einfach
- Frage: 10 gleichartige Gegenstände, unterscheidbar? (z.B. 10 Mikroskope)
  - -> wahrscheinlich 10 einzige, weil unterschiedliche Zustände

- schlecht, weil große Liste
  -  -> Untermenü für einzelne Gegenstände?