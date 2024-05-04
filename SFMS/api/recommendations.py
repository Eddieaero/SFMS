





def recommend_for_crop(data):
    recommendations = {}

    ph_value = float(data['ph_value'])
    if ph_value < 5.8:
        recommendations['ph_value_rec'] = 'Soil is too acidic for maize. Consider using lime to increase pH.'
    elif ph_value > 7.0:
        recommendations['ph_value_rec'] = 'Soil is too alkaline for maize. Consider using sulfur or acidifying fertilizers to decrease pH.'
    else:
        recommendations['ph_value_rec'] = 'Soil pH is optimal for maize. Maintain current practices.'


    nitrogen = float(data['nitrogen'])
    phosphorus = float(data['phosphorus'])
    potassium = float(data['potassium'])
    # Assuming 1-20 scale for NPK values
    if nitrogen < 10:
        recommendations['nitrogen_rec'] = 'Soil has low nitrogen for maize. Consider using a nitrogen-rich fertilizer.'
    elif nitrogen > 15:
        recommendations['nitrogen_rec'] = 'Soil has high nitrogen for maize. Consider reducing nitrogen fertilizer.'
    else:
        recommendations['nitrogen_rec'] = 'Soil nitrogen level is optimal for maize. Maintain current practices.'

    if phosphorus < 10:
        recommendations['phosphorus_rec'] = 'Soil has low phosphorus for maize. Consider using a phosphorus-rich fertilizer.'
    elif phosphorus > 15:
        recommendations['phosphorus_rec'] = 'Soil has high phosphorus for maize. Consider reducing phosphorus fertilizer.'
    else:
        recommendations['phosphorus_rec'] = 'Soil phosphorus level is optimal for maize. Maintain current practices.'

    if potassium < 10:
        recommendations['potassium_rec'] = 'Soil has low potassium for maize. Consider using a potassium-rich fertilizer.'
    elif potassium > 15:
        recommendations['potassium_rec'] = 'Soil has high potassium for maize. Consider reducing potassium fertilizer.'
    else:
        recommendations['potassium_rec'] = 'Soil potassium level is optimal for maize. Maintain current practices.'

    soil_temperature = float(data['soil_temperature'])
    if soil_temperature < 10:
        recommendations['soil_temperature_rec'] = 'Soil is too cold for maize. Consider using plastic mulch to increase soil temperature.'
    elif soil_temperature > 30:
        recommendations['soil_temperature_rec'] = 'Soil is too hot for maize. Consider using shade cloth to decrease soil temperature.'
    else:
        recommendations['soil_temperature_rec'] = 'Soil temperature is optimal for maize. Maintain current practices.'

    air_temperature = float(data['air_temperature'])
    if air_temperature < 10:
        recommendations['air_temperature_rec'] = 'Air is too cold for maize. Consider using a greenhouse or row covers to increase air temperature.'
    elif air_temperature > 30:
        recommendations['air_temperature_rec'] ='Air is too hot for maize. Consider using shade cloth to decrease air temperature.'
    else:
        recommendations['air_temperature_rec'] ='Air temperature is optimal for maize. Maintain current practices.'

    air_humidity = float(data['air_humidity'])
    # Assuming 1-10 scale for air humidity
    if air_humidity < 4:
        recommendations['air_humidity_rec'] = 'Air is too dry for maize. Consider using a humidifier or misting to increase air humidity.'
    elif air_humidity > 7:
        recommendations['air_humidity_rec'] = 'Air is too humid for maize. Consider improving ventilation.'
    else:
        recommendations['air_humidity_rec'] = 'Air humidity is optimal for maize. Maintain current practices.'

    return recommendations