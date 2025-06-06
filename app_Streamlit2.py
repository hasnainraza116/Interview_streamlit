import streamlit as st

prompt = st.text_input("Type your message here" , max_chars=50)
if prompt:
    st.write(f"User message : {prompt}")
 