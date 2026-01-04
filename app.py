import streamlit as st
import os
import sys
from PIL import Image
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modules.parser import parse_resume
from modules.ranker import rank_resumes

st.set_page_config(page_title="Syncro | Resume Screening", layout="centered")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background-color: #cce6ff; }
[data-testid="stHeader"] { background: none; }
h1, h2, h3, h4, p, label { text-align: center !important; }
</style>
""", unsafe_allow_html=True)

logo_path = "data/assets/syncro_logo.png"
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(logo, width=250)
else:
    st.warning("⚠️ Logo not found at data/assets/syncro_logo.png")

st.markdown("<h4 style='color:#3399ff;'>Where the Right Talent Meets the Right Role</h4>", unsafe_allow_html=True)
st.markdown("<p style='font-size:18px;margin-top:14px;'>Find your score for your dream job.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:16px;'>Upload your resume and let Syncro do the magic.</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📄 Upload Your Resume", type=["pdf", "txt"])

if uploaded_file is not None:
    temp_path = os.path.join("data", "temp_resume" + os.path.splitext(uploaded_file.name)[1])
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("🔍 Scanning your resume..."):
        try:
            st.write("➡️ Starting resume parsing...")
            resume_text = parse_resume(temp_path)
            st.write("✅ Resume parsed successfully")

            resumes = {uploaded_file.name: resume_text}

            st.write("➡️ Starting ranking...")
            results = rank_resumes(resumes)
            st.write("✅ Ranking complete")

            time.sleep(1.0)

            best_result = results[uploaded_file.name]
            st.success("✅ Match Found!")

            colA, colB, colC = st.columns([1,2,1])
            with colB:
                st.markdown("<div style='font-size:28px;'>🧑‍💼</div>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='margin-top:6px;'>{best_result['best_match']}</h3>", unsafe_allow_html=True)

            score = best_result['score']
            stars = "⭐" * (score // 20) + "☆" * (5 - score // 20)
            st.markdown(f"<h4 style='text-align:center;'>Score: {score}/100 &nbsp;&nbsp; {stars}</h4>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center;'><b>Keyword Match Ratio:</b> {best_result['keyword_match_ratio']}%</p>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error processing resume: {e}")
