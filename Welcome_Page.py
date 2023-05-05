"""
Name: Gregory Cormier
CS230: Section 3
Data: Meteorite Landings
Description:
This program takes in 2 csv files, turning them both into dataframes, then using those dataframes for images such as maps, pie-charts, bar graphs, etc.)
Extra Credit: used Lambda in ______ and uploaded to Streamlit.io (https://gcore-14-cs230-welcome-page-3d9nyj.streamlit.app/)
"""

import streamlit as st
import pandas as pd
from PIL import Image





st.title("Welcome to the World of Meteors!")

st.sidebar.success("Select a demo above.")

image = Image.open('190801-meteor-shower-cs-124p.jpg')
st.image(image)



