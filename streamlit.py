
import streamlit
import requests
streamlit.title("My parents new healthy dinner")
streamlit.header("Breakfast Menu")
streamlit.text("Omega3 contains meal")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
