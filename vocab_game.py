import time
import streamlit as st

st.markdown("# :blue[***:material/Timer: เกมเติมศัพท์จับเวลา***]")
st.write("*เกมเติมศัพท์จับเวลาที่ให้คุณเติมคำตอบภายในเวลา*")
st.divider()

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

def reset_game():
    st.session_state.ans1_val = "" 
    st.session_state.ans2_val = ""  
    st.session_state.ans3_val = "" 
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()  
    st.session_state.is_ended = False  
    
@st.dialog(":material/bar_chart: สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    if u_ans1 == "apple":
        st.success(":material/check: ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f":material/close: ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")
        
    if u_ans2 == "fish":
        st.success(":material/check: ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f":material/close: ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    if u_ans3 == "boil":
        st.success(":material/check: ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f":material/close: ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")
        
    if u_ans4 == "melt":
        st.success(":material/check: ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f":material/close: ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    st.info(f":material/trophy: ได้คะแนนรวม: {score} คะแนน")

    if score >= 3:
        st.success(":material/award_star: คุณชนะ!")
        st.write(f"ได้ {score}/4 คะแนน")
    else:
        st.error(":material/close: คุณแพ้!")
        st.write(f"ได้ {score}/4 คะแนน")

st.button(":material/sports_esports: เริ่มเล่นเกม", on_click=reset_game)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f":material/Timer: เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. :material/nutrition",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. :material/set_meal:",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 4: In order to make a soup, you must `b _ _ _` the water. :material/water_drop:",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: `M _ _ _` the butter in the pan. :material/breakfast_dining:",
    value=st.session_state.ans4_val,
)

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button(":material/upload: ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2)

st.divider()
st.caption("สร้างโดย")
st.markdown("นาย **ภูริณัฐ บ่อไทย** เลขที่ **33** ม.**4/3**")
