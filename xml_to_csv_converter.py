import xml.etree.ElementTree as ET
import csv

# Parse the XML file
tree = ET.parse('/content/drive/MyDrive/Data for analysis/data_aqi_cpcb.xml')
root = tree.getroot()

# Prepare the CSV file
output_csv = '/content/drive/MyDrive/Data for analysis/aqi_data.csv'
headers = [
    "Country", "State", "City", "Station", "Latitude", "Longitude", "LastUpdate",
    "PM2.5_Min", "PM2.5_Max", "PM2.5_Avg",
    "PM10_Min", "PM10_Max", "PM10_Avg",
    "NO2_Min", "NO2_Max", "NO2_Avg",
    "SO2_Min", "SO2_Max", "SO2_Avg",
    "CO_Min", "CO_Max", "CO_Avg",
    "OZONE_Min", "OZONE_Max", "OZONE_Avg",
    "NH3_Min", "NH3_Max", "NH3_Avg",
    "Air_Quality_Index_Value", "Predominant_Parameter"
]

# Write the data to CSV
with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for country in root.findall('Country'):
        country_name = country.get('id')
        for state in country.findall('State'):
            state_name = state.get('id')
            for city in state.findall('City'):
                city_name = city.get('id')
                for station in city.findall('Station'):
                    station_name = station.get('id')
                    latitude = station.get('latitude')
                    longitude = station.get('longitude')
                    last_update = station.get('lastupdate')

                    # Initialize pollutant data
                    pollutants = {
                        "PM2.5": {"Min": "NA", "Max": "NA", "Avg": "NA"},
                        "PM10": {"Min": "NA", "Max": "NA", "Avg": "NA"},
                        "NO2": {"Min": "NA", "Max": "NA", "Avg": "NA"},
                        "SO2": {"Min": "NA", "Max": "NA", "Avg": "NA"},
                        "CO": {"Min": "NA", "Max": "NA", "Avg": "NA"},
                        "OZONE": {"Min": "NA", "Max": "NA", "Avg": "NA"},
                        "NH3": {"Min": "NA", "Max": "NA", "Avg": "NA"}
                    }

                    for pollutant in station.findall('Pollutant_Index'):
                        pollutant_id = pollutant.get('id')
                        if pollutant_id in pollutants:
                            pollutants[pollutant_id]["Min"] = pollutant.get('Min')
                            pollutants[pollutant_id]["Max"] = pollutant.get('Max')
                            pollutants[pollutant_id]["Avg"] = pollutant.get('Avg')
                        else:
                            print(f"Unexpected pollutant ID '{pollutant_id}' found in station {station_name}")

                    # Air Quality Index
                    aqi = station.find('Air_Quality_Index')
                    aqi_value = aqi.get('Value') if aqi is not None else "NA"
                    predominant_parameter = aqi.get('Predominant_Parameter') if aqi is not None else "NA"

                    # Write row
                    writer.writerow([
                        country_name, state_name, city_name, station_name, latitude, longitude, last_update,
                        pollutants["PM2.5"]["Min"], pollutants["PM2.5"]["Max"], pollutants["PM2.5"]["Avg"],
                        pollutants["PM10"]["Min"], pollutants["PM10"]["Max"], pollutants["PM10"]["Avg"],
                        pollutants["NO2"]["Min"], pollutants["NO2"]["Max"], pollutants["NO2"]["Avg"],
                        pollutants["SO2"]["Min"], pollutants["SO2"]["Max"], pollutants["SO2"]["Avg"],
                        pollutants["CO"]["Min"], pollutants["CO"]["Max"], pollutants["CO"]["Avg"],
                        pollutants["OZONE"]["Min"], pollutants["OZONE"]["Max"], pollutants["OZONE"]["Avg"],
                        pollutants["NH3"]["Min"], pollutants["NH3"]["Max"], pollutants["NH3"]["Avg"],
                        aqi_value, predominant_parameter
                    ])

print(f"Data has been successfully converted to {output_csv}")
