from rest_framework import serializers

from .models import Shipment
from robot_factory.robots.models import Robot


class CreateShipmentSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        return {
            'shipRobots': Robot.objects.filter(pk__in=data.get('shipRobots'))
        }

    def validate(self, data):
        for robot in data.get('shipRobots'):
            if not robot.qa_status:
                raise serializers.ValidationError('not ready for Shipment')

        return data

    def create(self, validated_data):
        shipment = Shipment.objects.create()
        validated_data['shipRobots'].update(shipment=shipment)

        return shipment

    class Meta:
        model = Shipment
        fields = '__all__'
