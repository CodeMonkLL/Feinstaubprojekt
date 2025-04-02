import sqlite3

# Datenbank-Pfad (wird automatisch erstellt, wenn sie noch nicht existiert)
db_path = 'feinstaub.db'

# Verbindung zur Datenbank herstellen
def connect_db():
    try:
        conn = sqlite3.connect(db_path)
        print("Verbindung zur Datenbank erfolgreich!")
        return conn
    except sqlite3.Error as e:
        print(f"Fehler beim Verbinden mit der Datenbank: {e}")
        return None

# Tabellen erstellen (für DHT22 und SDS011)
def create_tables():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()

        # Erstellen der dht22_metric Tabelle
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS dht22_metric (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id INTEGER NOT NULL,
            sensor_type TEXT NOT NULL,
            location TEXT,
            lat REAL NOT NULL,
            lon REAL NOT NULL,
            timestamp TEXT NOT NULL,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL
        );
        ''')

        # Erstellen der sds011_metric Tabelle
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sds011_metric (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id INTEGER NOT NULL,
            sensor_type TEXT NOT NULL,
            location TEXT,
            lat REAL NOT NULL,
            lon REAL NOT NULL,
            timestamp TEXT NOT NULL,
            P1 REAL NOT NULL,
            durP1 REAL NOT NULL,
            ratioP1 REAL NOT NULL,
            P2 REAL NOT NULL,
            durP2 REAL NOT NULL,
            ratioP2 REAL NOT NULL
        );
        ''')

        # Änderungen speichern
        conn.commit()
        print("Tabellen erfolgreich erstellt.")
        conn.close()

# Hauptfunktion ausführen
if __name__ == "__main__":
    create_tables()