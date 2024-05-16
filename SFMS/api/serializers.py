from rest_framework import serializers
from .recommendations import recommend_for_crop
from .models import SensorData
from .models import WeatherData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = [
                    'sensor_data_id',
                    'air_humidity',
                    'air_temperature',
                    'soil_temperature',
                    'flux',
                    'rain_drop',
                    'ph_value',
                    'nitrogen',
                    'phosphorus',
                    'potassium', 
                    'recommendations', 
                    'timestamp'     ]
  
        
    # def create(self, data):
    #     return SensorData.objects.create(**data)

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = [
                  'rainfall',
                  'temperature',
                  'humidity',
                  'wind_speed'
                  'timestamp'
                  ]