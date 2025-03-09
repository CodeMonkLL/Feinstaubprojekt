import requests
import gzip
import shutil

# Richtige URL mit Dateinamen
gz_datei = "2022-01-01_dht22_sensor_3660.csv.gz"
gz_url = f"https://archive.sensor.community/2022/2022-01-01/{gz_datei}"

# GZ-Datei herunterladen
response = requests.get(gz_url, stream=True)

# Überprüfen, ob der Download erfolgreich war (Statuscode 200)
if response.status_code == 200:
    with open(gz_datei, "wb") as file:
        file.write(response.content)
    print("GZ-Datei erfolgreich heruntergeladen!")

    # GZ-Datei entpacken
    entpackte_datei = "data.csv"
    with gzip.open(gz_datei, "rb") as f_in:
        with open(entpackte_datei, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

    print("GZ-Datei entpackt!")
else:
    print(f"Fehler beim Herunterladen: {response.status_code} - {response.reason}")
