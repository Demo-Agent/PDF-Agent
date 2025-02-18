import streamlit as st

pages = {
    "Text, Image, Table Extraction": [
        st.Page("extraction_v2.py", title="Extraction"),
    ],
    "Chat Bot": [
        st.Page("text_llm.py", title="Chat Bot"),
    ],
    "Multi Model Image": [st.Page("image_llm_v2.py", title="Multi Model Image")],
}

pg = st.navigation(pages)
pg.run()
