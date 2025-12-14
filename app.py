import streamlit as st
from resume_matcher import calculate_match

st.set_page_config(page_title="AI Resume Screening System")

st.title("📄 AI Resume Screening System")

resume_text = st.text_area("Paste Resume Text")
job_text = st.text_area("Paste Job Description")

if st.button("Match Resume"):
    if resume_text and job_text:
        score = calculate_match(resume_text, job_text)
        st.success(f"Resume Match Score: {score}%")
    else:
        st.warning("Please paste both Resume and Job Description")
