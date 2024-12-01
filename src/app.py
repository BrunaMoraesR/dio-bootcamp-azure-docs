import streamlit as st

def configure_interface():
    st.title("Upload de arquivos DIO - Desafio 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploaded("Escolha um arquivo", type=["png", "jpg", "jpeg"])