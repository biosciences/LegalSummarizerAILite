import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from core import pdf_parser, prompt_template, summarizer, doc_generator
from core.doc_generator import summary_to_html

# Set Streamlit page config
st.set_page_config(page_title="LegalSummarizerAI Lite", layout="wide")
st.title("📑 LegalSummarizerAI Lite")
st.markdown("Upload a NSW residential tenancy agreement PDF. I’ll generate a structured summary and flag risks.")

# File uploader
uploaded = st.file_uploader("📤 Upload PDF", type="pdf")

if uploaded:
    # Extract text from uploaded PDF
    raw_text = pdf_parser.extract_text(uploaded)
    
    # Build structured prompt
    user_prompt = prompt_template.build_user_prompt(raw_text)
    
    # Generate summary using GPT-4o
    with st.spinner("🧠 Summarising with GPT-4.1..."):
        try:
            summary = summarizer.generate_summary(user_prompt)
        except Exception as e:
            st.error(f"❌ Failed to summarize: {e}")
            st.stop()

    # Display summary
    st.subheader("📝 AI-Generated Summary")
    st.markdown(summary)

    # Save HTML to /docs/
    html_path = summary_to_html(summary)
    st.success(f"📄 HTML summary saved to `{html_path}`")

    # Offer downloads
    col1, col2 = st.columns(2)
    with col1:
        word_buf = doc_generator.summary_to_word(summary)
        st.download_button("⬇️ Download Word", data=word_buf, file_name="summary.docx")
    with col2:
        pdf_buf = doc_generator.summary_to_pdf(summary)
        st.download_button("⬇️ Download PDF", data=pdf_buf, file_name="summary.pdf")
