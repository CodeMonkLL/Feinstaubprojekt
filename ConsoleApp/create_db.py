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
        CREATE TABLE dht22_metric (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id INTEGER NOT NULL,
            sensor_type TEXT NOT NULL,
            location TEXT,
            lat FLOAT,
            lon FLOAT,
            timestamp TEXT,
            temperature FLOAT NOT NULL,
            humidity FLOAT NOT NULL
        );
        ''')

        # Erstellen der sds011_metric Tabelle
        cursor.execute('''
        CREATE TABLE sds011_metric (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id INTEGER NOT NULL,
            sensor_type TEXT NOT NULL,
            location TEXT,
            lat FLOAT,
            lon FLOAT,
            timestamp TEXT,
            P1 FLOAT NOT NULL,
            durP1 FLOAT,
            ratioP1 FLOAT,
            P2 FLOAT NOT NULL,
            durP2 FLOAT,
            ratioP2 FLOAT
        );
        ''')

        # Änderungen speichern
        conn.commit()
        print("Tabellen erfolgreich erstellt.")
        conn.close()

# Hauptfunktion ausführen
if __name__ == "__main__":
    create_tables()