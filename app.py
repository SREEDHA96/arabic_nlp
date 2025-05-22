import streamlit as st
import re

st.set_page_config(page_title="Arabic NLP Demo", layout="centered")

st.title("📘 Arabic NLP Demo")
st.write("Enter Arabic text to process it (tokenize and normalize).")

# Text input
arabic_text = st.text_area("✍️ Enter Arabic text:", height=150)

# Normalization function
def normalize_arabic(text):
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "و", text)
    text = re.sub("ئ", "ي", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("[ًٌٍَُِّْ]", "", text)
    return text

# Tokenization function
def tokenize(text):
    tokens = re.findall(r'\b\w+\b', text)
    return tokens

# Process button
if st.button("🔍 Process Text"):
    if arabic_text.strip():
        norm_text = normalize_arabic(arabic_text)
        tokens = tokenize(norm_text)

        st.subheader("✅ Normalized Text:")
        st.write(norm_text)

        st.subheader("🧩 Tokens:")
        st.write(tokens)
    else:
        st.warning("Please enter some Arabic text first.")
