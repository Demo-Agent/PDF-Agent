import streamlit as st
from unstructured.partition.pdf import partition_pdf
import glob
import os
from PIL import Image as PILImage
from fpdf import FPDF

# Set OCR agent
os.environ["OCR_AGENT"] = "Tesseract"

# Title of the app
st.title("Content Extractor from PDF")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    filename = "temp.pdf"
    with open(filename, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        elements = partition_pdf(
            filename=filename,
            strategy="hi_res",
            extract_images_in_pdf=True,
            infer_table_structure=True,
            extract_image_block_output_dir="images",
            ocr_languages="eng",
        )

        texts = [el for el in elements if el.category == "NarrativeText"]
        images = [el for el in elements if el.category == "Image"]
        tables = [el for el in elements if el.category == "Table"]

        st.session_state["pdf_texts"] = [
            el.text for el in elements if el.category == "NarrativeText"
        ]

        text_pages = {
            el.metadata.page_number
            for el in texts
            if el.metadata and el.metadata.page_number
        }
        table_pages = {
            el.metadata.page_number
            for el in tables
            if el.metadata and el.metadata.page_number
        }

        content_pages = text_pages.union(table_pages)

        st.header("Table of Contents")
        toc = {
            "Pages Numbers": len(content_pages),
            "Images": len(images),
            "Tables": len(tables),
        }
        for key, value in toc.items():
            st.write(f"- {key}: {value}")

        st.sidebar.title("Navigation")
        section_type = st.sidebar.selectbox(
            "Select Section Type", ["Text", "Image", "Table"]
        )

        if section_type == "Text":
            st.header("Text Sections")
            page_contents = {}

            for el in elements:
                page = (
                    el.metadata.page_number
                    if el.metadata and el.metadata.page_number
                    else 1
                )
                if page not in page_contents:
                    page_contents[page] = []
                if el.category in ["Title", "NarrativeText"]:
                    text = el.text.strip()
                    page_contents[page].append({"type": "text", "content": text})

            sorted_pages = sorted(page_contents.keys())
            selected_page = st.sidebar.selectbox("Select Page", sorted_pages, index=0)
            st.header(f"Contents of Page {selected_page}")

            text_content = "\n".join(
                [
                    item["content"]
                    for item in page_contents[selected_page]
                    if item["type"] == "text"
                ]
            )

            if "modified_text" not in st.session_state:
                st.session_state["modified_text"] = {}

            if selected_page not in st.session_state["modified_text"]:
                st.session_state["modified_text"][selected_page] = text_content

            st.write(st.session_state["modified_text"][selected_page])

            if st.button("Modify"):
                st.session_state["editing"] = selected_page

            if (
                "editing" in st.session_state
                and st.session_state["editing"] == selected_page
            ):
                modified_text = st.text_area(
                    "Edit Text", st.session_state["modified_text"][selected_page]
                )
                col1, col2 = st.columns(2)

                if col1.button("Save"):
                    st.session_state["modified_text"][selected_page] = modified_text
                    del st.session_state["editing"]
                    st.rerun()
                if col2.button("Cancel"):
                    del st.session_state["editing"]
                    st.rerun()

                if st.button("Download as PDF"):

                    pdf = FPDF()
                    pdf.add_page()

                    # Load a Unicode font (DejaVuSans supports UTF-8)
                    # pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
                    # pdf.set_font("DejaVu", size=12)

                    # Ensure UTF-8 encoding
                    text = st.session_state["modified_text"][selected_page]

                    pdf.multi_cell(190, 10, text)

                    pdf_file = f"modified_page_{selected_page}.pdf"
                    pdf.output(pdf_file, "F")

                    with open(pdf_file, "rb") as f:
                        st.download_button(
                            label="Download PDF",
                            data=f,
                            file_name=pdf_file,
                            mime="application/pdf",
                        )

    except Exception as e:
        st.error(f"An error occurred: {e}")

    finally:
        if os.path.exists(filename):
            os.remove(filename)
