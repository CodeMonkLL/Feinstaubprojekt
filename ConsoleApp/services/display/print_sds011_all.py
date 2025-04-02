import sqlite3
import os
from datetime import datetime

def connect_db():
    # Berechnet den Pfad zur feinstaub.db relativ zum Ordner, in dem das Skript ausgeführt wird (services/).
    project_dir = os.path.dirname(os.path.abspath(__file__))  # Der Ordner, in dem das Skript liegt (services)
    db_path = os.path.join(project_dir, '..', '..', 'feinstaub.db')  # Geht einen Ordner zurück und dann in den ConsoleApp-Ordner
    return sqlite3.connect(db_path)

def read_all_sds011_data():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sds011_metric")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)  # Alle Daten in der Konsole anzeigen
    else:
        print("Keine Daten gefunden.")

    conn.close()

if __name__ == "__main__":
    read_all_sds011_data()
