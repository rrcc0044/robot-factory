from django.db import models


class Shipment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
