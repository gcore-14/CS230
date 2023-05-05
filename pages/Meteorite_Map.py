import streamlit as st
import pandas as pd
#importing folium b/c an option in the instructions
import folium
from streamlit_folium import folium_static

dfinfo = pd.read_csv("Meteorite_Landings.csv")
dfinfo = dfinfo.dropna()
dfinfo = dfinfo[dfinfo['year'] <= 2023]

def maplocations(geo):
    st.subheader('Check out the first 100 meteors NASA tracked!')
    #getting the average lat and long to be the center of the map
    mean_lat, mean_long = geo['reclat'].mean(), geo['reclong'].mean()
    map_center = [mean_lat, mean_long]
    zoom_level = 1
    m = folium.Map(location=map_center, zoom_start=zoom_level, max_bounds=True)
    #sorting the values by ascending
    geo = geo.sort_values(
        by='year',
        ascending=True
    )
    #creating a tooltip so when you go across a dot on the map it gives you the name, year and exact location
    for index, row in geo.head(100).iterrows():
        name = row['name']
        lat = row['reclat']
        long = row['reclong']
        year = row['year']
        tooltip = f"{name}, in {year}: Location:({lat}, {long}))"

        folium.Marker([lat, long], tooltip=tooltip).add_to(m)
    folium_static(m)


maplocations(dfinfo)
