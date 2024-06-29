import requests
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import streamlit as st
import source
from source import Root


try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e)
else:
    root = Root.model_validate_json(data_str)
    data = root.model_dump()
    areas:list[str] = list(set(map(lambda value:value['行政區'],data)))

    #定義callback的function
    def area_change():
        st.write(st.session_state.sarea)

    #設定初始值
    if 'sarea' not in st.session_state:
        st.session_state.sarea = "淡水區"
        area_change()

    #設定key值供session使用
    with st.sidebar:
        st.selectbox(":orange[請選擇行政區域:]",options=areas,on_change=area_change,key='sarea')
    
    st.write(st.session_state)

    