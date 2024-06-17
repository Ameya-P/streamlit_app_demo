from PIL import Image
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid import GridOptionsBuilder
import pandas as pd

logo = Image.open("resources/berkeley_logo.png")
st.set_page_config(
    layout="wide",
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
projects_tab = pd.read_csv("resources/v11.csv")

builder = GridOptionsBuilder.from_dataframe(projects_tab)
builder.configure_default_column(editable = True, sorteable = True)
#builder.configure_auto_height()
builder.configure_column(header_name = "Credits issued by issuance year (when the registry issued the credits)", 
                         children = [{ "field": "1996_IV" },{ "field": "1997_IV" }]
                         )

go = builder.build()

grid_options = {
"columnDefs": [
{
"headerName": "Credits issued by issuance year (when the registry issued the credits)",
"children": [
{ "field": "1996_IV" },
{ "field": "1997_IV" },
{ "field": "1998_IV" },
{ "field": "1999_IV" },
{ "field": "2000_IV" },
{ "field": "2001_IV" },
{ "field": "2002_IV" },
{ "field": "2003_IV" },
{ "field": "2004_IV" },
{ "field": "2005_IV" },
{ "field": "2006_IV" },
{ "field": "2007_IV" },
{ "field": "2008_IV" },
{ "field": "2009_IV" },
{ "field": "2010_IV" },
{ "field": "2011_IV" },
{ "field": "2012_IV" },
{ "field": "2013_IV" },
{ "field": "2014_IV" },
{ "field": "2015_IV" },
{ "field": "2016_IV" },
{ "field": "2017_IV" },
{ "field": "2018_IV" },
{ "field": "2019_IV" },
{ "field": "2020_IV" },
{ "field": "2021_IV" },
{ "field": "2022_IV" },
{ "field": "2023_IV" },
{ "field": "2024_IV" }
    ]
}
]
}

grid_return = AgGrid(projects_tab, go)