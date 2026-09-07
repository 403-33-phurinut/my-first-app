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

from code_editor import code_editor

st.title("Streamlit Editable Code Editor")

# Initial code snippet to display inside the editor
initial_code = """def greet(name):
    print(f"Hello, {name}!")

greet("Streamlit User")
"""

# Render the editable code block
# Setting a fixed 'key' prevents the component from flashing/re-rendering on app updates
response = code_editor(
    initial_code, 
    lang="python", 
    key="my_code_editor"
)

# Extract and display the modified code from the response dictionary
if response and response.get("text"):
    edited_code = response["text"]
    
    st.subheader("Live Output / Captured Code:")
    st.code(edited_code, language="python")
