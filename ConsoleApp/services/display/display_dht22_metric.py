import sqlite3
from datetime import datetime
import os

def connect_db():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'feinstaub.db')
    return sqlite3.connect(db_path)

def get_stats_for_date(date_str, value_type):
    # Konvertiere das Datum in das passende Format für SQL-Abfragen
    date = datetime.strptime(date_str, "%Y-%m-%d").date()

    # Bestimme die Spalte basierend auf dem Wertetyp
    if value_type == 'temperature':
        value_column = 'temperature'
    elif value_type == 'humidity':
        value_column = 'humidity'
    else:
        print("Ungültiger Wertetyp. Gültige Optionen: 'temperature', 'humidity'.")
        return

    # Verbindung zur Datenbank herstellen
    conn = connect_db()
    cursor = conn.cursor()

    # SQL-Abfrage, um die höchsten, niedrigsten und durchschnittlichen Werte für den angegebenen Tag zu erhalten
    cursor.execute(f'''
        SELECT MAX({value_column}), MIN({value_column}), AVG({value_column})
        FROM dht22_metric
        WHERE DATE(timestamp) = ?
    ''', (date,))

    result = cursor.fetchone()

    if result[0] is None:
        print(f"Keine Daten für den {date_str} gefunden.")
    else:
        print(f"Statistiken für den {date_str} ({value_type}):")
        print(f"Höchster Wert: {result[0]}")
        print(f"Niedrigster Wert: {result[1]}")
        print(f"Durchschnittlicher Wert: {result[2]:.2f}")

    # Verbindung schließen
    conn.close()

# Hauptfunktion ausführen
if __name__ == "__main__":
    date_input = input("Gib das Datum im Format YYYY-MM-DD ein: ")
    value_type_input = input("Gib den Wertetyp ein (temperature, humidity): ")
    
    get_stats_for_date(date_input, value_type_input)
