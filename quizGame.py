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

st.button(":material/sports_esports: เริ่มเล่นเกม", on_click=reset_game)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f":material/Timer: เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()
