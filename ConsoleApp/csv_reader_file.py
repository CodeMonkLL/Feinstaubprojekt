# import sqlite3
# import os
# import csv
# import datetime
# import requests
# # CREATE TABLE dht22_metric (
# #     id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     sensor_id INTEGER NOT NULL,
# #     sensor_type VARCHAR(50) NOT NULL,
# #     location VARCHAR(255),
# #     lat FLOAT NOT NULL,
# #     lon FLOAT NOT NULL,
# #     timestamp DATETIME NOT NULL,
# #     temperature FLOAT NOT NULL,
# #     humidity FLOAT NOT NULL
# # );


# # CREATE TABLE sds011_metric (
# #     id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     sensor_id INTEGER NOT NULL,
# #     sensor_type VARCHAR(50) NOT NULL,
# #     location VARCHAR(255),
# #     lat FLOAT NOT NULL,
# #     lon FLOAT NOT NULL,
# #     timestamp DATETIME NOT NULL,
# #     P1 FLOAT NOT NULL,
# #     durP1 FLOAT NOT NULL,
# #     ratioP1 FLOAT NOT NULL,
# #     P2 FLOAT NOT NULL,
# #     durP2 FLOAT NOT NULL,
# #     ratioP2 FLOAT NOT NULL
# # );


# ### Im folgenden werden die Paths zur Datenbank, zum Ordner der abgespeicherten CSVs und der zu connectenden Website definiert

# # Verbindet sich mit der SQliteDB im anderen Projektordner
# db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Feinstaub', 'feinstaubproject', 'db.sqlite3')
# # Speichertort im Django Ordner für die CSV Dateien
# save_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Feinstaub', 'feinstaubproject', 'data')

# os.makedirs(save_dir, exist_ok=True)

# # Der vollständige Pfad zur CSV-Datei
# save_path = os.path.join(save_dir, "downloaded_data.csv.gz")

# connect = sqlite3.connect(db_path)
# cursor = connect.cursor()



# #URL zum Herunterladen der Dateien
# year = 2022
# month = 1
# sensor_name = "dht22_sensor_3660"
# url = f"https://archive.sensor.community/{year}/{month:02d}/{year}-{month:02d}-01_{sensor_name}.csv.gz"

# # Prüfen, ob der Download erfolgreich war
# response = requests.get(url)

# if response.status_code == 200:
#     with open(save_path, 'wb') as f:
#         f.write(response.content)
#     print(f"CSV-Datei erfolgreich heruntergeladen: {save_path}")
# else:
#     print(f"Fehler beim Herunterladen der Datei: {response.status_code}")


import os
import requests
import calendar
import gzip

# Definiert den Pfad zum Ordner, in dem die CSV-Dateien gespeichert werden
save_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Feinstaub', 'feinstaubproject', 'data')

# Stellt sicher, dass der Ordner existiert
os.makedirs(save_dir, exist_ok=True)

# Funktion zum Herunterladen der CSV-Dateien
def download_data(year, month, sensor_name):
    # Anzahl der Tage im angegebenen Monat
    days_in_month = calendar.monthrange(year, month)[1]

    # Alle Dateien für den Monat herunterladen und speichern
    for day in range(1, days_in_month + 1):
        date_str = f"{year}-{month:02d}-{day:02d}"
        url = f"https://archive.sensor.community/{year}/{date_str}/{date_str}_{sensor_name}.csv.gz"
        local_gz_path = os.path.join(save_dir, f"{date_str}_{sensor_name}.csv.gz")

        try:
            # Lade die Datei herunter, wenn sie existiert
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(local_gz_path, 'wb') as f:
                    f.write(response.content)
                print(f"✅ Downloaded: {url}")
            else:
                print(f"❌ Couldn't download: {url} (Code {response.status_code})")

        except Exception as e:
            print(f"❌ Error downloading {url}: {e}")

def unzip_gz_to_csv():
    # Durchlaufe alle .gz-Dateien im save_dir und entpacke sie
    for filename in os.listdir(save_dir):
        if filename.endswith('.csv.gz'):
            gz_file_path = os.path.join(save_dir, filename)
            csv_file_path = os.path.join(save_dir, filename[:-3])  # Entfernt das .gz und erhält den Dateinamen

            try:
                # Entpacke die gz-Datei und speichere sie als .csv
                with gzip.open(gz_file_path, 'rt', encoding='utf-8') as gz_file:
                    with open(csv_file_path, 'w', encoding='utf-8') as csv_file:
                        shutil.copyfileobj(gz_file, csv_file)
                print(f"✅ Successfully converted {gz_file_path} to {csv_file_path}")
            except Exception as e:
                print(f"❌ Error converting {gz_file_path} to {csv_file_path}: {e}")