import streamlit as st

st.markdown("# :red[***:material/wc: คำนวณค่าดัชนีมวลกาย BMI***]")
st.write("*กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น*")
st.divider()

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):",min_value=0.0)
height = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):",min_value=0.0)

if st.button(":material/info: คำนวณ BMI"):
  hMeter = height/100
  bmi = weight/(hMeter**2)
  st.write(f"## ค่าดัชนีมวลกาย/BMI ของคุณคือ: ***{bmi:.2f} kg/m²***")
  
