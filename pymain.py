import streamlit as st
import streamlit.components.v1 as components
import base64

# Function to embed local images into HTML
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load your HTML content
with open("happybirthday47.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace image paths in HTML with base64-encoded data
for image_name in ["1.jpg", "2.jpg"]:
    base64_str = get_base64_image(image_name)
    html_content = html_content.replace(
        image_name, f"data:image/jpeg;base64,{base64_str}"
    )

st.set_page_config(page_title="Happy Birthday Mom!", layout="centered")
components.html(html_content, height=1000, scrolling=True)True)
