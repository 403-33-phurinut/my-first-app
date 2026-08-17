import streamlit as st

st.markdown("# :red[***:material/wc: คำนวณค่าดัชนีมวลกาย BMI***]")
st.write("*กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น*")
st.divider()

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):",min_value=0.0)
height = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):",min_value=0.0)

if st.button("**:material/info:** คำนวณ BMI"):
  hMeter = height/100
  bmi = weight/(hMeter**2)
  st.write(f"### ค่าดัชนีมวลกาย/BMI ของคุณคือ: ***{bmi:.2f} kg/m²***")

  if bmi < 18.5:
    st.badge("คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)",icon=:material/warning)
  elif 18.5 <= bmi < 23.0:
    st.badge("คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)",icon=:material/check)
  elif 23.0 <= bmi < 25.0:
    st.badge("คุณเริ่มมีน้ำหนักเกินเกณฑ์ (ท้วม)",icon=:material/warning)
  else:
    st.badge("คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย,icon=":material/dangerous)
st.divider()
st.write("นาย ภูริณัฐ บ่อไทย เลขที่ 33 ม.4/3")
