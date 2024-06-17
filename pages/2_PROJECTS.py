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

#------------------ Hide columns that aren't formatted properly
builder.configure_columns(column_names = ["Project ID", "Project Name", "Voluntary Registry", "ARB/WA Project", "Voluntary Status", "Scope", 
                                          " Type", "Reduction / Removal", "Methodology / Protocol", "Region", "Country", "State", "Project Site Location", 
                                          "Project Developer", "Total Credits Issued", "Total Credits Retired", "Total Credits Remaining", 
                                          "Total Buffer Pool Deposits", "Reversals Covered by Buffer Pool", "Reversals Not Covered by Buffer", 
                                          "First Year of Project (Vintage)", "1996_IV", "1997_IV", "1998_IV", "1999_IV", "2000_IV", "2001_IV", 
                                          "2002_IV", "2003_IV", "2004_IV", "2005_IV", "2006_IV", "2007_IV", "2008_IV", "2009_IV", "2010_IV", "2011_IV", 
                                          "2012_IV", "2013_IV", "2014_IV", "2015_IV", "2016_IV", "2017_IV", "2018_IV", "2019_IV", "2020_IV", "2021_IV", 
                                          "2022_IV", "2023_IV", "2024_IV", "1996_C", "1997_C", "1998_C", "1999_C", "2000_C", "2001_C", "2002_C", "2003_C", 
                                          "2004_C", "2005_C", "2006_C", "2007_C", "2008_C", "2009_C", "2010_C", "2011_C", "2012_C", "2013_C", "2014_C", 
                                          "2015_C", "2016_C", "2017_C", "2018_C", "2019_C", "2020_C", "2021_C", "2022_C", "2023_C", "2024_C", 
                                          "Year Unknown_C", "1996_R", "1997_R", "1998_R", "1999_R", "2000_R", "2001_R", "2002_R", "2003_R", "2004_R", 
                                          "2005_R", "2006_R", "2007_R", "2008_R", "2009_R", "2010_R", "2011_R", "2012_R", "2013_R", "2014_R", "2015_R", "2016_R", 
                                          "2017_R", "2018_R", "2019_R", "2020_R", "2021_R", "2022_R", "2023_R", "2024_R", "Project Owner ", 
                                          "Offset Project Operator ", "Authorized Project Designee", "Verifier", "Estimated Annual Emission Reductions", " PERs ", 
                                          "Registry / ARB / WA", "ARB Project Detail", "ARB ID", "PoA ID/Aggregate ID", "CORSIA Eligible", "Project Listed", 
                                          "Project Registered ", "CCB / Certifications", "Project Type From the Registry", "Registry Documents", "Project Website", 
                                          "1996_II", "1997_II", "1998_II", "1999_II", "2000_II", "2001_II", "2002_II", "2003_II", "2004_II", "2005_II", "2006_II", "2007_II", 
                                          "2008_II", "2009_II", "2010_II", "2011_II", "2012_II", "2013_II", "2014_II", "2015_II", "2016_II", "2017_II", "2018_II", "2019_II", 
                                          "2020_II", "2021_II", "2022_II", "2023_II", "2024_II", "Notes from Registry", "Notes from Berkeley Carbon Trading Project", 
                                          "Added to Database Version - With Data Through"], 
                                          lock_visible = True)

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
                        children = [{ "field": "1996_II" },
                                    { "field": "1997_II" },
                                    { "field": "1998_II" },
                                    { "field": "1999_II" },
                                    { "field": "2000_II" },
                                    { "field": "2001_II" },
                                    { "field": "2002_II" },
                                    { "field": "2003_II" },
                                    { "field": "2004_II" },
                                    { "field": "2005_II" },
                                    { "field": "2006_II" },
                                    { "field": "2007_II" },
                                    { "field": "2008_II" },
                                    { "field": "2009_II" },
                                    { "field": "2010_II" },
                                    { "field": "2011_II" },
                                    { "field": "2012_II" },
                                    { "field": "2013_II" },
                                    { "field": "2014_II" },
                                    { "field": "2015_II" },
                                    { "field": "2016_II" },
                                    { "field": "2017_II" },
                                    { "field": "2018_II" },
                                    { "field": "2019_II" },
                                    { "field": "2020_II" },
                                    { "field": "2021_II" },
                                    { "field": "2022_II" },
                                    { "field": "2023_II" },
                                    { "field": "2024_II" }]
                        )

builder.configure_column(field = "Additional Project Characteristics",
                        children = [{ "field": "Notes from Registry" },
                                    { "field": "Notes from Berkeley Carbon Trading Project" },
                                    { "field": "Added to Database Version - With Data Through" }]
                        )

go = builder.build()

grid_return = AgGrid(projects_tab, go)