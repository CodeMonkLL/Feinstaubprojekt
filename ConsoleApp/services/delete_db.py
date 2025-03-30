import sqlite3
import os

# Verbindung zur SQLite-Datenbank herstellen
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'feinstaub.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Tabelle(n) löschen (dht22_metric als Beispiel)
cursor.execute("DELETE FROM dht22_metric")  # Alle Daten in der dht22_metric-Tabelle löschen
cursor.execute("DELETE FROM sds011_metric")

# cursor.execute("DELETE FROM another_table")

# Änderungen speichern
conn.commit()

# Verbindung schließen
conn.close()
