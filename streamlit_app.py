import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

st.title("EDA for ReThink Data by Rushan Arshad")

data_front = pd.read_excel('Data Summary.xlsx', sheet_name = 'Data-Front End efficiency')
data_till = pd.read_excel('Data Summary.xlsx', sheet_name = 'Data-Till Activity Study')

st.dataframe(data_front)
