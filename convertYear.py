import streamlit as st
st.title("แอปพลิเคชั่นแปลง พ.ศ. เป็น ค.ศ.")

bhYear = st.number_input("กรอกปี พ.ศ.")
ceYear = st.number_input("กรอกปี ค.ศ.")
value = 543
ceResult = bhYear - value
bhResult = ceYear + value
st.header(f"ปี ค.ศ. คือ: {ceResult}")
st.header(f"ปี พ.ศ. คือ: {bhResult}")
