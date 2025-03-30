import sqlite3
import csv
import os
from datetime import datetime

def connect_db():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'feinstaub.db')
    return sqlite3.connect(db_path)

def write_csv_to_db(csv_file_path, table_name):
    # Verbindung zur Datenbank herstellen
    conn = connect_db()
    cursor = conn.cursor()

    # CSV-Datei lesen und in die Datenbank einfügen
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        
        for row in csv_reader:
            try:
                if table_name == 'dht22_metric':
                    # Daten aus der CSV für DHT22 extrahieren
                    sensor_id = int(row['sensor_id'])
                    sensor_type = row.get('sensor_type', 'DHT22')  # Standardwert setzen
                    location = row.get('location', '')
                    lat = float(row['lat'])
                    lon = float(row['lon'])
                    timestamp = datetime.strptime(row['timestamp'], "%Y-%m-%dT%H:%M:%S")
                    temperature = float(row['temperature'])
                    humidity = float(row['humidity'])

                    # SQL-Insert-Statement für DHT22
                    cursor.execute('''
                        INSERT INTO dht22_metric (sensor_id, sensor_type, location, lat, lon, timestamp, temperature, humidity)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (sensor_id, sensor_type, location, lat, lon, timestamp, temperature, humidity))

                elif table_name == 'sds011_metric':
                    # Daten aus der CSV für SDS011 extrahieren
                    sensor_id = int(row['sensor_id'])
                    sensor_type = row.get('sensor_type', 'SDS011')  # Standardwert setzen
                    location = row.get('location', '')
                    lat = float(row['lat'])
                    lon = float(row['lon'])
                    timestamp = datetime.strptime(row['timestamp'], "%Y-%m-%dT%H:%M:%S")
                    P1 = float(row['P1'])
                    durP1 = float(row['durP1'])
                    ratioP1 = float(row['ratioP1'])
                    P2 = float(row['P2'])
                    durP2 = float(row['durP2'])
                    ratioP2 = float(row['ratioP2'])

                    # SQL-Insert-Statement für SDS011
                    cursor.execute('''
                        INSERT INTO sds011_metric (sensor_id, sensor_type, location, lat, lon, timestamp, P1, durP1, ratioP1, P2, durP2, ratioP2)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (sensor_id, sensor_type, location, lat, lon, timestamp, P1, durP1, ratioP1, P2, durP2, ratioP2))

                conn.commit()
                print(f"✅ Saved: {sensor_id} at {timestamp}")
            except (ValueError, sqlite3.IntegrityError) as e:
                print(f"⚠️ Skipped: {e}")
    
    # Verbindung schließen
    conn.close()

# Funktion zum Durchlaufen des Ordners und Verarbeiten der CSV-Dateien
def process_all_csv_in_directory(downloads_folder):
    # Alle Dateien im Ordner durchsuchen
    for filename in os.listdir(downloads_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(downloads_folder, filename)
            print(f"Verarbeite {filename}")

            # CSV-Datei öffnen und die Spalten überprüfen
            with open(file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file, delimiter=';')
                fieldnames = csv_reader.fieldnames

                # Überprüfen, ob die CSV-Datei die Spalten für dht22_metric enthält
                if all(col in fieldnames for col in ['sensor_id', 'sensor_type', 'location', 'lat', 'lon', 'timestamp', 'temperature', 'humidity']):
                    write_csv_to_db(file_path, 'dht22_metric')
                # Überprüfen, ob die CSV-Datei die Spalten für sds011_metric enthält
                elif all(col in fieldnames for col in ['sensor_id', 'sensor_type', 'location', 'lat', 'lon', 'timestamp', 'P1', 'durP1', 'ratioP1', 'P2', 'durP2', 'ratioP2']):
                    write_csv_to_db(file_path, 'sds011_metric')
                else:
                    print(f"⚠️ Unbekannte Spaltenstruktur in {filename}. Diese Datei wird übersprungen.")

# Hauptfunktion ausführen
if __name__ == "__main__":
    # Ordnerpfad angeben, in dem die CSV-Dateien liegen
    downloads_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'downloads')
    
    # Alle CSV-Dateien im Ordner verarbeiten
    process_all_csv_in_directory(downloads_folder)
