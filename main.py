import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Christopher Craig")
    content = """
    Hello! My name is Christopher and I'm a budding program developer. Currently working
    in Tech and doing a lot of data management, so I thought Python would be a perfect first
    add to my quiver. 
    
    After this I plan on brushing up on my HTML & CSS and then adding
    JavaScript to the mix. I'll then get into some other coding like iOS and C#.
    """
    st.info(content)
