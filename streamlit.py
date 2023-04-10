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
      "account"   : "ZX16444",
      "user"      : "malakamboj",
      "password"  : "Rupashi@20",
      "role"      : "ACCOUNTADMIN",
      "warehouse" : "COMPUTE_WH",
      "database"  : "TESTBYMALA",
      "schema"    : "Public"
    }
    session = Session.builder.configs(connection_parameters).create()
    return session

# Add header and a subheader
st.header("IDR : First Demo")
st.subheader("Central Data FOR IDR")
  
# Create Snowpark DataFrames that loads data from Knoema: Environmental Data Atlas
def load_data(session):
  with st.form("update_report"):
    comment_txt = st.text_area('Report comment:')
    comment_dt = st.date_input('Date of report:')
    sub_comment = st.form_submit_button('Submit')

# STEP 4 : WRITE THAT TO A TABLE IN SNOWFLAKE
if sub_comment:
        session.sql(f"""INSERT INTO DB.SCHEMA.TABLE (DATE, USER, COMMENT) 
    VALUES ('{comment_dt}', CURRENT_USER(), '{comment_txt}')""").collect()
        st.success('Success!', icon="✅")

# STEP 5 : PRESENT THE TABLE IN THE APP
q_comments = f"""SELECT * FROM DB.SCHEMA.TABLE ORDER BY 1 desc LIMIT 10"""
df_comments = session.sql(q_comments).to_pandas()
st.dataframe(df_comments, use_container_width=True)

if __name__ == "__main__":
    session = create_session_object()
    load_data(session)
