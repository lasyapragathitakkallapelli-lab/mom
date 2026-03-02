import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Birthday Mom!", layout="centered")

# Load your HTML file
with open("happybirthday47.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the HTML
components.html(html_content, height=800, scrolling=True)
