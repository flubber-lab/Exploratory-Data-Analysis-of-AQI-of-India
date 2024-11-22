India Air Quality Index (AQI) Data Analysis

This repository contains Air Quality Index (AQI) data (2023) for various locations across India, originally provided in an XML format. The data has been processed and converted into a CSV format for easy analysis. Additionally, we aim to perform exploratory data analysis (EDA) on this dataset to uncover patterns, insights, and trends about air quality in India.

Data Description

Original XML File
The XML file contains hierarchical data with the following structure:

Country: The country (India) containing air quality data.
State: States within India.
City: Cities within each state.
Station: Monitoring stations providing air quality data.
Pollutant_Index: Contains pollutant data for:
PM2.5
PM10
NO2
SO2
CO
OZONE
NH3
Air_Quality_Index: Provides the overall AQI and predominant pollutant at the station.

Processed CSV File
The XML data was transformed into a tabular CSV format, with each row representing a monitoring station and its corresponding data. Columns in the CSV include:

Geographical Information: Country, State, City, Station, Latitude, Longitude
Time Information: LastUpdate
Pollutant Data: Minimum (Min), Maximum (Max), and Average (Avg) values for each pollutant
Air Quality Index: Air_Quality_Index_Value, Predominant_Parameter

How We Processed the Data

Parsed the XML File:
The hierarchical XML structure was parsed using Python's xml.etree.ElementTree.
Extracted details such as country, state, city, station name, latitude, longitude, and pollutants.
Transformed to CSV:
Flattened the XML data into a tabular structure using Python.
Included pollutant information for PM2.5, PM10, NO2, SO2, CO, OZONE, and NH3.
Calculated values for the Air_Quality_Index (if available).
Saved the Data:
Saved the processed data into aqi_data.csv, making it ready for analysis.

Future Plans: Exploratory Data Analysis (EDA)

We will perform detailed EDA on the CSV file to uncover patterns, trends, and insights, including:

Summary Statistics:
Analyze overall pollutant levels and AQI across states and cities.
Identify regions with the highest and lowest pollution levels.

Missing Data Analysis:
Examine missing or incomplete data and its impact.

Geospatial Analysis:
Visualize pollutant levels geographically using mapping tools like folium.

Pollutant Comparison:
Compare levels of different pollutants across regions.
Analyze which pollutants dominate AQI in different states.

Time-based Trends:
If timestamps are available, explore how AQI and pollutants change over time.

Correlation Analysis:
Examine relationships between different pollutants and overall AQI.

