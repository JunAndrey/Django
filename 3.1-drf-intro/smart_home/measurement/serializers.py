from rest_framework import serializers
from .models import Sensor, Measurements


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = "__all__"


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description', 'measurements')

