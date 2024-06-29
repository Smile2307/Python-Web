import requests
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import streamlit as st
#匯入modul的function
import source
#匯入modul的class
from source import Root



try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e)
else:
    root = Root.model_validate_json(data_str)
    data = root.model_dump()

    def ijk(value):
        return value['行政區']

    areas:list[str] = list(set(map(ijk,data)))

    option = st.selectbox("請選擇行政區",areas)
    st.write("您選擇:", option)