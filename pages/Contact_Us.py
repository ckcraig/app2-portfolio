import streamlit as st

st.set_page_config(layout="wide")

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message here")
    submit_button = st.form_submit_button("Send Message")
    if submit_button:
        # message = message + user_email
        print("Pressed successfully")