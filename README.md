                 **AI-Powered Streamlit Application for PDF Processing and Analysis**
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Overview**

This Streamlit-based application enables users to:

Extract text, images, and tables from PDFs.

Interact with an AI-powered chatbot for in-depth PDF content analysis.

Perform AI-driven image analysis on extracted images using advanced LLMs.

**Large Language Models (LLMs) Utilized**

1. DeepSeek-R1 (70B Llama Variant)

Utilized for text-based PDF question-answering in text_llm.py.

2. LLaVA (Large Language and Vision Assistant)

Used for image analysis in image_llm.py.

Accepts and processes both text and image inputs.

**Libraries and Tools**

Streamlit: Web UI framework for interactive applications.

unstructured.partition.pdf: Extracts structured data (text, tables, images) from PDFs.

OpenAI: Enables AI-driven chatbot functionalities.

Requests: Facilitates API calls to external LLMs (via Ollama for image analysis).

glob, os, shutil: Manages file handling operations.

base64: Encodes images for API-based communication.

PIL (Pillow): Image processing.

fpdf: Generates PDFs from modified text.

**Key Features**

📄 PDF Extraction (extraction.py)

Upload a PDF and extract structured data, including text, tables, and images.

Navigate through the extracted content via an interactive user interface.

Edit extracted text and download the modified content as a PDF.

🤖 AI-Powered Chatbot (text_llm.py)

Ask questions about extracted PDF content using the DeepSeek-R1 (Llama-70B) model.

Receive AI-generated responses based on the document’s content.

🖼️ AI-Based Image Analysis (image_llm.py)

View images extracted from PDFs.

Query the AI (LLaVA model) to analyze images and provide insightful responses.

**Technologies & Dependencies**

Programming Language

Python

Framework

Streamlit

LLMs Used

deepseek/deepseek-r1-distill-llama-70b:free

llava:latest (via Ollama API)

Required Libraries

streamlit - UI framework

unstructured - PDF processing

openai - AI-powered chatbot

requests - API communication

fpdf - PDF generation

Installation Guide

Prerequisites

Ensure you have the latest version of Python installed.

sudo apt update
sudo apt install python3.10
python3.10 --version

Create a Virtual Environment

python3 -m venv myenv
source myenv/bin/activate

Install Dependencies

pip install -r requirements.txt

Running the Application

To launch the Streamlit app, execute the following command:

streamlit run main.py

This will start the application and allow users to interact with the AI-powered PDF processing system through a web interface.

This document provides a structured, professional overview of the AI-powered PDF processing and analysis application. Let me know if you need further refinements or additional details!
