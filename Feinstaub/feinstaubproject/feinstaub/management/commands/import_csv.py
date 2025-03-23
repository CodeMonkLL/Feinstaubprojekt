from django.core.management.base import BaseCommand
import os
import csv
import gzip
import requests
import calendar
from datetime import datetime
from django.db import IntegrityError
from feinstaub.models import DHT22Metric

class Command(BaseCommand):  
    help = "Download and import DHT22 sensor data from archive.sensor.community"

    def handle(self, *args, **options):
        year = 2022
        sensor_name = "dht22_sensor_3660"
        save_dir = "data"

        os.makedirs(save_dir, exist_ok=True)

        for month in range(1, 13):
            days_in_month = calendar.monthrange(year, month)[1]

            for day in range(1, days_in_month + 1):
                date_str = f"{year}-{month:02d}-{day:02d}"
                url = f"https://archive.sensor.community/{year}/{date_str}/{date_str}_{sensor_name}.csv.gz"
                local_gz_path = os.path.join(save_dir, f"{date_str}_{sensor_name}.csv.gz")
                local_csv_path = local_gz_path[:-3]

                try:
                    response = requests.get(url, stream=True)
                    if response.status_code == 200:
                        with open(local_gz_path, 'wb') as f:
                            f.write(response.content)
                        self.stdout.write(self.style.SUCCESS(f"✅ Downloaded: {url}"))

                        with gzip.open(local_gz_path, 'rt', encoding='utf-8') as gz_file:
                            with open(local_csv_path, 'w', encoding='utf-8') as csv_out:
                                csv_out.write(gz_file.read())

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
                                    self.stdout.write(self.style.WARNING(f"⚠️ Skiped: {e}"))

                        os.remove(local_gz_path)
                        os.remove(local_csv_path)
                        self.stdout.write(self.style.SUCCESS(f"🗑️ Delete temporary files: {local_gz_path}, {local_csv_path}"))

                    else:
                        self.stdout.write(self.style.ERROR(f"❌  Can't downloaded: {url} (Code {response.status_code})"))

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"❌ Error {url}: {e}"))
