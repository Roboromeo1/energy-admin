from django.db import models

class PQCurve(models.Model):
    voltage = models.FloatField()
    capacity = models.FloatField()
    pf_droop = models.FloatField()