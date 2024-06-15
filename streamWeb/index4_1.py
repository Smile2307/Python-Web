import streamlit as st
import time

placeholder = st.empty()

with placeholder:
    for seconds in range(60):
        st.write(f"{seconds} seconds have passed")
        time.sleep(1)

    st.write("😜 1 minute over!")

time.sleep(5)
placeholder.empty()