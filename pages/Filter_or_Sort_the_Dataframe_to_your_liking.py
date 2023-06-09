import streamlit as st
import pandas as pd
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)
from PIL import Image


dfinfo = pd.read_csv("Meteorite_Landings.csv")
dfinfo = dfinfo.dropna()
dfinfo = dfinfo[dfinfo['year'] <= 2023]



st.write('Select as many filters as you want to filter the data to meet your desire!')

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    from https://github.com/tylerjrichards/st-filter-dataframe/blob/main/streamlit_app.py
    """
    modify = st.checkbox("Add filters")
    #creating a checkbox so users can add filters 

    if not modify:
        return df

    


    modification_container = st.container()

    with modification_container:
        #creating a drop down filter, using the columns as the options
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            #a drop down if the filter has more options
            left.write("↳")
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                #filtering the dataframe based on the user choice
                df = df[df[column].isin(user_cat_input)]
            #if the column has numbers, display a slider
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    _min,
                    _max,
                    (_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
                #creating the inputs to be a min and max of the columns if there is a date
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            #if the column option isn't any of the above it creates a space for the user to input text of the specifics they want to sort or filter by
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].str.contains(user_text_input)]

    st.dataframe(df)

image = Image.open('meteor_shower_topic_1024.jpg')
st.image(image)




filter_dataframe(dfinfo)
