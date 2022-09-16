import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

st.title("EDA for ReThink Data by Rushan Arshad")

data_front = pd.read_excel('Data Summary.xlsx', sheet_name = 'Data-Front End efficiency')
data_till = pd.read_excel('Data Summary.xlsx', sheet_name = 'Data-Till Activity Study')

data_front = data_front.astype(str)

st.dataframe(data_front.head())

time_spent = data_front.groupby(["Location"]).BMS.sum().reset_index()
AgGrid(data_front)
