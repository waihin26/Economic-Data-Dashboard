import streamlit as st
import numpy as np
import pandas as pd
from data_fetcher.fred import continued_claims

st.set_page_config(page_title="Data Panel", page_icon="📈")

st.markdown("# Data Panel")
st.sidebar.header("Data Panel")
##################################################choose data you want to see
option = st.selectbox(
    "Choose data you want to see",
    ('data1','data2','Continued Claims'),
)
##################################################introduction for this data
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)
##############################################
col1, col2,col3,col4 = st.columns(4)

with col1:
    start_date = st.date_input("Start", value=None)
with col2:
    end_date = st.date_input("End", value=None)
with col3:
    st.empty()
with col4:
    st.empty()

if option=='data1':
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    if "ma" not in st.session_state:
        # set the initial default value of the slider widget
        st.session_state.ma = 1
    chart_data=chart_data.rolling(st.session_state.ma).mean()
    chart = st.line_chart(chart_data)

    ma = st.slider("Moving Average", 1, 8, step=2,key='ma')

elif option=='Continued Claims':
    chart_data = continued_claims(start_date, end_date)
    if "ma" not in st.session_state:
        # set the initial default value of the slider widget
        st.session_state.ma = 1
    chart_data=chart_data.rolling(st.session_state.ma).mean()
    chart = st.line_chart(chart_data)

    ma = st.slider("Moving Average", 1, 8, step=2,key='ma')
