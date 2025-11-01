import streamlit as st
from transformers import pipeline

# ---- App setup ----
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="💼", layout="centered")

st.title("💼 Elevate Your LinkedIn Posts")
st.markdown("Transform your ideas into **professional, engaging LinkedIn posts** using AI with the right tone, emojis, and hashtags.")

# ---- Input fields ----
context = st.text_area("✍️ Write a short idea or update you'd like to post:", 
                       placeholder="e.g. Completed my internship at Purview India Consulting & Services LLP...")

tone = st.selectbox("Choose a tone:", ["Professional", "Inspirational", "Grateful", "Celebratory", "Humblebrag"])

include_hashtags = st.checkbox("Add relevant hashtags automatically", value=True)
include_emojis = st.checkbox("Add emojis for better engagement", value=True)

st.markdown("---")

# ---- Generate post ----
if st.button("✨ Generate LinkedIn Post"):
    if not context.strip():
        st.warning("Please enter some context before generating.")
    else:
        with st.spinner("Crafting your perfect LinkedIn post..."):
            try:
                generator = pipeline("text-generation", model="tiiuae/falcon-7b-instruct")

                prompt = f"""
                You are a professional LinkedIn content creator.
                Write a detailed, engaging, and natural-sounding LinkedIn post.
                Context: {context}
                Tone: {tone}
                Add hashtags: {include_hashtags}
                Add emojis: {include_emojis}
                Ensure it's formatted in multiple short paragraphs with a positive closing line.
                """

                response = generator(prompt, max_length=300, do_sample=True, temperature=0.8)
                post = response[0]["generated_text"]

                # Trim unnecessary text if model repeats prompt
                if "Context:" in post:
                    post = post.split("Context:")[-1].strip()

                st.success("✅ Your LinkedIn post is ready!")
                st.text_area("📢 Generated Post:", value=post, height=250)
                st.download_button("⬇️ Download Post", data=post, file_name="linkedin_post.txt")

            except Exception as e:
                st.error(f"⚠️ Something went wrong: {e}")
