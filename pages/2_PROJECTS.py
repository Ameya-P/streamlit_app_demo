from PIL import Image
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid import GridOptionsBuilder
from st_aggrid import GridUpdateMode, DataReturnMode
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

builder.configure_column(field = "Notes",
                        children = notes
                        )

go = builder.build()

#------------------ 
def sum_col(df):
    total_sum = 0
    columnData = df.items()
    for index, value in columnData:
        if type(value) == type("string"):
            if value == " ":
                total_sum += 0
            else:
                total_sum += int(value.replace(",", ""))
        else:
            total_sum += value
    
    return total_sum


#------------------ Hide columns that aren't formatted properly
options_list = go.get('columnDefs')
go['columnDefs'] = options_list[158:] #158 = number of columns in original data table

#------------------ Totals 
names = ["Project ID", "Project Name", "Voluntary Registry", "ARB/WA Project", "Voluntary Status", "Scope", " Type", "Reduction / Removal", "Methodology / Protocol", "Region", "Country", "State", "Project Site Location", "Project Developer",
                                            "Total Credits Issued", "Total Credits Retired", "Total Credits Remaining", "Total Buffer Pool Deposits", "Reversals Covered by Buffer Pool", "Reversals Not Covered by Buffer", "First Year of Project (Vintage)", "1996_IV", "1997_IV",
                                            "1998_IV", "1999_IV", "2000_IV", "2001_IV", "2002_IV", "2003_IV", "2004_IV", "2005_IV", "2006_IV", "2007_IV", "2008_IV", "2009_IV", "2010_IV", "2011_IV", "2012_IV", "2013_IV", "2014_IV", "2015_IV", "2016_IV", "2017_IV", "2018_IV",
                                            "2019_IV", "2020_IV", "2021_IV", "2022_IV", "2023_IV", "2024_IV", "1996_C", "1997_C", "1998_C", "1999_C", "2000_C", "2001_C", "2002_C", "2003_C", "2004_C", "2005_C", "2006_C", "2007_C", "2008_C", "2009_C", "2010_C", "2011_C",
                                            "2012_C", "2013_C", "2014_C", "2015_C", "2016_C", "2017_C", "2018_C", "2019_C", "2020_C", "2021_C", "2022_C", "2023_C", "2024_C", "Year Unknown_C", "1996_R", "1997_R", "1998_R", "1999_R", "2000_R", "2001_R", "2002_R", "2003_R",
                                            "2004_R", "2005_R", "2006_R", "2007_R", "2008_R", "2009_R", "2010_R", "2011_R", "2012_R", "2013_R", "2014_R", "2015_R", "2016_R", "2017_R", "2018_R", "2019_R", "2020_R", "2021_R", "2022_R", "2023_R", "2024_R", "Project Owner ",
                                            "Offset Project Operator ", "Authorized Project Designee", "Verifier", "Estimated Annual Emission Reductions", " PERs ", "Registry / ARB / WA", "ARB Project Detail", "ARB ID", "PoA ID/Aggregate ID", "CORSIA Eligible",
                                            "Project Listed", "Project Registered ", "CCB / Certifications", "Project Type From the Registry", "Registry Documents", "Project Website", "1996_II", "1997_II", "1998_II", "1999_II", "2000_II", "2001_II", "2002_II", "2003_II",
                                            "2004_II", "2005_II", "2006_II", "2007_II", "2008_II", "2009_II", "2010_II", "2011_II", "2012_II", "2013_II", "2014_II", "2015_II", "2016_II", "2017_II", "2018_II", "2019_II", "2020_II", "2021_II", "2022_II", "2023_II", "2024_II",
                                            "Notes from Registry", "Notes from Berkeley Carbon Trading Project", "Added to Database Version - With Data Through"]

data = [""]
i = 0

#-- Basic Project Characteristics
df = projects_tab

data.append("All " + str(df.count) + " offset projects are visible")
for i in range(2,13):
    data.append("")

data.append("Totals for visible projects:")

for i in range(14,20):
    data.append(sum_col(df.iloc[:, i]))

data.append("")

for i in range(21,109):
    data.append(sum_col(df.iloc[:, i]))

for i in range(109,114):
    data.append("")

data.append(sum_col(df.iloc[:, 114]))

for i in range(115,126):
    data.append("")

for i in range(126,155):
    data.append(sum_col(df.iloc[:, i]))

for i in range(155,158):
    data.append("")

red_totals = pd.DataFrame([data], columns = names)

#--- Pinned Top Row
go['pinnedTopRowData'] = red_totals.to_dict(orient="records")

#------------------ Final Table
grid_return = AgGrid(projects_tab, go, 800, update_mode = GridUpdateMode.FILTERING_CHANGED, data_return_mode = DataReturnMode.FILTERED_AND_SORTED)

#------------------ Totals Table
data = [""]
i = 0

#-- Basic Project Characteristics
df = grid_return["data"]

data.append("All " + str(df.count) + " offset projects are visible")
for i in range(2,13):
    data.append("")

data.append("Totals for visible projects:")

for i in range(14,20):
    data.append(sum_col(df.iloc[:, i]))

data.append("")

for i in range(21,109):
    data.append(sum_col(df.iloc[:, i]))

for i in range(109,114):
    data.append("")

data.append(sum_col(df.iloc[:, 114]))

for i in range(115,126):
    data.append("")

for i in range(126,155):
    data.append(sum_col(df.iloc[:, i]))

for i in range(155,158):
    data.append("")

red_totals = pd.DataFrame([data], columns = names)

#------------------ Final Table
grid_return = AgGrid(red_totals, go, update_mode = GridUpdateMode.FILTERING_CHANGED, data_return_mode = DataReturnMode.FILTERED_AND_SORTED)