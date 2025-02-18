import streamlit as st
import glob
import os
import base64
import requests
import shutil  # To delete image directory

# Title of the app
st.title("Image Viewer with LLM")

# Check if extracted text exists in session state
if "pdf_texts" not in st.session_state or not st.session_state["pdf_texts"]:
    st.warning("No extracted text found! Please run the PDF extractor first.")

    # If no text, remove the images folder
    if os.path.exists("images"):
        shutil.rmtree("images")  # Delete the entire images folder

else:
    # Fetch all images from the 'images' folder
    image_files = glob.glob("images/*.jpg")

    if image_files:
        image_options = [f"Image {i+1}" for i in range(len(image_files))]
        # Dropdown to select an image
        selected_image_label = st.sidebar.selectbox(
            "Select Image", image_options, index=0
        )
        selected_image_index = image_options.index(
            selected_image_label
        )  # Get actual index
        selected_image_path = image_files[selected_image_index]
        st.image(
            selected_image_path,
            caption=f"Image {selected_image_index+1}",
            use_container_width=True,
        )

        # Query box for user input
        user_query = st.text_input("Enter your query about the image:")

        # Button to submit the query
        if st.button("Ask about the image"):
            if user_query:
                # Function to encode image to base64
                def encode_image_to_base64(image_path):
                    with open(image_path, "rb") as image_file:
                        return base64.b64encode(image_file.read()).decode("utf-8")

                # Encode the selected image to base64
                encoded_image = encode_image_to_base64(selected_image_path)

                # Define the prompt for LLaVA
                prompt = f"USER: {user_query}\nASSISTANT:"

                # Prepare the payload for Ollama API
                payload = {
                    "model": "llava:latest",  # Replace with the actual model name if different
                    "prompt": prompt,
                    "images": [encoded_image],  # Send the base64-encoded image
                    "stream": False,
                }

                # Send the request to Ollama API
                try:
                    response = requests.post(
                        "http://localhost:11434/api/generate", json=payload
                    )
                    response.raise_for_status()  # Raise an error for bad responses

                    # Parse the response
                    result = response.json()
                    st.write(f"Response from LLaVA: {result['response']}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error communicating with Ollama: {e}")
            else:
                st.warning("Please enter a query.")
    else:
        st.write("No images found in the 'images' folder.")
