import streamlit as st
import numpy as np

with st.container(border=True):
    st.write("this is inside the container")
    st.bar_chart(np.random.randn(50,3))

st.write("this is outside the container")