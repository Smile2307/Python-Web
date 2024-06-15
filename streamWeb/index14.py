import streamlit as st

st.title("計數器範例")

#只會執行1次
if 'count' not in st.session_state:
    st.session_state.count = 0
#利用session_state的寫法
increment = st.button("Increment",key='Increment')
#檢查session_state的內容
st.session_state
if increment:
    st.session_state.count += 1

st.write("Count=", st.session_state.count)