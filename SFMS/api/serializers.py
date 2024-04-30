from rest_framework import serializers
from .models import SensorData
from .models import WeatherData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = [
                  'sensor_data_id',
                  'ph_value',
                  'soil_moisture', 
                  'npk_value', 
                  'soil_temperature', 
                  'timestamp']
        
    # def create(self, data):
    #     return SensorData.objects.create(**data)

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = [
                  'rainfall',
                  'temperature',
                  'humidity',
                  'wind_speed']