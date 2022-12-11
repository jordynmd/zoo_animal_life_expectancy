import pandas as pd
import altair as alt
import streamlit as st

st.set_page_config(layout="centered")
zoo = pd.read_csv('zoo_data.csv')
st.title('Animal Median Life Expectancy 🦓')


st.write(alt.Chart(zoo).mark_point().encode(
x=alt.X('Male MLE:Q'),
y=alt.Y('Female MLE:Q' ),
color=alt.Color('TaxonClass:N', scale=alt.Scale(scheme='turbo'))).properties(
title='Male vs Female Median Life Expectancy',
width=600
))




option = st.selectbox('MLE by Species Common Name', ('','Male MLE', 'Female MLE','Both'))
col1, col2 = st.columns(2)
if option == 'Male MLE':
    with col1:
        st.write(alt.Chart(zoo).mark_bar().encode(
        x=alt.X('Male MLE'),
        y=alt.Y('Species Common Name', sort='-x' )
        ).properties(title='Male Median Life Expectancy',width=600))

if option=='Female MLE':
    with col2:
        st.write(alt.Chart(zoo).mark_bar().encode(
            x=alt.X('Female MLE', stack='zero'),
            y=alt.Y('Species Common Name', sort='-x' )
        ).properties(title='Female Median Life Expectancy', width=600))

if option=='Both':
    col11, col12 = st.columns(2)
    with col11:
        st.write(alt.Chart(zoo).mark_bar().encode(
        x=alt.X('Male MLE'),
        y=alt.Y('Species Common Name', sort='-x' )
        ).properties(title='Male Median Life Expectancy',width=600))
    with col12:
        st.write(alt.Chart(zoo).mark_bar().encode(
            x=alt.X('Female MLE', stack='zero'),
            y=alt.Y('Species Common Name', sort='-x' )
        ).properties(title='Female Median Life Expectancy', width=600))

st.write(alt.Chart(zoo).mark_rect().encode(
    alt.X('Female MLE:Q', bin=alt.Bin(maxbins=40)),
    alt.Y('Male MLE:Q', bin=alt.Bin(maxbins=20)),
    alt.Color('Overall MLE:Q', scale=alt.Scale(scheme='turbo')
)).properties(title='Binned Female and Male MLE Values', width=600))


    