import sqlite3
import os

def connect_db():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'feinstaub.db')
    return sqlite3.connect(db_path)

def list_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print("Tabellen in der Datenbank:")
    for table in tables:
        print(table[0])

    conn.close()

list_tables()


def print_table_data(table_name):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    print(f"\nDaten aus der Tabelle {table_name}:")
    for row in rows:
        print(row)

    conn.close()


# Daten aus dht22_metric anzeigen
print_table_data('dht22_metric')

# Daten aus sds011_metric anzeigen
print_table_data('sds011_metric')