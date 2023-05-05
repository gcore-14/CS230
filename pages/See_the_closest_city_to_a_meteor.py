import streamlit as st
import pandas as pd

from haversine import haversine, Unit
import math



dfinfo = pd.read_csv("Meteorite_Landings.csv")
dfgeonames = pd.read_csv("geonames_cities.csv", sep=";")
dfgeonames1 = pd.concat([dfgeonames, dfgeonames['Coordinates'].str.split(', ', expand=True)], axis=1)
dfgeonames1 = dfgeonames1.rename(columns={0: 'Latitude', 1: 'Longitude'})
dfgeonames1 = dfgeonames1[dfgeonames1['Country name EN'].notna()]
#importing another csv file and splitting it up into 2 new columns for the locations

dfinfo = dfinfo.dropna()
dfinfo = dfinfo[dfinfo['year'] <= 2023]

def distance(meteorite, cities):
    #user selects what meteor they want information on 
    options = st.multiselect(
        'What Meteorite do you want to find?',
        meteorite['name']
    )
    dict_options = {}
    geo_options = {}
    locations = {}
    #for the chosen option, getting the location of it for the haversine function and also for the locations{} so can map it later
    for name in options:
        row = meteorite[meteorite['name'] == name].iloc[0]
        lat, long = row['reclat'], row['reclong']
        dict_options[name] = (lat, long)
        locations[name] = {'latitude': lat, 'longitude': long}

        for index, row in cities.iterrows():
            geo_name = row['Name']
            geo_country, geo_lat, geo_long = row['Country name EN'], float(row['Latitude']), float(row['Longitude'])
            geo_options[geo_name] = (geo_country, geo_lat, geo_long)


        distance = 1000
        town = None
        country = None
#using the haversine function, it finds the exact distance between the points and returns what the closest city is, replacing the distance, town, and country
        for key, value in geo_options.items():
            haver_distance = haversine((dict_options[name][0], dict_options[name][1]), (value[1], value[2]), unit=Unit.MILES)
            if haver_distance < distance:
                distance = haver_distance
                town = key
                country = value[0]
        st.write(f"The closest city to {name}, is {town} in {country}, and it is {round(distance,2)} miles away")
    df_locations = pd.DataFrame.from_dict(locations, orient='index')
    st.map(df_locations, zoom=2, use_container_width=True)
    st.text('The dot(s) show where the meteor landed')


distance(dfinfo, dfgeonames1)
