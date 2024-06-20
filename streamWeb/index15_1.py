import streamlit as st

tab1, tab2 = st.tabs(["session_state", "call_back"])

with tab1:
    with st.form("my_form"):
        # 標題
        st.markdown('<h3 style="color:purple;text-align:center">BMI值計算(session_state)</h3>', unsafe_allow_html=True)

        # 初始化输入栏位值
        if 'weight' not in st.session_state:
            st.session_state.weight = 0.0
        if 'height' not in st.session_state:
            st.session_state.height = 0.0

        # 创建两列布局
        col1, col2, col3 = st.columns(3)

        # 体重输入栏在第一列
        with col1:
            weight = st.number_input("體重 (kg):", min_value=0.0, value=st.session_state.weight, step=0.1, key='weight_input')
            height = st.number_input("身高 (cm):", min_value=0.0, value=st.session_state.height, step=0.1, key='height_input')
            
        # 身高输入栏在第二列
        with col2:
            st.markdown('<br>', unsafe_allow_html=True)  # 确保换行
            BMI_CAL = st.form_submit_button("開始計算")
            st.markdown('<br>', unsafe_allow_html=True)  # 确保换行
            BMI_clear = st.form_submit_button("清除結果")
        with col3:
            # 当按下计算按钮时，检查输入值
            if BMI_CAL:
                if weight <= 0 or height <= 0:
                    st.error("輸入值不可為負值或零，請重新輸入。")
                else:
                    # 如果值有效，计算并显示BMI
                    bmi = weight / ((height / 100) ** 2)
                    if bmi < 18.5:
                        txt = "<font color=DarkBlue>**體重過輕**</font>"
                    elif bmi < 24:
                        txt = "<font color=green>**正常範圍**</font>"
                    elif bmi < 27:
                        txt = "<font color=red>**過重**</font>"
                    elif bmi < 30:
                        txt = "<font color=Fuchsia>**輕度肥胖**</font>"
                    elif bmi < 35:
                        txt = "<font color=DarkSalmon >**中度肥胖**</font>"
                    else:
                        txt = "<font color=BlueViolet>**重度肥胖**</font>"

                    st.markdown("<br><br>", unsafe_allow_html=True)
                    st.markdown(f"您的BMI值為: {bmi:.2f} <br> 體重: {txt}", unsafe_allow_html=True)

        


    # 当按下清除按钮时，清空输入栏并重新加载页面
    if BMI_clear:
        st.session_state.weight = 0.0
        st.session_state.height = 0.0
        #st.session_state['weight_input'] = 0.0
        #st.session_state['height_input'] = 0.0
        st.experimental_rerun()
        # 使用URL参数强制刷新页面
        st.query_params.clear()
        #st.experimental_set_query_params()

            



    # BMI分类表格
    st.markdown('''
    |  | 身體質量指數(BMI)(kg/m²) | 腰圍(cm)  |
    |-|-|-|
    | 體重過輕 | BMI ＜ 18.5 | -  |
    | 正常範圍 | 18.5 ≦ BMI ＜ 24 | -  |
    | 異常範圍 | 過重：24 ≦ BMI ＜ 27 <br>輕度肥胖：27 ≦ BMI ＜ 30 <br>中度肥胖：30 ≦ BMI ＜ 35 <br>重度肥胖：BMI ≧ 35 | 男性：≧90公分  <br>女性：≧80公分  |
    ''', unsafe_allow_html=True)

with tab2:
    with st.form("my_form2"):
        # 標題
        st.markdown('<h3 style="color:purple;text-align:center">BMI值計算(call_back)</h3>', unsafe_allow_html=True)

        # 初始化输入栏位值
        if 'weight' not in st.session_state:
            st.session_state.weight = 0.0
        if 'height' not in st.session_state:
            st.session_state.height = 0.0

        # 创建两列布局
        col1, col2, col3 = st.columns(3)

        # 体重输入栏在第一列
        with col1:
            weight = st.number_input("體重 (kg):", min_value=0.0, value=st.session_state.weight, step=0.1, key='weight_input')
            height = st.number_input("身高 (cm):", min_value=0.0, value=st.session_state.height, step=0.1, key='height_input')
            
        # 身高输入栏在第二列
        with col2:
            st.markdown('<br>', unsafe_allow_html=True)  # 确保换行
            BMI_CAL = st.form_submit_button("開始計算")
            st.markdown('<br>', unsafe_allow_html=True)  # 确保换行
            BMI_clear = st.form_submit_button("清除結果")
        with col3:
            # 当按下计算按钮时，检查输入值
            if BMI_CAL:
                if weight <= 0 or height <= 0:
                    st.error("輸入值不可為負值或零，請重新輸入。")
                else:
                    # 如果值有效，计算并显示BMI
                    bmi = weight / ((height / 100) ** 2)
                    if bmi < 18.5:
                        txt = "<font color=DarkBlue>**體重過輕**</font>"
                    elif bmi < 24:
                        txt = "<font color=green>**正常範圍**</font>"
                    elif bmi < 27:
                        txt = "<font color=red>**過重**</font>"
                    elif bmi < 30:
                        txt = "<font color=Fuchsia>**輕度肥胖**</font>"
                    elif bmi < 35:
                        txt = "<font color=DarkSalmon >**中度肥胖**</font>"
                    else:
                        txt = "<font color=BlueViolet>**重度肥胖**</font>"

                    st.markdown("<br><br>", unsafe_allow_html=True)
                    st.markdown(f"您的BMI值為: {bmi:.2f} <br> 體重: {txt}", unsafe_allow_html=True)

        


    # 当按下清除按钮时，清空输入栏并重新加载页面
    if BMI_clear:
        st.session_state.weight = 0.0
        st.session_state.height = 0.0
        #st.session_state['weight_input'] = 0.0
        #st.session_state['height_input'] = 0.0
        st.experimental_rerun()
        # 使用URL参数强制刷新页面
        st.query_params.clear()
        #st.experimental_set_query_params()

            



    # BMI分类表格
    st.markdown('''
    |  | 身體質量指數(BMI)(kg/m²) | 腰圍(cm)  |
    |-|-|-|
    | 體重過輕 | BMI ＜ 18.5 | -  |
    | 正常範圍 | 18.5 ≦ BMI ＜ 24 | -  |
    | 異常範圍 | 過重：24 ≦ BMI ＜ 27 <br>輕度肥胖：27 ≦ BMI ＜ 30 <br>中度肥胖：30 ≦ BMI ＜ 35 <br>重度肥胖：BMI ≧ 35 | 男性：≧90公分  <br>女性：≧80公分  |
    ''', unsafe_allow_html=True)
