# Snowpark
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import avg, sum, col,lit
import streamlit as st
import pandas as pd

st.set_page_config(
     page_title="Environment Data Atlas",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://developers.snowflake.com',
         'About': "This is an *extremely* cool app powered by Snowpark for Python, Streamlit, and Snowflake Data Marketplace"
     }
)

# Create Session object
def create_session_object():
    connection_parameters = {
      "account"   : "LJ22006.ap-south-1",
      "user"      : "malakamboj",
      "password"  : "Rupashi@20",
      "role"      : "ACCOUNTADMIN",
      "warehouse" : "COMPUTE_WH",
      "database"  : "TESTBYMALA",
      "schema"    : "PUBLIC"
    }
    session = Session.builder.configs(connection_parameters).create()
    return session

# Add header and a subheader
st.header("IDR : POC ")
st.subheader("Powered by Accenture@2023 | Made with Streamlit")
  
# Create Snowpark DataFrames that loads data from Knoema: Environmental Data Atlas
def load_data(session):    # CO2 Emissions by Country
   df = session.table("PERSON")
   edited = st.experimental_data_editor(df, use_container_width=True, num_rows="dynamic")
   session.write_pandas(edited, "ESG_SCORES_DEMO", overwrite=True)
   
 
if __name__ == "__main__":
    session = create_session_object()
    load_data(session)
  
