import streamlit as st
from streamlit_extras .add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
import pickle
# from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

with st.sidebar:
    st.title('LLM Chat')
    st.markdown('Test')
    add_vertical_space(5)
    st.write('Made it by Karan Patel')
# load_dotenv()
def main():
    st.header("Chat with PDF..!!")
    
    pdf=st.file_uploader('Upload Your PDF',type='pdf')
    if pdf is not None:
        st.write(pdf.name)
        pdf_reader=PdfReader(pdf)
        text=""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks= text_splitter.split_text(text=text)
        embeddings=OpenAIEmbeddings()
        VectorStore=FAISS.from_texts(chunks,embedding=embeddings)
        store_name=pdf.name[:-4]
        with open(f"{store_name}.pkl","wb") as f:
            pickle.dump(VectorStore,f)
        # st.write(chunks)

if __name__== '__main__':
    main()
