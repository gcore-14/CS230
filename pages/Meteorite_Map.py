import streamlit as st
import pandas as pd

import folium
from streamlit_folium import folium_static

dfinfo = pd.read_csv("In class/final/Meteorite_Landings.csv")
dfinfo = dfinfo.dropna()
dfinfo = dfinfo[dfinfo['year'] <= 2023]

def maplocations(geo):
    st.subheader('Check out the first 100 meteors NASA tracked!')
    mean_lat, mean_long = geo['reclat'].mean(), geo['reclong'].mean()
    map_center = [mean_lat, mean_long]
    zoom_level = 1
    m = folium.Map(location=map_center, zoom_start=zoom_level, max_bounds=True)
    geo = geo.sort_values(
        by='year',
        ascending=True
    )
    for index, row in geo.head(100).iterrows():
        name = row['name']
        lat = row['reclat']
        long = row['reclong']
        year = row['year']
        tooltip = f"{name}, {year}: Location:({lat}, {long}))"

        folium.Marker([lat, long], tooltip=tooltip).add_to(m)
    folium_static(m)


maplocations(dfinfo)
