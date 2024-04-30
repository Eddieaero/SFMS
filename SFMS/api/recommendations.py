





def recommend_for_crop(data):
    recommendations = []

    ph_value = float(data['ph_value'])
    if ph_value < 5.8:
        recommendations.append('Soil is too acidic for maize. Consider using lime to increase pH.')
    elif ph_value > 7.0:
        recommendations.append('Soil is too alkaline for maize. Consider using sulfur or acidifying fertilizers to decrease pH.')
    else:
        recommendations.append('Soil pH is optimal for maize. Maintain current practices.')

    nitrogen = float(data['nitrogen'])
    phosphorus = float(data['phosphorus'])
    potassium = float(data['potassium'])
    # Assuming 1-20 scale for NPK values
    if nitrogen < 10:
        recommendations.append('Soil has low nitrogen for maize. Consider using a nitrogen-rich fertilizer.')
    elif nitrogen > 15:
        recommendations.append('Soil has high nitrogen for maize. Consider reducing nitrogen fertilizer.')
    else:
        recommendations.append('Soil nitrogen level is optimal for maize. Maintain current practices.')

    # Similar checks for phosphorus and potassium...

    soil_temperature = float(data['soil_temperature'])
    if soil_temperature < 10:
        recommendations.append('Soil is too cold for maize. Consider using plastic mulch to increase soil temperature.')
    elif soil_temperature > 30:
        recommendations.append('Soil is too hot for maize. Consider using shade cloth to decrease soil temperature.')
    else:
        recommendations.append('Soil temperature is optimal for maize. Maintain current practices.')

    air_temperature = float(data['air_temperature'])
    if air_temperature < 10:
        recommendations.append('Air is too cold for maize. Consider using a greenhouse or row covers to increase air temperature.')
    elif air_temperature > 30:
        recommendations.append('Air is too hot for maize. Consider using shade cloth to decrease air temperature.')
    else:
        recommendations.append('Air temperature is optimal for maize. Maintain current practices.')

    air_humidity = float(data['air_humidity'])
    # Assuming 1-10 scale for air humidity
    if air_humidity < 4:
        recommendations.append('Air is too dry for maize. Consider using a humidifier or misting to increase air humidity.')
    elif air_humidity > 7:
        recommendations.append('Air is too humid for maize. Consider improving ventilation.')
    else:
        recommendations.append('Air humidity is optimal for maize. Maintain current practices.')

    return recommendations