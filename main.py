import streamlit as st

pages = {
    "Text, Image, Table Extraction": [
        st.Page("extraction.py", title="Extraction"),
    ],
    "Text with LLM": [
        st.Page("text_llm_v2.py", title="Text Summarization With RAG and LLM"),
    ],
    "Image with LLM": [
        st.Page("image_llm_v2.py", title="Image Summarization With LLM"),
    ],
}

pg = st.navigation(pages)
pg.run()
