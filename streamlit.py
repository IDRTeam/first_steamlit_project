
# STEP 1 : IMPORT PYTHON PACKAGES
import streamlit as st
from snowflake.snowpark.context import get_active_session

# STEP 2 : USE CURRENT SNOWFLAKE SESSION, NO NEED TO MANAGE CREDS!
 # Create Session object
def create_session_object():
    connection_parameters = {
      "account"   : "",
      "user"      : "",
      "password"  : "",
      "role"      : "",
      "warehouse" : "",
      "database"  : "KNOEMA_ENVIRONMENT_DATA_ATLAS",
      "schema"    : "ENVIRONMENT"
    }
    session = Session.builder.configs(connection_parameters).create()
    return session
# STEP 3 :  SET UP YOUR INPUT FORM
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
