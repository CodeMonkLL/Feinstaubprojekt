import sqlite3
import os
from datetime import datetime

def connect_db():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'feinstaub.db')
    return sqlite3.connect(db_path)

def get_sds011_values(date_str):
    conn = connect_db()
    cursor = conn.cursor()

    # Datum konvertieren und Zeitbereich festlegen
    date = datetime.strptime(date_str, "%Y-%m-%d")
    start_timestamp = date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_timestamp = date.replace(hour=23, minute=59, second=59, microsecond=999999)

    # SQL-Abfrage für SDS011-Werte, einschließlich P1, P2, durP1, ratioP1, durP2, ratioP2
    cursor.execute('''
        SELECT
            MAX(P1), MIN(P1), AVG(P1),
            MAX(P2), MIN(P2), AVG(P2),
            MAX(durP1), MIN(durP1), AVG(durP1),
            MAX(ratioP1), MIN(ratioP1), AVG(ratioP1),
            MAX(durP2), MIN(durP2), AVG(durP2),
            MAX(ratioP2), MIN(ratioP2), AVG(ratioP2)
        FROM sds011_metric
        WHERE timestamp BETWEEN ? AND ?
    ''', (start_timestamp, end_timestamp))

    result = cursor.fetchone()
    conn.close()

    # Ergebnisse ausgeben
    if result:
        print(f"Max P1: {result[0]}, Min P1: {result[1]}, Avg P1: {result[2]}")
        print(f"Max P2: {result[3]}, Min P2: {result[4]}, Avg P2: {result[5]}")
        print(f"Max durP1: {result[6]}, Min durP1: {result[7]}, Avg durP1: {result[8]}")
        print(f"Max ratioP1: {result[9]}, Min ratioP1: {result[10]}, Avg ratioP1: {result[11]}")
        print(f"Max durP2: {result[12]}, Min durP2: {result[13]}, Avg durP2: {result[14]}")
        print(f"Max ratioP2: {result[15]}, Min ratioP2: {result[16]}, Avg ratioP2: {result[17]}")
    else:
        print("Keine Daten für dieses Datum gefunden.")

if __name__ == "__main__":
    date = input("Geben Sie das Datum im Format YYYY-MM-DD ein: ")
    get_sds011_values(date)