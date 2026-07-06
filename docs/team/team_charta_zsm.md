# Team Charta Notizen

### 4.1.1
Effektive Software Entwicklung erlernen, Software Enigneering realitätsnah erlernen, agile und effektive Entwicklung, Erfahrung für späteres Berufsleben sammeln, Programmierkenntnisse erweitern, nutzbare und weitgehend profesionelle Software erarbeiten, Teamfähigkeit ausbauen

### 4.1.2
Erfolg:
* Scrum Framework verstanden
* Produktive und effiziente Zusammenarbeit, Klare Kommunikation
* Termintreue
* Probleme erkennen und nennen; Konfliktlösung
* Strukturierte Meetings
* MVP (minimum viable Product)

Vermeiden:
* Terminverstösse
* Mediation durch externe 
* KI-Slop; Copy&Paste
* doppelte Arbeit durch schlechte Kommuniaktion/ Aufgabenaufteilung
* unstrukturierte Meetings (Zeitüberschreitungen)
* Featurecreep

### 4.2.1 Fragen zu den einzelnen Rollen 

#### Product Owner 
- **Hauptrolle:** Priorisiert und bestimmt, welche genauen Features und Implementierungen im Projekt landen, inhaltliche und geschäftliche Rahmenbedingungen
- **Aufgaben:** User Stories verfassen, Aktzeptanz Kriterien festlegen, Elemente und Features in Pläne schreiben oder entfernen, User Research, Stakeholder Gespräch
- **Ausfall:** Vertreter wird festgelegt, Entscheidungen werden mit dem Team besprochen.

#### Scrum Master 
- **Hauptrolle:** Sicherstellen einer guten und effizienten Zusammenarbeit im Team.
- **Aufgaben:** Koordiniert und moderiert Meetings, hilft bei Problemen und Konflikten, Verwaltung von GitHub, VErbesserung der Zusammenarbeit durch Retrospekiven
- **Ausfall:** Vertreter wird festgelegt oder Eigenorganisation im Team.

#### Tech Lead
- **Hauptrolle:** Chef bei Technikfragen und Entscheidungen
- **Aufgaben:** bereitet Meeting für technische Entscheidungen vor, hat letztes Wort bei Technikfragen, initialisiert src Ordner
-  **Ausfall:** Dev Team übernimmt

#### Developer Team 
- **Hauptrolle:** Verständlichen, gut strukturierten Code schreiben, Code Testen
- **Aufgaben:** Mitentscheiden bei Feature-Implementierung (Aufwand vs. Nutzen), Code testen, Code Review und Feedback, saubere Kommentare und Dokumentation, VErsionsverwaltung, Branching
- **Ausfall:** Andere Entwickler übernehmen Aufgaben; weniger relevante Features werden verschoben.

### 4.2.2 Entscheidungsfindung

- **Scope Entscheidungen:** Das letzte Wort hat der Product Owner; Ideen und Kritikpunkte sind vorher im Team ansprechbar.
- **Technische Architekturentscheidungen:** Tech Lead, Themen Experten
- **Wer eskaliert bei Blockaden:** Scrum Master (Kommunikation mit den Coaches), Organisation einer VM im HTW Netz
- **Review und Merging des Codes:** Alle Developer stehen mit Fachwissen bereit; Product Owner und Scrum Master übernehmen organisatorische Aufgaben im Repository.

## Kommunikation
### 4.3.1
- **Kanäle:**
  * Discord für Meetings und asynchrone Kommunikation
  * alternativ WhatsApp für 1:1 Kommunikation
  * Miro während Meetings als Whiteboard (Planung -> Projektaufbau, UserStories, Vorgehensweisen)
  * Github für Code, Bugs/ Tasks und Dokumentation
  * GitHub Projects (ProductBacklog, Aufgabenverwaltung, Risks)
* Antwort mindestens am selben Tag, sonst so zeitnah wie möglich
* Synchron: Fragen, Probleme, Meetings, die das ganze Team betreffen.
* Asynchron: Chat bei kleineren Fragen.

### 4.3.2
* Signalisierung der Erreichbarkeit ( online auf Discord??)

### 4.3.3
- Wie gehen wir mit Meinungsverschiedenheiten um?
  - Kompromiss finden oder Spike starten, beides ausprobieren und schauen, was besser funktioniert
- Was machen wir, wenn jemand blockiert ist?
  - ein anderer übernimmt soweit das möglich ist oder verschieben der Aufgaben der blockierten Person
- Wie treffen wir Entscheidungen, wenn das Team uneins ist?
  - versuchen gemeinsame Lösung im Team zu finden, objektiver Vergleich Vor- und Nachteile beider Lösungen

## Meetings
### 4.4.1

- Daily Standup: --> eher Weekly
  - könnte nervig sein ein extra 10-15 min Meeting zu machen 
  -> vielleicht nur als Chat, wo jeder so in der Hälfte der Woche reinschreibt, wie weit er ist, was noch gemacht werden muss und die Probleme
- Sprint Planning: 
  - findet nach Retrospektive statt, 1,5 Std.
  - vorbereitet vom Product Owner
  - Entwicklerteam bereitet Fragen vor
- Sprint Review: 
  - alle nehmen teil
  - Erreichte Aufgaben aus dem Sprint wird von jedem der Devs gezeigt
  - Feedback Zielgruppe (evtl. Sicht von anderen Teams)
- Retrospektive: 
  - vielleicht im Anschluss an Sprint Review?
  - Scrum Master moderiert
  - Miro für Sticky Notes (was lief gut/schlecht, Verbesserungsvorschläge etc.)
- Backlog Refinement: 
  - vor Sprint Planning
  - vorallem ProductOwner und Dev Team
  - Klärung von Ideen, Priorisierung, Abschätzen wieviele Aufgaben im Sprint geschafft werden können

## Vereinbarungen
- Branching: 
  - Feature Branches
  - z.B. branch von `main` auf `feature/login` (Namenskonvention?)
  - 1-2 Personen arbeiten daran (2 Personen müssen koordiniert arbeiten, sodass keine Konflikte im Featurebranch entstehen)

- Pull Requests: 
  - PR für fertiges Feature
  - Peer-Review: mind. 1 Approval von einem **anderen** Dev (am besten mit der selben Expertise) -> Gemergt kann von einem anderen Dev nach Approval
  - PR sollten niemals mehr als 1 Feature haben und nicht 50 Dateien ändern (dadurch steigt Risiko des Merge-Konflikts)

- Definition of Ready:
  - User Stories/Akzeptanzkriterien ausformuliert
  - Story klein genug, dass innerhalb Sprint umsetzbar
  - Wichtigkeit des Features bestätigt
  - keine Unklarheiten

- Definition of Done:
  - Code fertig geschrieben und getestet
  - mind. 1 Approval des PR
  - Akzeptanzkriterien erfüllt
  - Doku geschrieben (falls nötig)
  -> in `main` gemerged

- Weiteres:
  - Coding Styleguides?
  - immer Branch gleich hochladen, sodass manche schon vorher draufschauen können und evtl. Probleme frühzeitig erkannt werden