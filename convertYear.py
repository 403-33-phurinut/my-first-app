import streamlit as st
st.title("แอปพลิเคชั่นแปลง พ.ศ. เป็น ค.ศ.")

bhYear = st.number_input("กรอกปี พ.ศ.")
ceYear = st.number_input("กรอกปี ค.ศ.")
value = 543
if bhYear > 0:
  ceResult = bhYear - value
else:
  ceResult = "กรอกข้อมูล"

if ceYear > 0:
  bhResult = ceYear - value
else:
  bhResult = "กรอกข้อมูล"
  
st.subheader(f"ปี ค.ศ. คือ: {ceResult}")
st.subheader(f"ปี พ.ศ. คือ: {bhResult}")
