import streamlit as st
st.title("แอปพลิเคชั่นแปลง พ.ศ. เป็น ค.ศ.")
st.caption("มีการดัดแปลง")

value = 543
bhYear = int(st.number_input("กรอกปี พ.ศ.") - value)
ceYear = int(st.number_input("กรอกปี ค.ศ.") + value)
if bhYear > 0:
  ceResult = bhYear
elif bhYear <= 0:
  ceResult = f"ก่อนคริสต์ศักราช {abs(bhYear)} ปี"

if ceYear > 0:
  bhResult = ceYear
elif ceYear <= 0:
  bhResult = f"ก่อนพุทธศักราช {abs(ceYear)} ปี"
  
st.subheader(f"ปี ค.ศ. คือ: {ceResult}")
st.subheader(f"ปี พ.ศ. คือ: {bhResult}")
