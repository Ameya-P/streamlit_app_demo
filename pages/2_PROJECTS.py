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
#builder.configure_default_column(editable = True, sorteable = True)
#builder.configure_auto_height()

#------------------ MultiColumn Header
builder.configure_column(field = "Basic Project Characteristics", 
                         children = [{ "field": "Project ID" },
                                     { "field": "Project Name" },
                                     { "field": "Voluntary Registry" },
                                     { "field": "ARB/WA Project" },
                                     { "field": "Voluntary Status" },
                                     { "field": "Scope" },
                                     { "field": "Type" },
                                     { "field": "Reduction / Removal" },
                                     { "field": "Methodology / Protocol" },
                                     { "field": "Region" },
                                     { "field": "Country" },
                                     { "field": "State" },
                                     { "field": "Project Site Location" },
                                     { "field": "Project Developer" },
                                     { "field": "First Year of Project (Vintage)"}]
                         )

builder.configure_column(field = "Credit Totals", 
                         children = [{ "field": "Total Credits Issued" },
                                     { "field": "Total Credits Retired" },
                                     { "field": "Total Credits Remaining" },
                                     { "field": "Total Buffer Pool Deposits" },
                                     { "field": "Reversals Covered by Buffer Pool" },
                                     { "field": "Reversals Not Covered by Buffer" }]
                         )
				 							
builder.configure_column(field = "Credits issued by vintage year (when reduction/removals occurred)", 
                         children = [{ "field": "1996_IV" },
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
                                     { "field": "2024_IV" }]
                         )

builder.configure_column(field = "Credits retired or cancelled in",
                        children = [{ "field": "1996_C" },
                                    { "field": "1997_C" },
                                    { "field": "1998_C" },
                                    { "field": "1999_C" },
                                    { "field": "2000_C" },
                                    { "field": "2001_C" },
                                    { "field": "2002_C" },
                                    { "field": "2003_C" },
                                    { "field": "2004_C" },
                                    { "field": "2005_C" },
                                    { "field": "2006_C" },
                                    { "field": "2007_C" },
                                    { "field": "2008_C" },
                                    { "field": "2009_C" },
                                    { "field": "2010_C" },
                                    { "field": "2011_C" },
                                    { "field": "2012_C" },
                                    { "field": "2013_C" },
                                    { "field": "2014_C" },
                                    { "field": "2015_C" },
                                    { "field": "2016_C" },
                                    { "field": "2017_C" },
                                    { "field": "2018_C" },
                                    { "field": "2019_C" },
                                    { "field": "2020_C" },
                                    { "field": "2021_C" },
                                    { "field": "2022_C" },
                                    { "field": "2023_C" },
                                    { "field": "2024_C" },
                                    { "field": "Year Unknown_C" }]
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