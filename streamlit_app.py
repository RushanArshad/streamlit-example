import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

st.title("EDA for ReThink Data by Rushan Arshad")

data_front = pd.read_excel('Data Summary.xlsx', sheet_name = 'Data-Front End efficiency')
data_till = pd.read_excel('Data Summary.xlsx', sheet_name = 'Data-Till Activity Study')

data_front = data_front.astype(str)

st.dataframe(data_front)

AgGrid(data_front)

gb = GridOptionsBuilder.from_dataframe(data_front)
gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()

grid_response = AgGrid(
    data_front,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='STREAMLIT', #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    reload_data=True
)

data_front = grid_response['data']
selected = grid_response['selected_rows'] 
