from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import SensorData
from .serializers import SensorDataSerializer
import requests  # For OpenWeather API calls
from .models import WeatherData
from .recommendations import recommend_for_crop
# from django.http import JsonResponse

# Replace with your OpenWeather API key






# class SensorDataView(APIView):
#     # @api_view(['POST'])
#     def post(self, request):
#         # Receive data from GSM module
#         serializer = SensorDataSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = serializer.data
#             recommendations = recommend_for_crop(data)
#             combined_data = {**data, **recommendations}
#             # return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(combined_data.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SensorDataView(APIView):
    # @api_view(['POST'])
    def post(self, request):
        # Receive data from GSM module
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            recommendations = recommend_for_crop(data)
            data['recommendations'] = recommendations
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


    # @api_view(['GET'])
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
            # return JsonResponse({
            #     "Data": sensor_data
            # })
    # def put(self, request, pk=None):
    #     if pk:
    #         try:
    #             sensor_data = SensorData.objects.get(pk=pk)
    #             serializer = SensorDataSerializer(sensor_data, data=request.data)
    #             if serializer.is_valid():
    #                 serializer.save()
    #                 return Response(serializer.data)
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #         except SensorData.DoesNotExist:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # def delete(self, request, pk=None):
    #     if pk:
    #         try:
    #             sensor_data = SensorData.objects.get(pk=pk)
    #             sensor_data.delete()
    #             return Response(status=status.HTTP_204_NO_CONTENT)
    #         except SensorData.DoesNotExist:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)





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