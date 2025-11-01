import streamlit as st

st.set_page_config(page_title="LinkedIn Post Generator", layout="wide")

st.title("🚀 Elevate Your LinkedIn Presence")
st.write("Welcome! This app helps you generate engaging LinkedIn posts that attract HRs and professionals.")

user_input = st.text_area("Write a few details about your achievement or experience:")
if st.button("Generate Post"):
    st.success(f"✨ Here's your polished LinkedIn post:\n\nProud to share that {user_input}. Grateful for this journey and excited for what’s next!")
