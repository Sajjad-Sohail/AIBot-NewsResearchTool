import os
import streamlit as st
import time
import pickle
from langchain_openai import OpenAI
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI


from dotenv import load_dotenv
load_dotenv()

st.title("News Research Tool")
st.sidebar.title("New Article URLs")

urls = []
file_path = "faiss_store_openai.pkl"
main_placefolder = st.empty()
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

if process_url_clicked:
    loader = UnstructuredURLLoader(urls=urls)
    main_placefolder.text("Data Loading...Started...")
    data = loader.load()
    main_placefolder.text("Loaded..now text_splitter is initializing")

    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n','.',','],
        chunk_size=1000
    )
    main_placefolder.text("Documents splitting...")

    docs = text_splitter.split_documents(data)
    #creating embedding

    embeddings  = OpenAIEmbeddings()
    main_placefolder.text("Documents splitting...")
    main_placefolder.text("Embedding Vector Started Building...")
    #saving into FAISS
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    time.sleep(2)
    #save the FAISS index to a pickle file
    
    main_placefolder.text("Embedding saving to disc...")

    vectorstore_openai.save_local("faiss_index")
    main_placefolder.text("Embedding saving finished.!!!")

    


query = main_placefolder.text_input("Question:")
if query:
    
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )
    
    st.success("FAISS Loaded Successfully!")


     

