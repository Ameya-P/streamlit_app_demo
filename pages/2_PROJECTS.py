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

builder.configure_auto_height()

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

for col in projects_tab.columns[21:50]:
    cancelled.append({"field": col, "headerName": col[0:4], "filter": True})

builder.configure_column(field = "Credits retired or cancelled in",
                        children = cancelled
                        )

builder.configure_column(field = "Credits remaining by vintage",
                        children = [{ "field": "1996_R" },
                                    { "field": "1997_R" },
                                    { "field": "1998_R" },
                                    { "field": "1999_R" },
                                    { "field": "2000_R" },
                                    { "field": "2001_R" },
                                    { "field": "2002_R" },
                                    { "field": "2003_R" },
                                    { "field": "2004_R" },
                                    { "field": "2005_R" },
                                    { "field": "2006_R" },
                                    { "field": "2007_R" },
                                    { "field": "2008_R" },
                                    { "field": "2009_R" },
                                    { "field": "2010_R" },
                                    { "field": "2011_R" },
                                    { "field": "2012_R" },
                                    { "field": "2013_R" },
                                    { "field": "2014_R" },
                                    { "field": "2015_R" },
                                    { "field": "2016_R" },
                                    { "field": "2017_R" },
                                    { "field": "2018_R" },
                                    { "field": "2019_R" },
                                    { "field": "2020_R" },
                                    { "field": "2021_R" },
                                    { "field": "2022_R" },
                                    { "field": "2023_R" },
                                    { "field": "2024_R" }]
                        )

builder.configure_column(field = "Additional Project Characteristics",
                        children = [{ "field": "Project Owner" },
                                    { "field": "Offset Project Operator" },
                                    { "field": "Authorized Project Designee" },
                                    { "field": "Verifier" },
                                    { "field": "Estimated Annual Emission Reductions" },
                                    { "field": "PERs" },
                                    { "field": "Registry / ARB / WA" },
                                    { "field": "ARB Project Detail" },
                                    { "field": "ARB ID" },
                                    { "field": "PoA ID/Aggregate ID" },
                                    { "field": "CORSIA Eligible" },
                                    { "field": "Project Listed" },
                                    { "field": "Project Registered" },
                                    { "field": "CCB / Certifications" },
                                    { "field": "Project Type From the Registry"},
                                    { "field": "Registry Documents"},
                                    { "field": "Project Website"}]
                        )

builder.configure_column(field = "Credits issued by issuance year (when the registry issued the credits)",
                        children = [{ "field": "1996_II", "headerName": "1996"},
                                    { "field": "1997_II", "headerName": "1997" },
                                    { "field": "1998_II", "headerName": "1998" },
                                    { "field": "1999_II", "headerName": "1999" },
                                    { "field": "2000_II", "headerName": "2000" },
                                    { "field": "2001_II", "headerName": "2001" },
                                    { "field": "2002_II", "headerName": "2002" },
                                    { "field": "2003_II", "headerName": "2003" },
                                    { "field": "2004_II", "headerName": "2004" },
                                    { "field": "2005_II", "headerName": "2005" },
                                    { "field": "2006_II", "headerName": "2006" },
                                    { "field": "2007_II", "headerName": "2007" },
                                    { "field": "2008_II", "headerName": "2008" },
                                    { "field": "2009_II", "headerName": "2009" },
                                    { "field": "2010_II", "headerName": "2010" },
                                    { "field": "2011_II", "headerName": "2011" },
                                    { "field": "2012_II", "headerName": "2012" },
                                    { "field": "2013_II", "headerName": "2013" },
                                    { "field": "2014_II", "headerName": "2014" },
                                    { "field": "2015_II", "headerName": "2015" },
                                    { "field": "2016_II", "headerName": "2016" },
                                    { "field": "2017_II", "headerName": "2017" },
                                    { "field": "2018_II", "headerName": "2018" },
                                    { "field": "2019_II", "headerName": "2019" },
                                    { "field": "2020_II", "headerName": "2020" },
                                    { "field": "2021_II", "headerName": "2021" },
                                    { "field": "2022_II", "headerName": "2022" },
                                    { "field": "2023_II", "headerName": "2023" },
                                    { "field": "2024_II", "headerName": "2024" }]
                        )

builder.configure_column(field = "Additional Project Characteristics",
                        children = [{ "field": "Notes from Registry" },
                                    { "field": "Notes from Berkeley Carbon Trading Project" },
                                    { "field": "Added to Database Version - With Data Through" }]
                        )

go = builder.build()

#------------------ Hide columns that aren't formatted properly
options_list = go.get('columnDefs')
go['columnDefs'] = options_list[158:] #158 = number of columns in original data table

grid_return = AgGrid(projects_tab, go)