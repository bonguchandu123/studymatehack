

import streamlit as st
import requests
from utils.pdf_utils import extract_text_from_pdf, chunk_text
from utils.retriever import QAEngine

st.set_page_config(page_title="📚 StudyMate", layout="wide")
API_URL = "http://localhost:8000"

if "token" not in st.session_state:
    st.session_state.token = None
if "username" not in st.session_state:
    st.session_state.username = None
if "theme" not in st.session_state:
    st.session_state.theme = "Light"

theme = st.selectbox("🌓 Select Theme", ["Light", "Dark"], index=0 if st.session_state.theme == "Light" else 1)
st.session_state.theme = theme

light_css = """
    <style>
    body {
        background-color: white;
        color: black;
    }
    .navbar {
        background: #2575fc;
        color: white;
        padding: 1rem;
        font-size: 24px;
        font-weight: bold;
        border-radius: 0 0 12px 12px;
        margin-bottom: 1rem;
        text-align: center;
    }
    .header-section {
        font-size: 30px;
        font-weight: 600;
        color: #000;
        text-align: center;
        margin-top: 1rem;
    }
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding: 1rem;
        font-size: 14px;
        background: #2575fc;
        color: white;
        border-top-left-radius: 12px;
        border-top-right-radius: 12px;
    }
    </style>
"""

dark_css = """
    <style>
    
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .navbar {
        background: #1f1c2c;
        color: white;
        padding: 1rem;
        font-size: 24px;
        font-weight: bold;
        border-radius: 0 0 12px 12px;
        margin-bottom: 1rem;
        text-align: center;
    }
    .header-section {
        font-size: 30px;
        font-weight: 600;
        color: #ffffff;
        text-align: center;
        margin-top: 1rem;
        
    }

    .footer {
        text-align: center;
        margin-top: 4rem;
        padding: 1rem;
        font-size: 14px;
        background: #1f1c2c;
        color: white;
        border-top-left-radius: 12px;
        border-top-right-radius: 12px;
    }
    </style>
"""

st.markdown(dark_css if theme == "Dark" else light_css, unsafe_allow_html=True)
navbar_html = f"""
    <div class="navbar">
        📘 StudyMate – Smart Q&A from PDFs
        {'<span style="float:right;">👤 ' + st.session_state.username + '</span>' if st.session_state.username else ''}
    </div>
"""
st.markdown(navbar_html, unsafe_allow_html=True)



def show_auth():
    st.title("🔐 Login / Sign Up to Continue")
    auth_mode = st.radio("Choose mode", ["Login", "Sign Up"], horizontal=True)

    with st.form(key="auth_form"):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Submit")

    if submit:
        try:
            if auth_mode == "Sign Up":
                response = requests.post(f"{API_URL}/signup", json={
                    "username": username,
                    "email": email,
                    "password": password
                })
            else:
                response = requests.post(f"{API_URL}/login", json={
                    "email": email,
                    "password": password
                })

            if response.status_code == 200:
                data = response.json()
                st.session_state.token = data["token"]
                st.session_state.username = data["username"]
                st.success(f"✅ {auth_mode} successful! Welcome, {data['username']} 👋")
                st.rerun()
            else:
                st.error(f"❌ {auth_mode} failed: {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Backend connection failed: {str(e)}")


if not st.session_state.token:
    show_auth()
else:
    st.markdown(f"<div class='header-section'>Welcome, {st.session_state.username}! Upload Your PDFs & Ask Questions</div>", unsafe_allow_html=True)

    if st.button("🔓 Logout"):
        st.session_state.token = None
        st.session_state.username = None
        st.rerun()

    qa_engine = QAEngine()
    uploaded_files = st.file_uploader("📤 Upload PDF(s)", type="pdf", accept_multiple_files=True)
    query = st.text_input("💬 Ask a question about your PDFs")

    if not uploaded_files:
        st.info("👆 Please upload one or more PDF files to get started.")
    elif not query:
        st.info("✍️ Enter a question about the uploaded PDF(s).")
    elif uploaded_files and query:
        all_chunks = []
        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            chunks = chunk_text(text)

            if not chunks:
                st.warning(f"⚠️ No usable text extracted from {file.name}. Skipping.")
                continue

            all_chunks.extend(chunks)

        if not all_chunks:
            st.error("❌ No valid content found in uploaded PDFs. Please try different files.")
        else:
            qa_engine.process_documents(all_chunks)
            answer, references = qa_engine.ask(query)

            st.subheader("💡 Answer")
            st.markdown(answer)

            with st.expander("📑 Referenced Paragraphs"):
                for para in references:
                    st.markdown(f"> {para}")


st.markdown("""
    <div class="footer">
        🚀 Built with ❤️ by <a href="https://github.com/bonguchandu123" target="_blank" style="color: white; text-decoration: underline;">@bonguchandu123</a> | © 2025 StudyMate
    </div>
""", unsafe_allow_html=True)
