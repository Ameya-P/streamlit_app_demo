from PIL import Image
import streamlit as st

logo = Image.open("resources/berkeley_logo.png")

st.set_page_config(
    page_title="Voluntary Registry Offsets Database",
    page_icon=logo,
)

#-------------------- Intro
st.title("Voluntary Registry Offsets Database")

st.markdown(":blue[Berkeley Carbon Trading Project's] Voluntary Registry Offsets Database contains all carbon offset projects listed globally by four major voluntary offset project registries: American Carbon Registry (ACR), Climate Action Reserve (CAR), Gold Standard, and Verra (VCS). These four registries generate almost all of the world's voluntary market offsets and include projects eligible for use under the California, Quebec, and Washington lcap-and-trade programs as well as UN Clean Development Mechanism projects that transitioned into one of the voluntary registries.")

st.markdown("This database is formatted for Excel. If opened in Google Sheets, we recommend downloading it as an Excel workbook.")

st.markdown("Version 11 contains all projects, issuances, and retirements through March 31, 2024.")

creative_common_url = "https://creativecommons.org/licenses/by-sa/4.0/"
st.markdown("Released under [Creative Commons Attribution (CC BY-SA 4.0) license](%s).  If you wish to use, adapt, or reference this material, please cite as:" % creative_common_url)

st.markdown("*Barbara K. Haya, Aline Abayo, Ivy S. So, Micah Elias. (2024, May). Voluntary Registry Offsets Database v11, Berkeley Carbon Trading Project, University of California, Berkeley. Retrieved from:* [*https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database*](https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database)")

st.markdown("To download the database, sign up to receive update notices, provide suggestions, and let us know about data corrections, please visit:")

database_url = "https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database"
st.markdown("[https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database](%s)" % database_url)

st.divider()

#-------------------- Database Tabs
st.header("DATABASE TABS")

db_tab1, db_tab2, db_tab3, db_tab4, db_tab5 = st.tabs(["Projects", "Charts", "Map", "Table", "Credits by Vintage"])

#--- Tab 1
db_tab1.subheader("Projects Tab")

db_tab1.markdown("Lists all projects in all registries and can be filtered/sorted using drop-down menus. Filtered results are simultaneously viewable on the *Charts* and *Map* tabs.")

db_tab1.markdown('''* Black font indicates data directly sourced from the registries; blue font indicates information and data calculated/added by the Berkeley Carbon Trading Project.
* Each offset credit nominally represents one metric tonne of CO2-equivalent reduced or removed from the atmosphere.
* To clear all filters, click on the 'Data' menu and in the 'Sort & Filter' window, click 'Clear'. 
''')

vrod_url = "https://gspp.berkeley.edu/assets/uploads/page/VROD-Calculations.pdf"
db_tab1.markdown(":blue[All of our calculations are described in [VROD Calculations, linked here].](%s)" %vrod_url)

#--- Tab 2
db_tab2.subheader("Charts Tab")

db_tab2.markdown("View dynamic charts — use the column filters in *PROJECTS* tab to display filter results in the charts.")

#--- Tab 3
db_tab3.subheader("Map Tab")

db_tab3.markdown("View the distribution of projects around the world by number of projects and by credits issued. Use the column filters in *PROJECTS* tab to display filter results upon this map.")

#--- Tab 4
db_tab4.subheader("Table Tab")

db_tab4.markdown("Tallies projects, credits issued, and credits remaining by scope and type. Filter using the drop-down menus. Double click on any number to create a new tab with full information on all projects included in that row.")

#--- Tab 5
db_tab5.subheader("Credits by Vintage Tab")

db_tab5.markdown("Dynamic generator allows comprehensive view of all credits issued, retired, and remaining by vintage for any project. Simply select a Project ID from the drop-down menu and project data & details will populate.")

st.divider()

#-------------------- Registry Data
st.header("REGISTRY DATA")

zip_url = "https://gspp.berkeley.edu/research-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database"
st.markdown("[Downloaded the registry files we used to built this database: VROD-v11-RegistryFiles.zip](%s)" %zip_url)

st.divider()

#-------------------- More Information
st.header("MORE INFORMATION")

calc_url = "https://gspp.berkeley.edu/assets/uploads/page/VROD-Calculations.pdf"
st.markdown("[Detailed Description of Calculations](%s)" %calc_url)

cl_url = "https://gspp.berkeley.edu/assets/uploads/page/Change-Log--Voluntary-Registry-Offsets-Database.pdf"
st.markdown("[Change Log, v11](%s)" %cl_url)

type_url = "https://gspp.berkeley.edu/assets/uploads/page/VROD-ScopesTypes-v11.pdf"
st.markdown("[Project Scopes & Type Descriptions](%s)" %type_url)

vrod_db_url = "https://gspp.berkeley.edu/research-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database"
st.markdown("[Voluntary Registry Offsets Database webpage](%s)" %vrod_db_url)

bctp_url = "https://gspp.berkeley.edu/research-and-impact/centers/cepp/projects/berkeley-carbon-trading-project"
st.markdown("[Berkeley Carbon Trading Project](%s)" %bctp_url)

st.text("") #Spacer
st.text("") #Spacer

#--- Registry Tabs
st.subheader("REGISTRY DATA AND PROJECT DOCUMENTS")

r_tab1, r_tab2, r_tab3, r_tab4, r_tab5, r_tab6, r_tab7 = st.tabs(["ACR", "CAR", "GS", "VCS", "ARB", "WA","CDM"])

#--- Tab 1
r_tab1.subheader("American Carbon Registry (ACR)")

acr_registry_url = "https://americancarbonregistry.org/"
r_tab1.markdown("[Registry](%s)" %acr_registry_url)

acr_projects_url = "https://acr2.apx.com/myModule/rpt/myrpt.asp?r=111"
r_tab1.markdown("[Registered Projects](%s)" %acr_projects_url)

acr_issued_url = "https://acr2.apx.com/myModule/rpt/myrpt.asp?r=112"
r_tab1.markdown("[Credits Issued](%s)" %acr_issued_url)

acr_retired_url = "https://acr2.apx.com/myModule/rpt/myrpt.asp?r=206"
r_tab1.markdown("[Credits Retired](%s)" %acr_retired_url)

acr_cancelled_url = "https://acr2.apx.com/myModule/rpt/myrpt.asp?r=208"
r_tab1.markdown("[Credits Cancelled](%s)" %acr_cancelled_url)

acr_buffer_url = "https://acr2.apx.com/myModule/rpt/myrpt.asp?r=209"
r_tab1.markdown("[Buffer Pool](%s)" %acr_buffer_url)

acr_status_url = "https://acr2.apx.com/myModule/rpt/myrpt.asp?r=309"
r_tab1.markdown("[Credit Status](%s)" %acr_status_url)

acr_methods_url = "https://acrcarbon.org/methodologies/approved-methodologies/"
r_tab1.markdown("[Methodologies/Protocols](%s)" %acr_methods_url)

#--- Tab 2
r_tab2.subheader("Climate Action Reserve (CAR)")

car_registry_url = "https://www.climateactionreserve.org/"
r_tab2.markdown("[Registry](%s)" %car_registry_url)

car_projects_url = "https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=111"
r_tab2.markdown("[Registered Projects](%s)" %car_projects_url)

car_issued_url = "https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=112"
r_tab2.markdown("[Credits Issued](%s)" %car_issued_url)

car_retired_url = "https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=206"
r_tab2.markdown("[Credits Retired](%s)" %car_retired_url)

car_cancelled_url = "https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=308"
r_tab2.markdown("[Credits Cancelled](%s)" %car_cancelled_url)

car_buffer_url = "https://thereserve2.apx.com/myModule/rpt/myrpt.asp?r=706"
r_tab2.markdown("[Buffer Pool](%s)" %car_buffer_url)

car_methods_url = "https://www.climateactionreserve.org/how/protocols/"
r_tab2.markdown("[Methodologies/Protocols](%s)" %car_methods_url)

#--- Tab 3
r_tab3.subheader("Gold Standard (GS)")

gs_registry_url = "https://www.goldstandard.org/"
r_tab3.markdown("[Registry](%s)" %gs_registry_url)

gs_projects_url = "https://registry.goldstandard.org/projects?q=&page=1"
r_tab3.markdown("[Registered Projects](%s)" %gs_projects_url)

gs_issued_url = "https://registry.goldstandard.org/credit-blocks?q=&page=1"
r_tab3.markdown("[Credits Issued & Retired](%s)" %gs_issued_url)

gs_methods_url = "https://globalgoals.goldstandard.org/"
r_tab3.markdown("[Methodologies/Protocols](%s)" %gs_methods_url)

#--- Tab 4
r_tab4.subheader("Verified Carbon Standard (VCS)")

vcs_registry_url = "https://registry.verra.org/"
r_tab4.markdown("[Registry & Projects](%s)" %vcs_registry_url)

vcs_credits_url = "https://registry.verra.org/app/search/VCS"
r_tab4.markdown("[Credits Issued & Retired](%s)" %vcs_credits_url)

vcs_buffer_url = "https://registry.verra.org/app/search/VCS/All%20Projects"
r_tab4.markdown("[Buffer Pool](%s)" %vcs_buffer_url)

vcs_methods_url = "https://verra.org/methodologies-main/"
r_tab4.markdown("[VCS Methodologies](%s)" %vcs_methods_url)

vcs_cdm_url = "https://cdm.unfccc.int/methodologies/index.html"
r_tab4.markdown("[CDM Methodologies](%s)" %vcs_cdm_url)

#--- Tab 5
r_tab5.subheader("California Air Resources Board (ARB)")

arb_registry_url = "https://ww2.arb.ca.gov/our-work/programs/compliance-offset-program"
r_tab5.markdown("[Registry](%s)" %arb_registry_url)

arb_credits_url = "https://ww2.arb.ca.gov/resources/documents/arb-offset-credit-issuance-table"
r_tab5.markdown("[Credits Issued & Retired](%s)" %arb_credits_url)

arb_protocols_url = "https://ww2.arb.ca.gov/our-work/programs/compliance-offset-program/compliance-offset-protocols"
r_tab5.markdown("[Protocols](%s)" %arb_protocols_url)

#--- Tab 6
r_tab6.subheader("Washington State Climate Commitment Act (WA)")

wa_registry_url = "https://ecology.wa.gov/Air-Climate/Climate-Commitment-Act/Cap-and-invest/Offsets"
r_tab6.markdown("[Registry](%s)" %wa_registry_url)

wa_credits_url = "https://apps.ecology.wa.gov/publications/documents/2314026.pdf"
r_tab6.markdown("[Credits Issued](%s)" %wa_credits_url)

#--- Tab 7
r_tab7.subheader("UN's Clean Development Mechanism (CDM)")

r_tab7.markdown("Projects and credits issued under the :blue[UN's Clean Development Mechanism (CDM)] are only included in this voluntary registry offsets database if they have been transitioned to one of the voluntary registries.")

un_url = "https://cdm.unfccc.int/"
r_tab7.markdown("CDM projects can be found at the [UN's CDM website](%s)." %un_url)

unep_url = "http://www.cdmpipeline.org/"
r_tab7.markdown("CDM projects can also be found in the [UNEP's CDM Pipeline Database](%s)." %unep_url)

cdm_url = "https://cdm.unfccc.int/methodologies/index.html"
r_tab7.markdown("Some projects registered by voluntary registries use [CDM methodologies](%s). (These methodologies can be found with an online search for their name or ID.)" %cdm_url)


st.text("") #Spacer
st.text("") #Spacer

#--- Project Documents
st.subheader("PROJECT DOCUMENTS")

st.markdown('''You can view all project documents by visiting the project links above and searching for the project ID or name (you may need to scroll right and look for the search box).

**Main types of project documents:**

* **Project Listing Document** - indicates the intent to register a project under a registry and contains a draft of information in the PDD.
* **Project Design Document (PDD) / Project Description / Initial OPDR** - describes the project and its history, how it meets the eligibility requirements of the methodology, the calculations that will be used to estimate emissions reductions including definition of the baseline and the monitoring plan. Follows the requirements of the particular methodology and can have appendixes.
* **Validation Report** - approved third-party verifiers certify that the project meets the eligibility requirements of the methodology, and that the emissions/removals calculation and monitoring plan meet the requirements of the methodology. Sometimes, validation is performed in combination with the first verification.
* **Monitoring Report (also called OPDR)** - presents all monitored data and emission reduction/removals calculations on which credits are issued (often annually).
* **Verification Report** - third-party verifiers review the monitoring report, verifying that the data and calculations are correct and follow the requirements of the methodology. Registries issue credits based on the monitoring and verification reports. Verification reports can include project descriptions and other project details.
* **Methodology (also called Protocol)** - defines the eligibility, emissions calculations, and monitoring requirements for specific project types to generate offset credits.
''')

st.markdown("*We wholeheartedly thank the UC Berkeley students who helped write the Python code to build this database from the downloaded registry data: **Riyya Ahmed, Raaed Kamran Muggo, Ameya Patkar, Xinyun Rong**.*")

st.markdown("*Version 11*")