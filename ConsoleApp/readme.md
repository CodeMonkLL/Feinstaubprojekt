Natürlich! Hier ist ein Beispiel für eine **README**-Datei für dein Konsolenprojekt:

---

# Feinstaub Konsolenanwendung

Dieses Projekt ist eine Konsolenanwendung, die es ermöglicht, Feinstaubdaten in eine SQLite-Datenbank zu laden und diese anschließend nach verschiedenen Kriterien abzurufen. Die Anwendung nutzt Python und arbeitet direkt mit der SQLite-Datenbank über SQL, ohne ein ORM (Object-Relational Mapping).

## Projektbeschreibung

Das Ziel dieses Projekts ist es, Feinstaubdaten aus einer externen Quelle herunterzuladen und in eine SQLite-Datenbank zu speichern. Die Anwendung ermöglicht es, die Daten nach verschiedenen Zeiträumen in die Datenbank zu laden und später über SQL abzurufen. Dies dient als Grundlage für eine zukünftige Django-Webanwendung, die mit denselben Daten arbeitet.

### Funktionen:

- Feinstaubdaten aus einer CSV-Datei in die SQLite-Datenbank laden.
- Auswahl des Datumsbereichs für das Laden der Daten.
- Abrufen der Daten aus der SQLite-Datenbank basierend auf einem angegebenen Zeitraum.

## Installation

### 1. Klone das Repository:

```bash
git clone https://github.com/CodeMonkLL/Feinstaubprojekt
cd feinstaub-projekt
```

### 3. Installiere die benötigten Bibliotheken:

Da dieses Projekt nur die Python-Standardbibliothek verwendet, müssen keine externen Bibliotheken installiert werden. Sollte es in Zukunft zu Erweiterungen kommen, können benötigte Bibliotheken über `pip` installiert werden.

## Verwendete Bibliotheken

Dieses Projekt verwendet **nur die Python-Standardbibliothek**:

- `sqlite3`: Für die Verbindung zur SQLite-Datenbank und die Ausführung von SQL-Abfragen.
- `csv`: Für das Einlesen von CSV-Daten.
- `datetime`: Zur Verarbeitung von Datumsangaben und zur Auswahl von Zeiträumen.

**Keine externen Bibliotheken sind erforderlich.**

## Datenladen

Die Feinstaubdaten können auf zwei Arten in die Datenbank geladen werden:

1. **Alle Daten laden**: Lädt alle verfügbaren Daten in die Datenbank.
2. **Daten für einen bestimmten Zeitraum laden**: Du kannst einen Zeitraum angeben (z. B. von einem Start- bis zu einem Enddatum), und nur die Daten in diesem Zeitraum werden in die Datenbank geladen.

Die Daten werden als CSV-Datei bereitgestellt, und die Anwendung liest diese Datei, um die Daten in die SQLite-Datenbank einzufügen.

## Datenabruf

Du kannst die Feinstaubdaten nach einem bestimmten Zeitraum abrufen. Dies kann entweder für alle Daten oder für einen benutzerdefinierten Zeitraum erfolgen, indem du Start- und Enddatum angibst.

```

### Hinweise:
- Das Projekt arbeitet mit einer SQLite-Datenbank, die lokal auf dem Computer gespeichert wird. Der Datenbankname ist `feinstaub.db`.
- Das CSV-Datenformat für den Import sollte den entsprechenden Feinstaubdaten entsprechen (siehe `data_loader.py` für das genaue Format).

```
