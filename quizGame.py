import time
import streamlit as st

list = {
  "ans1Temp": "Test",
}

stss = st.session_state
st.markdown("# :green[***:material/Timer: Challenge Quiz Game***]")
st.write("*เกมที่คุณต้องเขียนโค้ดให้ทันภายในเวลา*")
st.divider()

ans1Temp = ""
ans2Temp = ""
ans3Temp = ""
ans4Temp = ""
