from rest_framework import serializers

from .models import Robot


class RobotSerializer(serializers.ModelSerializer):

    status = serializers.StringRelatedField(many=True)

    class Meta:
        model = Robot
        fields = ('id', 'name', 'configuration', 'status', 'qa_status')
