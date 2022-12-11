import pandas as pd
import altair as alt
import streamlit as st

st.set_page_config(layout="centered")
zoo = pd.read_csv('zoo_data.csv')


st.title('Zoo Animals and Their Median Life Expectancies')
st.write('Zoos are created to entertain and educate the public, and often have a strong emphasis on scientific research and species conservation.  The continuation of reputable zoos allows scientists to gain more information on the behaviorial, nutrtional, and health aspects of these animals.')
emp1, writemid, emp3 = st.columns(3)
with emp1:
    st.image('https://letshannondunk.com/wp-content/uploads/sites/8/2017/02/953.jpg')
with emp3:
    st.image('https://sundaymarketnetwork.files.wordpress.com/2022/02/pexels-photo-1316297.jpeg')
with writemid:
    st.image('https://miro.medium.com/max/1400/1*EXZ22TcQHuBuij5vl4g2Zg.jpeg')

class_count = zoo.groupby(['TaxonClass'])['TaxonClass'].count().reset_index(name='Count')

st.write(" ")

st.write(alt.Chart(class_count).configure_title().mark_bar().encode(
    x=alt.X('Count:Q',),
    y=alt.Y('TaxonClass:N', sort='-x'),
    color=alt.Color('TaxonClass:N', scale=alt.Scale(scheme='turbo') )
    ).properties(
        title='Number of Animals in Each Taxon Class', width=1000
    ))

option = st.selectbox('Description of Taxon Class',
('','Amphibia','Arachnida','Aves','Chondrichthyes','Mammalia','Reptilia' ))

if option == 'Mammalia':
    st.write('Mammals are a group of vertebrate animals constituting the class Mammalia, characterized by the presence of mammary glands which in females produce milk for feeding their young, a neocortex, fur or hair, and three middle ear bones.')
    st.write(
        alt.Chart(zoo).mark_point().encode(
            x=alt.X('Overall Sample Size:Q'),
            y=alt.Y('TaxonClass:N', sort='-x'),
            color=alt.Color('TaxonClass:N', scale=alt.Scale(scheme='turbo'))
            ).properties(height=400, width=900, title='Sample Number of Animals by Taxon Class'))
if option == 'Aves':
    st.write('Birds are a group of warm-blooded vertebrates constituting the class Aves, characterised by feathers, toothless beaked jaws, the laying of hard-shelled eggs, a high metabolic rate, a four-chambered heart, and a strong yet lightweight skeleton.')
    st.write(
        alt.Chart(zoo).mark_point().encode(
            x=alt.X('Overall Sample Size:Q'),
            y=alt.Y('TaxonClass:N', sort='-x'),
            color=alt.Color('TaxonClass:N', scale=alt.Scale(scheme='turbo'
            ))).properties(height=400, width=900, title='Sample Number of Animals by Taxon Class'))
if option == 'Reptilia':
    st.write('Reptiles, as most commonly defined are the animals in the class Reptilia, a paraphyletic grouping comprising all sauropsids except birds. Living reptiles comprise turtles, crocodilians, squamates and rhynchocephalians.')
    st.write(
        alt.Chart(zoo).mark_point().encode(
            x=alt.X('Overall Sample Size:Q'),
            y=alt.Y('TaxonClass:N', sort='-x'),
            color=alt.Color('TaxonClass:N', scale=alt.Scale(scheme='turbo'
            ))).properties(height=400, width=900, title='Sample Number of Animals by Taxon Class'))
if option == 'Amphibia':
    st.write('Amphibians are four-limbed and ectothermic vertebrates of the class Amphibia. All living amphibians belong to the group Lissamphibia. They inhabit a wide variety of habitats, with most species living within terrestrial, fossorial, arboreal or freshwater aquatic ecosystems.')
    st.write(
        alt.Chart(zoo).mark_point().encode(
            x=alt.X('Overall Sample Size:Q'),
            y=alt.Y('TaxonClass:N', sort='-x'),
            color=alt.Color('TaxonClass:N', scale=alt.Scale(scheme='turbo'
            ))).properties(height=400, width=900, title='Sample Number of Animals by Taxon Class'))
if option == 'Arachnida':
    st.write('Arachnida is a class of joint-legged invertebrate animals, in the subphylum Chelicerata. Arachnida includes, among others, spiders, scorpions, ticks, mites, pseudoscorpions, harvestmen, camel spiders, whip spiders and vinegaroons.')
    st.write(
        alt.Chart(zoo).mark_point().encode(
            x=alt.X('Overall Sample Size:Q'),
            y=alt.Y('TaxonClass:N', sort='-x'),
            color=alt.Color('TaxonClass:N', scale=alt.Scale(scheme='turbo'
            ))).properties(height=400, width=900, title='Sample Number of Animals by Taxon Class'))
if option == 'Chondrichthyes':
    st.write('Chondrichthyes is a class that contains the cartilaginous fishes that have skeletons primarily composed of cartilage. They can be contrasted with the Osteichthyes or bony fishes, which have skeletons primarily composed of bone tissue.')
    st.write(
        alt.Chart(zoo).mark_point().encode(
            x=alt.X('Overall Sample Size:Q'),
            y=alt.Y('TaxonClass:N', sort='-x'),
            color=alt.Color('TaxonClass:N', scale=alt.Scale(scheme='turbo'
            ))).properties(height=400, width=900, title='Sample Number of Animals by Taxon Class'))
