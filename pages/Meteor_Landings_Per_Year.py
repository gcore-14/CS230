import streamlit as st
import pandas as pd
from PIL import Image

dfinfo = pd.read_csv("Meteorite_Landings.csv")
dfinfo = dfinfo.dropna()
dfinfo = dfinfo[dfinfo['year']]


def yearfreq(years):
   year_counts = {}
   #using lambda to get rid of years less than 0 greater than the current year
   dataframe = years['year'].apply(lambda x: None if x < 0 or x > 2024 else x)
#using similar count method from selecting classifications to do the count
#if the year_counts is in both dataframe and year_counts then it adds by 1, if not it adds it to the dictionary
#i shows the years
   for i in dataframe:
       if i in year_counts:
           year_counts[i] += 1
       else:
           year_counts[i] = 1
   #getting the min and max year to show on the slider
   min_year = int(dataframe.min())
   max_year = int(dataframe.max())
   start, end = st.slider(
       'Select a range of years to see the total meteorite landing in that range!',
       min_year, max_year, value=(min_year, max_year)
   )
   st.write(f'Outputted range will be in between {start} and {end}')


#adding another function so if the button is pressed then the above code is run
   def run_code():
      #list comprehension so the dates and totals are computed
      #if the the year is in between start and end then dates = the given year, the same for totals, but it is the total amount per year
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
