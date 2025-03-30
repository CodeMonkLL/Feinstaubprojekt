import os
import requests
import calendar

# Definiert den Pfad zum Download-Ordner im Projekt
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Hauptprojektordner
download_dir = os.path.join(project_dir, 'downloads')  # Pfad zum Download-Ordner

# Sicherstellen, dass der Ordner existiert
os.makedirs(download_dir, exist_ok=True)

def download_data(year, month, sensor_name, save_dir):
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

# Beispielaufruf der Funktion
download_data(2022, 1, "dht22_sensor_3660", download_dir)