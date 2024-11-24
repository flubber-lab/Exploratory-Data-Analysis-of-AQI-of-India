import pandas as pd
import numpy as np

#read the csv file
df = pd.read_csv('/content/drive/MyDrive/Data for analysis/AQI India - 2023/aqi_data.csv')
df
#to drop duplicate values
df= df.drop_duplicates()

#Inspect the data
print(df.head())
print(df.info())
print(df.describe())

#Check for missing values
missing=df.isnull().sum()
print(missing)

#fill missing values
df.fillna('NA', inplace=True)

# NaN is recognized as a float: Using NaN ensures the column remains of the correct numerical type (e.g., float64) instead of being coerced into an object type.
df.replace('NA', np.nan, inplace=True)

# Summary of AQI
print(df['Air_Quality_Index_Value'].describe())

# Distribution plot for PM2.5 Average
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df['PM2.5_Avg'].dropna(), bins=30, kde=True)
plt.title('Distribution of PM2.5 (Average)')
plt.show()

#Geospatial Analysis

import folium

# Create a map
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered on India

# Add station markers
for i, row in data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row['Station']}<br>PM2.5: {row['PM2.5_Avg']}",
    ).add_to(m)

# Save and display map
m.save("India_AQI_Map.html")
