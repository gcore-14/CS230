import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

dfinfo = pd.read_csv("Meteorite_Landings.csv")
dfinfo = dfinfo.dropna()
dfinfo = dfinfo[dfinfo['year'] <= 2023]
#making sure the year is less than 2023
st.subheader('Year and Mass Correlation')
st.write('Choose what year to start with!')
def scatter(plot):
    #asking the user for a number to update the scatter plot using year and mass (g) then plotting it
    number = st.number_input(f"Type in a number in between {int(plot['year'].min())} and {int(plot['year'].max())}")
    plot = plot[plot['year'] >= number]
    fig, ax = plt.subplots()
    ax.scatter(plot['year'], plot['mass (g)'])
    ax.set_xlabel('Year')
    ax.set_ylabel('Mass (g)')
    ax.set_title("Scatterplot relationship between mass(g) and year")

    st.pyplot(fig)

scatter(dfinfo)
