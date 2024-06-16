from PIL import Image
import streamlit as st
import pandas as pd

logo = Image.open("resources/berkeley_logo.png")

st.set_page_config(
    page_title="Voluntary Registry Offsets Database",
    page_icon=logo,
)

#------------------ Title
st.title("Voluntary Registry Offsets Database")

st.divider()

#------------------ Guide
st.header("Instructions")

st.markdown("*Filter & sort projects with drop down arrows. Use Data menu to clear filters.*")

#---
st.subheader("Color Guide")

st.markdown("Black entries are downloaded directly from the registries.")

st.markdown(":blue[Blue entries are added by Berkeley Carbon Trading Project based on registry data and documents.]")

st.markdown(":red[Red font indicates tallies of visible (filtered) projects only.]")

st.divider()

#------------------ Dataframe
projects_tab = pd.read_excel("resources/v11.xlsx")

st.dataframe(projects_tab)
