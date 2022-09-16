import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

st.title("EDA for ReThink Data by Rushan Arshad")

data_front = pd.read_excel('Data Summary.xlsx', sheet_name = 'Data-Front End efficiency')
data_till = pd.read_excel('Data Summary.xlsx', sheet_name = 'Data-Till Activity Study')

data_front = data_front.astype(str)

st.dataframe(data_front)

time_spent = data_front.groupby(["Location", "BMS"])
st.dataframe(time_spent)
st.line_chart(time_spent)
