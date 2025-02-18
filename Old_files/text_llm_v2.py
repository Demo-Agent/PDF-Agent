import streamlit as st
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import ollama

st.title("PDF Viewer with RAG and LLM")


if "pdf_texts" not in st.session_state or not st.session_state["pdf_texts"]:
    st.warning("No extracted text found! Please run the PDF extractor first.")
else:
    texts = st.session_state["pdf_texts"]

    # Load embedding model
    embedding_model = SentenceTransformer("thenlper/gte-large")

    # Convert text to embeddings
    text_embeddings = embedding_model.encode(texts, convert_to_numpy=True)

    # Store embeddings in FAISS
    index = faiss.IndexFlatL2(text_embeddings.shape[1])
    index.add(text_embeddings)

    st.subheader("Ask a Question")
    user_query = st.text_input("Enter your query:")

    if user_query:
        query_embedding = embedding_model.encode([user_query], convert_to_numpy=True)
        _, indices = index.search(query_embedding, k=20)
        retrieved_texts = "\n".join([texts[i] for i in indices[0]])

        # Generate response using Ollama
        input_prompt = f"Context: {retrieved_texts}\n\nQuestion: {user_query}\nAnswer:"
        response = ollama.generate(model="llava:latest", prompt=input_prompt)[
            "response"
        ]

        st.write("### Answer:")
        st.write(response)
