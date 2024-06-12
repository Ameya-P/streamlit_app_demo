from PIL import Image
import streamlit as st

logo = Image.open("resources/berkeley_logo.png")

st.set_page_config(
    page_title="Voluntary Registry Offsets Database",
    page_icon=logo,
)

#--------------------
st.title("Voluntary Registry Offsets Database")

st.markdown(":blue[Berkeley Carbon Trading Project's] Voluntary Registry Offsets Database contains all carbon offset projects listed globally by four major voluntary offset project registries: American Carbon Registry (ACR), Climate Action Reserve (CAR), Gold Standard, and Verra (VCS). These four registries generate almost all of the world's voluntary market offsets and include projects eligible for use under the California, Quebec, and Washington lcap-and-trade programs as well as UN Clean Development Mechanism projects that transitioned into one of the voluntary registries.")

st.markdown("Version 11 contains all projects, issuances, and retirements through March 31, 2024.")

creative_common_url = "https://creativecommons.org/licenses/by-sa/4.0/"
st.markdown("Released under [Creative Commons Attribution (CC BY-SA 4.0) license](%s).  If you wish to use, adapt, or reference this material, please cite as:" % creative_common_url)

st.markdown("*Barbara K. Haya, Aline Abayo, Ivy S. So, Micah Elias. (2024, May). Voluntary Registry Offsets Database v11, Berkeley Carbon Trading Project, University of California, Berkeley. Retrieved from:* [*https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database*](https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database)")

st.markdown("To download the database, sign up to receive update notices, provide suggestions, and let us know about data corrections, please visit:")

database_url = "https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database"
st.markdown("[https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database](%s)" % database_url)

#--------------------
st.header("DATABASE TABS")

st.subheader("")

#--------------------
st.header("REGISTRY DATA")

#--------------------
st.header("MORE INFORMATION")

st.subheader("*Registry data and project documents:*")

st.subheader("American Carbon Registry (ACR)")

st.subheader("Climate Action Reserve (CAR)")

st.subheader("Gold Standard (GS)")

st.subheader("Verified Carbon Standard (VCS)")

st.subheader("California Air Resources Board (ARB)")

st.subheader("Washington State Climate Commitment Act (WA)")