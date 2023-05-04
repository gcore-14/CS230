"""
Name: Gregory Cormier
CS230: Section 3
Data: Meteorite Landings
Description:
This program ... (a few sentences about your program and the queries and charts)
"""

import streamlit as st
import pandas as pd
from PIL import Image





st.title("Welcome to the World of Meteors!")

st.sidebar.success("Select a demo above.")

image = Image.open('In class/final/190801-meteor-shower-cs-124p.jpg')
st.image(image)



