import streamlit as st
from send_email import send_email
import email.header


st.set_page_config(layout="wide")

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message here")

    message = f"""\
Subject: New email from Portfolio App | {user_email}

From: {user_email}
{raw_message}
"""
    submit_button = st.form_submit_button("Send Message")
    if submit_button:
        print("Pressed successfully")
        send_email(message)
        st.info("Your email was successfully sent!")
