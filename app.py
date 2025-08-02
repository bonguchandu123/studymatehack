

import streamlit as st
from utils.pdf_utils import extract_text_from_pdf, chunk_text
from utils.retriever import QAEngine


st.set_page_config(page_title="📚 StudyMate", layout="wide")

st.markdown("""
    <style>
    /* Gradient Background */
    body {
        background: linear-gradient(to right, #d9a7c7, #fffcdc);
    }

    /* Navbar */
    .navbar {
        position: sticky;
        top: 0;
        z-index: 999;
        background: linear-gradient(to right, #6a11cb, #2575fc);
        color: white;
        padding: 1rem 2rem;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-radius: 0 0 8px 8px;
    }

    /* Header section */
    .header-section {
        font-size: 36px;
        font-weight: 700;
        text-align: center;
        margin-top: 1rem;
        color: #333333;
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding: 1rem;
        font-size: 14px;
        background: linear-gradient(to right, #6a11cb, #2575fc);
        color: white;
        border-top-left-radius: 12px;
        border-top-right-radius: 12px;
    }

    /* Remove streamlit default max width */
    .css-18e3th9 {
        padding-top: 0rem;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="navbar">📘 StudyMate – Smart Q&A from PDFs</div>', unsafe_allow_html=True)


st.markdown('<div class="header-section">Upload Your PDFs & Ask Questions</div>', unsafe_allow_html=True)


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


# (studymate-env) PS C:\Users\bongu\Downloads\New folder (6)\studymate> streamlit run app.py