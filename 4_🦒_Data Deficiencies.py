import pandas as pd
import altair as alt
import streamlit as st

zoo = pd.read_csv('zoo_data.csv')

st.title('Data Deficiencies')

MDD = zoo.groupby(['Male Data Deficient'])['Male Data Deficient'].count().reset_index(name='Count')
FDD = zoo.groupby(['Female Data Deficient'])['Female Data Deficient'].count().reset_index(name='Count')

col1, col2, col3= st.columns(3)
with col1:
    st.write(alt.Chart(FDD).mark_bar().encode(
        x=alt.X('Female Data Deficient'),
        y=alt.Y('Count')
    ).properties(title='Count of Data Deficiency in Females'))
with col3:
    st.write(alt.Chart(MDD).mark_bar().encode(
        x=alt.X('Male Data Deficient'),
        y=alt.Y('Count')
    ).properties(title='Count of Data Deficiency in Males'))
with col2:
    st.write('A data deficient species is one which has been categorized by the International Union for Conservation of Nature as offering insufficient information for a proper assessment of conservation status to be made.')
    

url='https://www.nczoo.org/'
st.write("The North Carolina Zoo is a zoo in Asheboro, North Carolina, housing 1,800 animals of more than 250 species, primarily representing Africa and North America.  It is one of two state-supported zoos in the United States, with the other being the Minnesota Zoo.  For more imformation on  the [North Carolina Zoo](%s)" % url)
st.image('https://www.nczoo.com/wp-content/uploads/2016/06/1140x450_slider_zoo_entrance.jpg')