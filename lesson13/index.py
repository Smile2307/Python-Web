import streamlit as st

st.subheader("BMI計算")

#畫線
st.divider()

#latex可使用數學公式
st.latex('BMI值計算公式:BMI = 體重(公斤) / 身高^2(公尺^2)')
st.latex('例如：一個52公斤的人，身高是155公分，則BMI為:')

#說明_使用html、css及markdown語法
st.markdown('''
<h6 style="color:blue;text-align:center">52(公斤) / 1.552 ( 公尺<sup>2</sup> ) = 21.6</h6>
<h6 style="color:orange;text-align:center">體重正常範圍為 BMI = 18.5～24</h6>
<hr style="border:0;margin:0 auto;width:80%;border-top:2px dotted blue">
<h6 style="color:purple;text-align:center">快看看自己的BMI是否在理想範圍吧!</h6>
''', unsafe_allow_html=True)

#使用form
with st.form("BMI...",border=0):

    height = st.slider(":green[選擇身高(cm)]",max_value=250,min_value=100,key='height')
    weight = st.number_input(":green[選擇體重(kg)]",max_value=200,min_value=30,key='weight')
    
    col1,col2 = st.columns(2)


    #st.session_state
    with col1:

        #使用session state
        if st.form_submit_button("BMI計算"):

            bmi_result = round( weight / ((height/100) ** 2),1 )
            
            if bmi_result < 18.5:
                txt = "體重過輕"
            elif bmi_result < 24:
                txt = "正常範圍"
            elif bmi_result < 27:
                txt = "過重"
            elif bmi_result < 30:
                txt = "輕度肥胖"
            elif bmi_result < 35:
                txt = "中度肥胖"
            else:
                txt = "重度肥胖"
            
            st.session_state.bmi = f"您的BMI:{bmi_result}, 體重:{txt}"

            st.markdown(f"## :orange[{st.session_state.bmi}]")

col1, col2, col3 = st.columns(3)
with col1:
   st.text("")

with col2:
   st.text("身體質量指數(BMI)(kg/m2)")

with col3:
   st.text("腰圍(cm)")

bmiInfo = ["體重過輕","BMI ＜ 18.5","-","正常範圍","18.5 ≦ BMI＜24","-", "異常範圍", "過重：24≦BMI＜27 \n輕度肥胖：27≦BMI＜30 \n中度肥胖：30≦BMI＜35 \n重度肥胖：BMI≧35", "男性：≧90公分 \n女性：≧80公分", ""]

i=0
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)

for col in row1 + row2 + row3:
    if i > 5:
        tile = col.container(height=120, border=1)
        tile.text(bmiInfo[i])
    else:
        tile = col.container(height=55, border=1)
        tile.text(bmiInfo[i])
    i += 1


