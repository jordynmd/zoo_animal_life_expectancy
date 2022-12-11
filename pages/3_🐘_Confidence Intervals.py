import pandas as pd
import altair as alt
import streamlit as st

zoo = pd.read_csv('zoo_data.csv')

st.title('Animal Age Confidence Interval')

options = st.selectbox('Overall Confidence Interval', ('','Overall CI Upper','Overall CI Lower'))
if options == 'Overall CI Upper':
    st.write(alt.Chart(zoo).mark_point().encode(
        x=alt.X('Overall CI - upper:Q'),
        y=alt.Y('TaxonClass:N', sort='-x'),
        color=alt.Color('TaxonClass', scale=alt.Scale(scheme='turbo')),
        tooltip=['Species Common Name','Overall CI - upper']
    ).properties(height=300, width=700))

if options== 'Overall CI Lower':
    st.write(alt.Chart(zoo).mark_point().encode(
        x=alt.X('Overall CI - lower:Q'),
        y=alt.Y('TaxonClass:N', sort='-x'),
        color=alt.Color('TaxonClass', scale=alt.Scale(scheme='turbo')),
        tooltip=['Species Common Name','Overall CI - lower']
    ).properties(height=300, width=700))
options2= st.selectbox('Male or Female Confidence Interval', ('','Male CI Upper','Male CI Lower','Female CI Upper','Female CI Lower'))

if options2== 'Male CI Upper':
    st.write(alt.Chart(zoo).mark_point().encode(
        x=alt.X('Male CI - upper:Q'),
        y=alt.Y('TaxonClass:N', sort='-x'),
        color=alt.Color('TaxonClass', scale=alt.Scale(scheme='turbo')),
        tooltip=['Species Common Name','Male CI - upper']
    ).properties(height=300, width=700))

if options2== 'Male CI Lower':
    st.write(alt.Chart(zoo).mark_point().encode(
        x=alt.X('Male CI - lower:Q'),
        y=alt.Y('TaxonClass:N', sort='-x'),
        color=alt.Color('TaxonClass', scale=alt.Scale(scheme='turbo')),
        tooltip=['Species Common Name','Male CI - lower']
    ).properties(height=300, width=700))

if options2== 'Female CI Upper':
    st.write(alt.Chart(zoo).mark_point().encode(
    x=alt.X('Female CI - upper:Q'),
    y=alt.Y('TaxonClass:N', sort='-x'),
    color=alt.Color('TaxonClass', scale=alt.Scale(scheme='turbo')),
    tooltip=['Species Common Name','Female CI - upper']
    ).properties(height=300, width=700))

if options2== 'Female CI Lower':
    st.write(alt.Chart(zoo).mark_point().encode(
    x=alt.X('Female CI - lower:Q'),
    y=alt.Y('TaxonClass:N', sort='-x'),
    color=alt.Color('TaxonClass', scale=alt.Scale(scheme='turbo')),
    tooltip=['Species Common Name','Female CI - lower']
    ).properties(height=300, width=700))




