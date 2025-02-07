import numpy as np
import pandas as pd
import streamlit as st

st.title("Demo Title")
st.write("Demo Content")

st.write("")
st.write("Data Chart is Created Using Pandas: ")
data = pd.DataFrame({
    'A': ['Apple', 'And'],
    'B': ['Ball', 'Balloon']
})
st.write(data)

st.write("")
st.write("Numbers are Randomly Generated and Stored in the Matrix of 3x5: ")
chart_data = np.random.randn(3, 5)
st.write(chart_data)

st.line_chart(chart_data)