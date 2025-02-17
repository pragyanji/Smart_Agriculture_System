from django.db import models

# Create your models here.
class SensorData(models.Model):
    moisture = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    fire_alert = models.BooleanField(default=False)
    cattle_alert = models.BooleanField(default=False)
    pump_status = models.BooleanField(default=False)
    led_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Moisture: {self.moisture}, Fire: {self.fire_alert}, Cattle: {self.cattle_alert}"