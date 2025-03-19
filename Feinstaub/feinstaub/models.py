from django.db import models;

class SDS011Metric(models.Model):
    id = models.AutoField(primary_key=True)  # Automatische Primärschlüssel-ID
    sensor_id = models.IntegerField()  # ID des Sensors
    sensor_type = models.CharField(max_length=50)  # Typ des Sensors (SDS011)
    location = models.CharField(max_length=255, blank=True, null=True)  # Optionaler Standortname
    lat = models.FloatField()  # Breitengrad
    lon = models.FloatField()  # Längengrad
    timestamp = models.DateTimeField(auto_now_add=True)  # Zeitstempel der Messung

    # Feinstaubwerte
    P1 = models.FloatField()  # Feinstaub PM10
    durP1 = models.FloatField()  # Dauer PM10
    ratioP1 = models.FloatField()  # Verhältnis PM10
    P2 = models.FloatField()  # Feinstaub PM2.5
    durP2 = models.FloatField()  # Dauer PM2.5
    ratioP2 = models.FloatField()  # Verhältnis PM2.5

    class Meta:
        db_table = "sds011_metric"  # Setzt den Tabellennamen explizit auf 'sds011_metric'
    
    def __str__(self):
        return f"SDS011 Sensor {self.sensor_id} - {self.timestamp}"
    

class DHT22Metric(models.Model):
    id = models.AutoField(primary_key=True)  # Automatische Primärschlüssel-ID
    sensor_id = models.IntegerField()  # ID des Sensors
    sensor_type = models.CharField(max_length=50)  # Typ des Sensors (DHT22)
    location = models.CharField(max_length=255, blank=True, null=True)  # Optionaler Standortname
    lan = models.FloatField()  # Breitengrad
    lon = models.FloatField()  # Längengrad
    timestamp = models.DateTimeField(auto_now_add=True)  # Zeitstempel der Messung
    temperature = models.FloatField()  # Temperatur
    humidity = models.FloatField()  # Luftfeuchtigkeit

    class Meta:
        db_table = "dht22_metric"
    
    def __str__(self):
        return f"DHT22 Sensor {self.sensor_id} - {self.timestamp}"