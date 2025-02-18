import streamlit as st
from unstructured.partition.pdf import partition_pdf
import glob
import os
from PIL import Image as PILImage

# Title of the app
st.title("PDF Viewer with TOC")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    # Save the uploaded file temporarily
    filename = "temp.pdf"
    with open(filename, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract elements using `hi_res` strategy
    elements = partition_pdf(
        filename=filename,
        strategy='hi_res',
        extract_images_in_pdf=True,
        infer_table_structure=True,
        extract_image_block_output_dir="images"
    )

    # Convert elements to dictionary format
    element_dict = [el.to_dict() for el in elements]

    # Separate text, images, and tables
    texts = [el for el in elements if el.category == "Text"]
    images = [el for el in elements if el.category == "Image"]
    tables = [el for el in elements if el.category == "Table"]

    # Display TOC (Table of Contents)
    st.header("Table of Contents")
    toc = {
        "Text Sections": len(texts),
        "Images": len(images),
        "Tables": len(tables)
    }
    for key, value in toc.items():
        st.write(f"- {key}: {value}")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    section_type = st.sidebar.selectbox("Select Section Type", ["Text", "Image", "Table"])

    if section_type == "Text":
        st.header("Text Sections")
        max_idx = max(0, len(texts) - 1)  # Ensure max_value is non-negative
        selected_text_index = st.sidebar.number_input(
            "Select text index", min_value=0, max_value=max_idx, value=min(1, max_idx)
        )
        if texts:
            st.write(f"**Text Section {selected_text_index + 1}:**")
            st.write(texts[selected_text_index].text)

    elif section_type == "Image":
        st.header("Images")
        image_files = glob.glob("images/*.jpg")
        selected_image_index = st.sidebar.number_input(
            "Select Image", min_value=1, max_value=len(image_files), value=1
        )
        if image_files:
            st.image(image_files[selected_image_index - 1], caption=f"Image {selected_image_index}")

    elif section_type == "Table":
        st.header("Tables")
        selected_table_index = st.sidebar.number_input(
            "Select Table", min_value=1, max_value=len(tables), value=1
        )
        if tables:
            st.write(f"**Table {selected_table_index}:**")
            st.markdown(tables[selected_table_index - 1].metadata.text_as_html, unsafe_allow_html=True)

    # Clean up temporary files
    os.remove(filename)
    for file in glob.glob("images/*.jpg"):
        os.remove(file)
