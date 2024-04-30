from api.views import SensorDataView
from api.views import WeatherDataView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('SensorData/', SensorDataView.as_view())
    # path('SensorData/', SensorDataView.as_view())
    path('sensorData/', SensorDataView.as_view(), name='sensor-data'),
    path('weatherData/', WeatherDataView.as_view(), name='weather-data'),
    path('sensorData/<int:pk>/', SensorDataView.as_view(), name='sensor-data-detail'),
    path('weatherData/<int:pk>/', WeatherDataView.as_view(), name='weather-data-detail')
]
