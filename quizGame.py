import time
import streamlit as st

stss = st.session_state
st.markdown("# :green[***:material/Timer: Challenge Quiz Game***]")
st.write("*เกมที่คุณเลือกโค้ดที่ใช้งานได้ให้ทันภายในเวลา*")
st.divider()

if "ans1_val" not in stss:
    stss.ans1_val = ""
if "ans2_val" not in stss:
    stss.ans2_val = ""
if "ans3_val" not in stss:
    stss.ans3_val = ""
if "ans4_val" not in stss:
    stss.ans4_val = ""

def reset_game():
    stss.ans1_val = "" 
    stss.ans2_val = ""  
    stss.ans3_val = "" 
    stss.ans4_val = ""
    stss.start = time.time()  
    stss.is_ended = False  
    
@st.dialog(":material/bar_chart: สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    if u_ans1 == 1:
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
        st.balloons()
    else:
        st.error(":material/close: คุณแพ้!")
        st.write(f"ได้ {score}/4 คะแนน")

st.button(":material/sports_esports: เริ่มเล่นเกม", on_click=reset_game)

if "start" in stss and not stss.get("is_ended", False):
    time_left = int(30 - (time.time() - stss.start))

    if time_left > 0:
        st.error(f":material/Timer: เหลือเวลา: {time_left} วินาที")
    else:
        stss.is_ended = True
        st.rerun()

st.divider()

a1c1 = st.code('''text = string''')
a1c2 = st.code('''text = "string"''')
a1c3 = st.code('''text = [string]''')
a1c4 = st.code('''text = <string>''')

a2c1 = st.code('''num = 1''')
a2c2 = st.code('''num = 3.14''')
a2c3 = st.code('''num = "string"''')
a2c4 = st.code('''num = true''')

a3c1 = st.code('''float = 1''')
a3c2 = st.code('''float = 3.14''')
a3c3 = st.code('''float = "string"''')
a3c4 = st.code('''float = true''')

a4c1 = st.code('''def loop():
        print("Hello world!")''')
a4c2 = st.code('''def iterate(arg1,arg2):
        if arg1 >= arg2:
            return true''')
a4c3 = st.code('''loop == "string"''')
a4c4 = st.code('''for i in range(5):
        print("Hello world!")''')

ans1 = st.radio(
    "***1. ข้อใดคือ \"string\" ใน python***",
    [a1c1,a1c2,a1c3,a1c4],
    key=stss.ans1_val,
)
ans2 = st.radio(
    "***2. ข้อใดคือ \"interger\" ใน python***",
    [a2c1,a2c2,a2c3,a2c4],
    key=stss.ans2_val,
)
ans3 = st.radio(
    "***3. ข้อใดคือ \"float\" ใน python***",
    [a3c1,a3c2,a3c3,a3c4],
    key=stss.ans3_val,
)
ans4 = st.radio(
    "***4. ข้อใดคือ iteration ใน python***",
    [a4c1,a4c2,a4c3,a4c4],
    key=stss.ans4_val,
)
ans5 = st.radio(
    "***5. ข้อใดจะทำให้เกิด error ใน python***",
    key=stss.ans4_val,
)
ans6 = st.radio(
    "***6. ข้อใดไม่ใช่ภาษา python***",
    key=stss.ans4_val,
)

stss.ans1_val = ans1
stss.ans2_val = ans2
stss.ans3_val = ans3
stss.ans4_val = ans4

if "start" in stss and not stss.get("is_ended", False):
    if st.button(":material/upload: ส่งคำตอบ"):
        stss.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

if stss.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4)

st.divider()
st.caption("สร้างโดย")
st.markdown("นาย **ภูริณัฐ บ่อไทย** เลขที่ **33** ม.**4/3**")
