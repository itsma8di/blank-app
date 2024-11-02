##########################################################
# to run: streamlit run main.py
##########################################################
import plotly.express as px
import streamlit as st
import pandas as pd
import requests

# labels
labels = requests.get("https://blank-app-h4ahyp7v1fh.streamlit.app/api/labels").json()
selector = st.multiselect("Select WELL:", labels)

# load data
data = pd.read_json(
    requests.get("https://blank-app-h4ahyp7v1fh.streamlit.app/api/data", params={"selector": selector}).json()
)

# setup figure
fig = px.scatter(
    x=data["PHIND"],
    y=data["GR"],
)
st.write(fig)