import sqlite3
import os

# Verbindungsdetails zur Datenbank
project_dir = os.path.dirname(os.path.abspath(__file__))  # Hauptprojektordner
db_path = os.path.join(project_dir, '..', 'Feinstaub', 'feinstaubproject', 'db.sqlite3')

# Verbindung zur SQLite-Datenbank herstellen
def connect_db():
    try:
        conn = sqlite3.connect(db_path)
        print("Verbindung zur Datenbank erfolgreich!")
        return conn
    except sqlite3.Error as e:
        print(f"Fehler beim Verbinden mit der Datenbank: {e}")
        return None

# Alle Daten aus der dht22_metric Tabelle auslesen
def read_all_data():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            # Alle Daten aus der Tabelle dht22_metric abfragen
            cursor.execute("SELECT * FROM dht22_metric")
            rows = cursor.fetchall()
            
            if rows:
                print(f"Es wurden {len(rows)} Datensätze gefunden.")
                for row in rows:
                    print(row)
            else:
                print("Keine Daten gefunden!")

        except sqlite3.Error as e:
            print(f"Fehler bei der Abfrage der Daten: {e}")
        finally:
            conn.close()

# Hauptfunktion ausführen
if __name__ == "__main__":
    read_all_data()