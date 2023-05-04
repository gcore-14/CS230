import streamlit as st
import pandas as pd
from PIL import Image

dfinfo = pd.read_csv("Meteorite_Landings.csv")
dfinfo = dfinfo.dropna()
dfinfo = dfinfo[dfinfo['year'] <= 2023]


def yearfreq(years):
   year_counts = {}
   dataframe = years['year'].apply(lambda x: None if x < 0 else x)

   for i in dataframe:
       if i in year_counts:
           year_counts[i] += 1
       else:
           year_counts[i] = 1
   min_year = int(dataframe.min())
   max_year = int(dataframe.max())
   start, end = st.slider(
       'Select a range of years to see the total meteorite landing in that range!',
       min_year, max_year, value=(min_year, max_year)
   )
   st.write(f'Outputted range will be in between {start} and {end}')



   def run_code():
       dates = [year[0] for year in year_counts.items() if start <= year[0] <= end]
       totals = [year[1] for year in year_counts.items() if start <= year[0] <= end]
       data = {'year': dates, 'count': totals}
       df = pd.DataFrame(data)
       st.bar_chart(df, x='year', y='count')
   if st.button('Run Code'):
       run_code()

   image = Image.open('difference-meteors-meteoroids-meteorites-meteorite-Allende-example.jpg')
   st.image(image)



yearfreq(dfinfo)
