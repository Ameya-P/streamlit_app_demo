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

builder.configure_auto_height(autoHeight = True)

#------------------ MultiColumn Header
basic_characteristics = []

for col in projects_tab.columns[:14]:
    basic_characteristics.append({"field": col, "filter": True})

basic_characteristics.append({ "field": "First Year of Project (Vintage)"})

builder.configure_column(field = "Basic Project Characteristics", 
                         children = basic_characteristics
                         )

#---
totals = []

for col in projects_tab.columns[14:20]:
    totals.append({"field": col, "filter": True})
    
builder.configure_column(field = "Credit Totals", 
                         children = totals)

#---	
issued_vintage = []

for col in projects_tab.columns[21:50]:
    issued_vintage.append({"field": col, "headerName": col[0:4], "filter": True})
    
	 							
builder.configure_column(field = "Credits issued by vintage year (when reduction/removals occurred)", 
                         children = issued_vintage
                         )

#--- 
cancelled = []

for col in projects_tab.columns[50:80]:
    cancelled.append({"field": col, "headerName": col[0:4], "filter": True})

builder.configure_column(field = "Credits retired or cancelled in",
                        children = cancelled
                        )

#--
remaining = []

for col in projects_tab.columns[80:109]:
    remaining.append({"field": col, "headerName": col[0:4], "filter": True})

builder.configure_column(field = "Credits remaining by vintage",
                        children = remaining
                        )

#--
additional = []

for col in projects_tab.columns[109:126]:
    additional.append({"field": col, "filter": True})

builder.configure_column(field = "Additional Project Characteristics",
                        children = additional
                        )

#--
issued_issuance = []

for col in projects_tab.columns[126:155]:
    issued_issuance.append({"field": col, "headerName": col[0:4], "filter": True})
    
builder.configure_column(field = "Credits issued by issuance year (when the registry issued the credits)",
                        children = issued_issuance
                        )

#--
notes = []

for col in projects_tab.columns[155:158]:
    notes.append({"field": col, "filter": True})

builder.configure_column(field = "Additional Project Characteristics",
                        children = notes
                        )

go = builder.build()

#------------------ Hide columns that aren't formatted properly
options_list = go.get('columnDefs')
go['columnDefs'] = options_list[158:] #158 = number of columns in original data table

grid_return = AgGrid(projects_tab, go)