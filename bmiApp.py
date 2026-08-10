import streamlit as st

st.markdown("# :red[***:material/wc: คำนวณค่าดัชนีมวลกาย BMI***]")
st.divider()
st.write("*กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น*")

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):",min_value=0.0)
height = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):",min_value=0.0)
