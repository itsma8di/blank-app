# ##########################################################
# # to run: streamlit run main.py
# ##########################################################
# import plotly.express as px
# import streamlit as st
# import pandas as pd
# import requests
# import os 


# # labels
# labels = requests.get("https://blank-app-h4ahyp7v1fh.streamlit.app/api/labels").json()
# selector = st.multiselect("Select WELL:", labels)

# # load data
# data = pd.read_json(
#     requests.get("https://blank-app-h4ahyp7v1fh.streamlit.app/api/data", params={"selector": selector}).json()
# )

# # setup figure
# fig = px.scatter(
#     x=data["PHIND"],
#     y=data["GR"],
# )
# st.write(fig)
from flask import Flask, render_template
import streamlit as st

app = Flask(__name__)
@app.route('/')
def index():
    return {"demo"}
@app.route('/streamlit')
def streamlit():
    st.set_page_config(page_title="My Streamlit App")
    st.write("Hello, world!")
if __name__ == '__main__':
    app.run(port=8000)