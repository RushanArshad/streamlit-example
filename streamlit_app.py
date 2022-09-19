import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

st.title("EDA for ReThink Data by Rushan Arshad")

data_front = pd.read_excel('Data Summary.xlsx', sheet_name = 'Data-Front End efficiency')
data_till = pd.read_excel('Data Summary.xlsx', sheet_name = 'Data-Till Activity Study')

data_front = data_front.astype(str)

st.dataframe(data_front)



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
    theme="streamlit", #Add theme color to the table
    enable_enterprise_modules=True,
    height=350, 
    width='100%',
    reload_data=True
)

data_front = grid_response['data']
selected = grid_response['selected_rows'] 
df = pd.DataFrame(selected)

#time_spent = data_front.groupby(["Location"]).BMS.sum().reset_index()
#a1 = data_front["Location"]
#a2 = data_front["BMS"].sum()
#char_df= pd.DataFrame(a1,a2)
#st.line_chart(selected)

if st.button("Generate Bar Chart"):
    st.bar_chart(data_till)
if st.button(" Generate Line Chart"):
    st.line_chart(data=data_till, x='Location', y='BMs_per_UOM', width=0, height=0, use_container_width=True)
if st.button("Generate Area"):
    st.area_chart(data=data_till, x='Location', y='BMs_per_UOM', width=0, height=0, use_container_width=True)
