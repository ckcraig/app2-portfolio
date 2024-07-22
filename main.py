import pandas
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Christopher Craig")
    content = """
    Hello! 
    
    My name is Christopher and I'm a budding program developer. Currently working
    in Tech and doing a lot of data management, so I thought Python would be a perfect first
    add to my quiver. 
    
    After this I plan on brushing up on my HTML & CSS and then adding
    JavaScript to the mix. I'll then get into some other coding like iOS and C#.
    """
    st.info(content)

tag = """
    Below you can find some of the apps that I have built with Python. Feel free to contact me!
    """
st.write(tag)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

    st.image("images/1.png")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])

    st.image("images/2.png")