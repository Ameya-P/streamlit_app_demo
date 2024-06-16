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

st.markdown("This database is formatted for Excel. If opened in Google Sheets, we recommend downloading it as an Excel workbook.")

st.markdown("Version 11 contains all projects, issuances, and retirements through March 31, 2024.")

creative_common_url = "https://creativecommons.org/licenses/by-sa/4.0/"
st.markdown("Released under [Creative Commons Attribution (CC BY-SA 4.0) license](%s).  If you wish to use, adapt, or reference this material, please cite as:" % creative_common_url)

st.markdown("*Barbara K. Haya, Aline Abayo, Ivy S. So, Micah Elias. (2024, May). Voluntary Registry Offsets Database v11, Berkeley Carbon Trading Project, University of California, Berkeley. Retrieved from:* [*https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database*](https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database)")

st.markdown("To download the database, sign up to receive update notices, provide suggestions, and let us know about data corrections, please visit:")

database_url = "https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database"
st.markdown("[https://gspp.berkeley.edu/faculty-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database](%s)" % database_url)

#--------------------
st.header("DATABASE TABS")

st.subheader("PROJECTS tab")

st.markdown("Lists all projects in all registries and can be filtered/sorted using drop-down menus. Filtered results are simultaneously viewable on the Charts and Map tabs.")

st.markdown('''* Black font indicates data directly sourced from the registries; blue font indicates information and data calculated/added by the Berkeley Carbon Trading Project.
* Each offset credit nominally represents one metric tonne of CO2-equivalent reduced or removed from the atmosphere.
* To clear all filters, click on the 'Data' menu and in the 'Sort & Filter' window, click 'Clear'. 
''')

vrod_url = "https://gspp.berkeley.edu/assets/uploads/page/VROD-Calculations.pdf"
st.markdown(":blue[All of our calculations are described in [VROD Calculations, linked here].](%s)" %vrod_url)

st.subheader("CHARTS tab")

st.markdown("View dynamic charts — use the column filters in PROJECTS tab to display filter results in the charts.")

st.subheader("MAP tab")

st.markdown("View the distribution of projects around the world by number of projects and by credits issued. Use the column filters in PROJECTS tab to display filter results upon this map.")

st.subheader("TABLE tab")

st.markdown("Tallies projects, credits issued, and credits remaining by scope and type. Filter using the drop-down menus. Double click on any number to create a new tab with full information on all projects included in that row.")

st.subheader("CREDITS BY VINTAGE tab")

st.markdown("Dynamic generator allows comprehensive view of all credits issued, retired, and remaining by vintage for any project. Simply select a Project ID from the drop-down menu and project data & details will populate.")

#--------------------
st.header("REGISTRY DATA")

zip_url = "https://gspp.berkeley.edu/research-and-impact/centers/cepp/projects/berkeley-carbon-trading-project/offsets-database"
st.markdown("[Downloaded the registry files we used to built this database: VROD-v11-RegistryFiles.zip](%s)" %zip_url)

#--------------------
st.header("MORE INFORMATION")

st.subheader("*Registry data and project documents:*")

st.subheader("American Carbon Registry (ACR)")

st.subheader("Climate Action Reserve (CAR)")

st.subheader("Gold Standard (GS)")

st.subheader("Verified Carbon Standard (VCS)")
vcs_registry_url = 
st.markdown("[Registry](%s)" %vcs_registry_url)

vcs_credits_url = 
st.markdown("[Credits Issued & Retired](%s)" %vcs_credits_url)

vcs_protocols_url = 
st.markdown("[Protocols](%s)" %vcs_protocols_url)

st.subheader("California Air Resources Board (ARB)")
arb_registry_url = "https://ww2.arb.ca.gov/our-work/programs/compliance-offset-program"
st.markdown("[Registry](%s)" %arb_registry_url)

arb_credits_url = "https://ww2.arb.ca.gov/resources/documents/arb-offset-credit-issuance-table"
st.markdown("[Credits Issued & Retired](%s)" %arb_credits_url)

arb_protocols_url = "https://ww2.arb.ca.gov/our-work/programs/compliance-offset-program/compliance-offset-protocols"
st.markdown("[Protocols](%s)" %arb_protocols_url)

st.subheader("Washington State Climate Commitment Act (WA)")

wa_registry_url = "https://ecology.wa.gov/Air-Climate/Climate-Commitment-Act/Cap-and-invest/Offsets"
st.markdown("[Registry](%s)" %wa_registry_url)

wa_credits_url = "https://apps.ecology.wa.gov/publications/documents/2314026.pdf"
st.markdown("[Credits Issued](%s)" %wa_credits_url)

st.markdown("Projects and credits issued under the **UN's Clean Development Mechanism (CDM)** are only included in this voluntary registry offsets database if they have been transitioned to one of the voluntary registries.")

un_url = "https://cdm.unfccc.int/"
st.markdown("CDM projects can be found at the [UN's CDM website](%s)." %un_url)

unep_url = "http://www.cdmpipeline.org/"
st.markdown("CDM projects can also be found in the [UNEP's CDM Pipeline Database](%s)." %unep_url)

cdm_url = "https://cdm.unfccc.int/methodologies/index.html"
st.markdown("Some projects registered by voluntary registries use [CDM methodologies](%s). (These methodologies can be found with an online search for their name or ID.)" %cdm_url)


st.subheader("Project Documents:")

st.markdown('''You can view all project documents by visiting the project links above and searching for the project ID or name (you may need to scroll right and look for the search box).

**Main types of project documents:**

* **Project Listing Document** - indicates the intent to register a project under a registry and contains a draft of information in the PDD.
* **Project Design Document (PDD) / Project Description / Initial OPDR** - describes the project and its history, how it meets the eligibility requirements of the methodology, the calculations that will be used to estimate emissions reductions including definition of the baseline and the monitoring plan. Follows the requirements of the particular methodology and can have appendixes.
* **Validation Report** - approved third-party verifiers certify that the project meets the eligibility requirements of the methodology, and that the emissions/removals calculation and monitoring plan meet the requirements of the methodology. Sometimes, validation is performed in combination with the first verification.
* **Monitoring Report (also called OPDR)** - presents all monitored data and emission reduction/removals calculations on which credits are issued (often annually).
* **Verification Report** - third-party verifiers review the monitoring report, verifying that the data and calculations are correct and follow the requirements of the methodology. Registries issue credits based on the monitoring and verification reports. Verification reports can include project descriptions and other project details.
* **Methodology (also called Protocol)** - defines the eligibility, emissions calculations, and monitoring requirements for specific project types to generate offset credits.
''')

st.markdown("We wholeheartedly thank the UC Berkeley students who helped write the Python code to build this database from the downloaded registry data: Riyya Ahmed, Raaed Kamran Muggo, Ameya Patkar, Xinyun Rong.")

st.markdown("Version 11")