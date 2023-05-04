import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

dfinfo = pd.read_csv("In class/final/Meteorite_Landings.csv")
dfinfo = dfinfo.dropna()
dfinfo = dfinfo[dfinfo['year'] <= 2023]

def mostfreq(value):
    st.subheader("Check out the most frequent classifications of meteors!")
    counts = {}
    dataframe = value['recclass'].value_counts()[:10].index.tolist()
    dfinfo = value['recclass']
    for i in dfinfo:
        if i in dataframe:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
    labels = []
    freq = []
    for x, y in counts.items():
        labels.append(x)
        freq.append(y)
    fig, ax = plt.subplots()
    ax.axis('equal')
    ax.set_title("Top 10 Meteorite Classifications")
    ax.pie(freq, labels=labels, autopct='%.2f%%')

    st.pyplot(fig)
    return counts

mostfreq(dfinfo)
