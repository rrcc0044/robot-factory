from rest_framework import serializers

from .models import Shipment


class CreateShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'
