# PDF Processing & AI-Powered Analysis - A simple, clear title like: "AI-Powered Streamlit App for Extraction, Chatbot, and Multi-Model Image Processing"

        **Overview**:-
This Streamlit-based application allows users to: - Extract text, images, and tables from PDFs. - Interact with an AI-powered chatbot to analyze PDF content. - Analyze extracted images using LLMs.

LLMs used:
DeepSeek-R1 (70B Llama Variant)
Used for text-based PDF Q&A (text_llm.py).
LLaVA (Large Language and Vision Assistant)
Used for image analysis in image_llm.py.
Accepts both text and image inputs.
Libraries and Tools:
streamlit: Web UI for interactive applications -unstructured.partition.pdf: Extracts structured data (text, tables, images) from PDFs
openai: Access to OpenAI-based LLMs
requests: API calls to external LLMs (Ollama for image analysis)
glob, os, shutil: File handling
base64: Encodes images for API communication
PIL: Image processing
fpdf: PDF generation for modified text
Features
📄 PDF Extraction (extraction.py)
Upload a PDF and extract structured data (text, tables, images).
Navigate extracted content using an interactive UI.
Edit extracted text and download modified content as a PDF.
🤖 Chat with Your PDF (text_llm.py)
Ask questions about extracted PDF content using DeepSeek-R1 (Llama-70B).
AI responds with relevant answers based on PDF content.
🖼️ Image-Based Analysis (image_llm.py)
View extracted images from PDFs.
Ask AI (LLaVA model) to analyze and answer queries about images.
Technologies & Dependencies
Programming Language: Python
Framework: Streamlit
LLMs Used:
deepseek/deepseek-r1-distill-llama-70b:free
llava:latest (via Ollama API)
Libraries:
streamlit - UI framework
unstructured - PDF processing
openai - AI-powered chatbot
requests - API communication
fpdf - PDF generation
Installation
Prerequisites
Install Python3 version latest versions
''' sudo apt update '''
''' sudo apt install python3.10 '''
''' python3.10 --version '''
Create python3 virtual environment
''' python3 -m venv myenv '''
''' source myenv/bin/activate '''
Install dependencies:
""" pip install -m requirements.txt """
Running the Application
-Start the Streamlit app:
  - ''' streamlit run main.py '''
Streamlit will help to run the application
