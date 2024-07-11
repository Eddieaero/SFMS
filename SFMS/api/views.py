from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import SensorDataSerializer
import requests  
from .recommendations import recommend_for_crop
# from django.http import JsonResponse
import json
# Replace with your OpenWeather API key


class SensorDataView(APIView):
    def post(self, request):
        # Receive data from GSM module
        data = request.data.copy()
        recommendations = recommend_for_crop(data)
        data['recommendations'] = json.dumps(recommendations)
        serializer = SensorDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        if pk:
            # Get specific sensor data by ID
            try:
                sensor_data = SensorData.objects.get(pk=pk)
                serializer = SensorDataSerializer(sensor_data)
                return Response(serializer.data)
            except SensorData.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            # Get all sensor data
            sensor_data = SensorData.objects.all()
            serializer = SensorDataSerializer(sensor_data, many=True)
            return Response(serializer.data)

class WeatherDataView(APIView):
    def get(self, request):
        # Get weather data from OpenWeather API
        lat = request.GET.get('latitude')  # Get latitude from query parameter
        lon = request.GET.get('longitude')  # Get longitude from query parameter
        if not lat or not lon:
            return Response({'error': 'Missing latitude or longitude parameters'}, status=status.HTTP_400_BAD_REQUEST)
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()

            # Extract relevant weather information (rain, wind, temperature, pressure)
            rainfall = weather_data["rain"]["1h"]
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            # Create a new WeatherData instance and save it to the database
            weather_instance = WeatherData(
                rainfall=rainfall,
                temperature=temperature,
                humidity=humidity,
                wind_speed=wind_speed,
            )
            weather_instance.save()

            # Return the saved instance data
            return Response({
                'rainfall': rainfall,
                'temperature': temperature,
                'humidity': humidity,
                'wind_speed': wind_speed,
                'timestamp': weather_instance.timestamp,
            }, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'Failed to retrieve weather data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)