import os
import csv
import gzip
import requests
import calendar
from datetime import datetime
from django.db import IntegrityError
from feinstaub.models import DHT22Metric

year = 2022
sensor_name = "dht22_sensor_3660"
save_dir = "data"  # Catalog for saving files

# Check if the directory exists
os.makedirs(save_dir, exist_ok=True)

for month in range(1, 13):  # Go through the months
    days_in_month = calendar.monthrange(year, month)[1]  # Get the number of days in the month

    for day in range(1, days_in_month + 1):  # Go through the days
        date_str = f"{year}-{month:02d}-{day:02d}"  # YYYY-MM-DD
        url = f"https://archive.sensor.community/{year}/{date_str}/{date_str}_{sensor_name}.csv.gz"
        local_gz_path = os.path.join(save_dir, f"{date_str}_{sensor_name}.csv.gz")
        local_csv_path = local_gz_path[:-3]  # Delete ".gz" from the file name

        try:
            # 1. Download the .gz file
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(local_gz_path, 'wb') as f:
                    f.write(response.content)
                print(f"✅ Downloaded: {url}")

                # 2. Unpack the .gz file
                with gzip.open(local_gz_path, 'rt', encoding='utf-8') as gz_file:
                    with open(local_csv_path, 'w', encoding='utf-8') as csv_out:
                        csv_out.write(gz_file.read())

                # 3. Read the .csv file and save the data to the database
                with open(local_csv_path, 'r', encoding='utf-8') as file:
                    csv_reader = csv.DictReader(file)
                    for row in csv_reader:
                        try:
                            metric = DHT22Metric(
                                sensor_id=int(row['sensor_id']),
                                sensor_type=row.get('sensor_type', 'DHT22'),
                                location=row.get('location', ''),  
                                lan=float(row['lat']),  
                                lon=float(row['lon']),
                                timestamp=datetime.strptime(row['timestamp'], "%Y-%m-%dT%H:%M:%S"),  
                                temperature=float(row['temperature']),
                                humidity=float(row['humidity'])
                            )
                            metric.save()
                        except (ValueError, IntegrityError) as e:
                            print(f"⚠️ Missing line due to an error: {e}")

                # 4. Delete temporary files
                os.remove(local_gz_path)
                os.remove(local_csv_path)
                print(f" Temporary Files deleted: {local_gz_path}, {local_csv_path}")

            else:
                print(f"❌ Could not download: {url} (Code {response.status_code})")

        except Exception as e:
            print(f"❌ Processing error {url}: {e}")