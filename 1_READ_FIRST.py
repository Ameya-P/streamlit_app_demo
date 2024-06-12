from PIL import Image
import streamlit as st

logo = Image.open("resources/berkeley_logo.png")

st.set_page_config(
    page_title="Voluntary Registry Offsets Database",
    page_icon=logo,
)

st.title("Voluntary Registry Offsets Database")