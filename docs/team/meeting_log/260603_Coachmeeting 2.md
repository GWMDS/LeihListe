# 03.06.26: Coachmeeting 2

- verantworlich für 4 Teams (Leihliste / EventFlow)
- Agenda
  - 10-15 Min. Fragen stellen
  - 10 Min. zum Stand Sprint 2
  - Gründe Stärken/Probleme
  - Ausblick

- Teamreviewer anderer Teams nie kontaktiert: 
  - wird nochmal als Feedback gegeben
  - Reviewprozess kann Qualität erhöhen + (Un)sicherheit erzeugen
- Schwierige Aufgabenverteilung
  - Analyse liegt eher an PO
  - Devs fallen unter
  - Aufgaben schlecht aufzuteilen
  - -> PO verantwortlich für Funkt. / Abnahmebedingung
  - -> macht aber nicht die ganze Arbeit
  - -> Produktvision wird vom Team verstanden (schlecht wenn eine Person verantwortlich)
  - -> Architekt gibt 2 Architekturvarianten (Devs können darüber diskutieren)
  - -> Last verschiebt sich von Arch. zu Implementation
  - -> Person ist verantwortlich, aber macht es nie alleine
  - -> mit als Learning auf Agenda nehmen

- Frage: Unsicher als Rolle des Scrum Master
  - sonst nicht wirklich an Implementierungsachen beschäftigt
  - fehlt das was?
  - -> Wie eng sieht man die Rolle des SM?
  - -> eher SM und Teammanager: manchmal auch unangenehme Entscheidungen treffen, damit Arbeit vorwärts geht
  - -> Gefühl haben, das alle Teammitglieder sich gemäß Fähigkeiten in Aufgaben einbringen
  - -> SM schaut 2 Schritte in Zukunft
  - -> heißt nicht, dass SM irgendwann Code schreibt

---

- aktueller Arbeitsstand:
  - Architektur noch nicht Fix -> braucht Review
  - Code initialisiert
  - 2 (Mini)Implentierungsaufgaben für Frontend/Backend
  - sonst auf dem richtigen Level
- Sprint: 1/2 Wochen Puffer, Ende diese Woche
- begründete techn. Richtung, nicht vollst. Arch.
- Client/Server
  - Frontend: Vue.js (leichte Lernkurve)
  - Backend: FastAPI (bereits Expertise)
  - Persistenz: PostgreSQL (dagegen, weil VPN; Docker einfacher)
- -> sollte funktionieren, weil Expertise & Feature realisieren lassen
- Wireframes vereinbart, Git-Vereinbarung, init. Domainmodell
- -> passt, Ziel erreicht!

---

Reflexion: 
- Stärken:
  - jeder erledigt Aufgaben fristgemäß (außer 1 Fall)
  - inhaltlich weiter im Arbeitstand -> auf Kurs
  - Expertise, um es techn. umzusetzen
  - Mittwochs Meeting, jeder trägt alles in Miro ein, besprechen was in nächster Woche (max. 20 Min)
  - Sprint Planning / Retrospektive immer noch keinen Fahrplan
  - nur grobe Meta-Aufgaben und keine Aufwandschätzung -> Runterbrechen in einzelne Bausteine schwierig
  - -> das in Learning von Sprint 2 schreiben, unerfahren und zu schwer zerlegbar
  - -> Aufgaben inherent, erst am Ende zusammen packen (vorher einzeln an DB, API, Frontend arbeiten)

- Schwächen:
  - Problem schwierig in Worte zu fassen -> versuchen Scrum umzusetzen und warum manche Rollen existieren
  - Jonas wollte Refinement machen und hat Aufgabe gegeben, dass sich jeder Gedanken zu machen soll, welche US zuerst umgesetzt werden sollen -> eigentlich Aufgabe des PO
  - -> auch Punkt für Reflexion: dazu verständigen, YT-Video schauen, KI fragen
  - -> PO gibt Akzeptanzkriterien, ob Release akzeptiert sind
  - -> fehlende Betriebsverantwortung (Production, Rolling Release)
  - -> Rollenverständnis, -grenzen, -überschneidung
  - immer die Frage zu stellen, was die Gründe sind für Schwächen?
  - Ausblick Wintersemester: wird dann voraussichtlich aufgelöst

---

Ausblick:
  - Sprint 3: erstes lauffähiges Produktinkrement
  - jeder hat subjektive Eigenleistung + Learning von Software Engineering
  - Rollen für Dev-Team festgelegt
  - Miro-Board mit Ideen/Aufgaben (nicht nur für Dev-Team)
  - Dev-Team hatte am wenigsten gemacht (nicht daran schuld)
  - nicht klar, welche User Stories festgelegt sind
  - -> SM/PO sollten das Do./Fr. vorbesprechen (macht Sinn und jeder Dev hat was zu tun)
  - Frage Sprint Planning: Aufwandschätzung sinnvoll
  - -> noch nicht bei Sprint 3
  - -> wenn es mit Workload Probleme gibt, fängt man an Abzuschätzen
  - -> Zeitbedarf sehr abhängig von Erfahrungen
  - -> machbar und fair verteilt
  - -> z.B. Benutzer meldet sich an und bekommt eine Liste von ausgeliehenen Sachen
  - -> Account Löschung und kann sich danach nicht mehr anmelden
  - -> ein Fall überlegen, welcher zu Änderung in DB führt
  - -> auf mobilen Endgerät/Laptop zeigen -> Responsive Design
  - -> DB muss nicht vollständig sein
  - -> Lernziel: nicht perfektes Produkt, sondern Learnings
  - -> Sprint 2 formal zuende bringen
  - -> Learning notieren
  - -> kein Meeting in Sprint 3