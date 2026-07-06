# 18.06.26: Stakeholdermeeting 3

- Ausgeliehen/Verfügbar jetzt verfügbar
- nächste Woche Ausleihen geplant, aber noch nicht im aktuellen Scope
- -> Zeitraum eingeben als Filter?
- Screenshots:
  - 1 ist Inventarliste
  - 2 ist detaillierte Ansicht
  - 3 Fehlermeldung wenn offline
  - 4 als Testseite
- -> welche DB?: PostgreSQL als Dockercontainer

---

- Feedback Design: ok oder nicht?
  - -> Was wenn viele Seiten?
  - -> Testdaten klarer (nicht nur Item 0)
  - -> nur Bild, Titel und ob Ausgeliehen (keine Kategorie in Übersicht)
  - Beschreibung limitiert auf eine Zeile
  - Kategorie als Tag?
  - -> Bild nur bei Details? -> drei Usecases:
    - weiß was ich haben will: Suchen
    - ungefähr wissen: nach Kategorie filtern
    - ganz neugierig: alles durchstöbern, deshalb interessanter wenn Bild in Übersicht
  - -> Idee: Togglebutton zum Umschalten zwischen Liste und Bildern

---

- auf Detailseite: neben Schließen-Btn gibt es bald Ausleihen-Btn
- -> Idee: nicht Ausleihprozess je Gegenstand -> Warenkorb
- Button Ausleihen schon vor Präsi einfügen ist geplant
- bei Detailansicht nicht ID anzeigen (als Nutzer interessiert dich das nicht)
- -> Frage: bei Ausleihbutton einloggen?
  - wir machen dieses Semester noch kein Mehrnutzersystem, bisher automatisch eingeloggt
- bei Test-Seite dann "Meine Ausleihen"
- Fehlermeldung Schließen-Button schließt diese (für die ungeduldigen)