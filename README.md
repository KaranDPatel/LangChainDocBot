**PDF ChatBot with Streamlit, LangChain, and OpenAI**

**Overview**

This project is a PDF ChatBot that allows users to upload any PDF document, ask questions, and receive answers directly from the content of the PDF. It is built using Streamlit, LangChain, and OpenAI. The architecture efficiently processes and splits PDF content, embeds it for semantic search, and allows for natural language querying.

**Features**

PDF Upload: Upload any PDF document directly from the web interface.

Interactive Chat: Ask questions about the content of the PDF and receive relevant answers.

Streamlit Interface: A simple and intuitive web-based interface for interacting with your PDF.

OpenAI Integration: Leverages OpenAI's embeddings for semantic search within the document.

Persistent Storage: Saves vectorized representations of the PDF content for quick access in future sessions.

**Prerequisites**

Python 3.7+ installed on your system.

Required Python packages: streamlit, langchain, PyPDF2, dotenv, openai, faiss-cpu.

**Installation**

Clone the Repository:


sh
Copy code
git clone url
cd pdf-chatbot

Install Required Python Packages:

sh
Copy code
pip install streamlit langchain PyPDF2 python-dotenv openai faiss-cpu

Set Up Your OpenAI API Key:


Create a .env file in the root directory and add your OpenAI API key:
makefile
Copy code

OPENAI_API_KEY=your_openai_api_key
Usage
Run the Streamlit Application:

sh
Copy code
streamlit run main.py

Upload a PDF:

Use the interface to upload your PDF file.

Ask Questions:


Once the PDF is processed, you can ask questions in natural language, and the bot will return answers directly from the document.

File Structure
bash
Copy code
pdf-chatbot/

│

├── main.py                # Main script for the PDF ChatBot

├── README.md              # This readme file

├── .env                   # Environment file containing API keys

├── requirements.txt       # List of Python dependencies

└── backup/                # Directory for storing vectorized PDF content

**Architecture**
The project utilizes the following architecture:


PDF Extraction: Extracts text from uploaded PDF files using PyPDF2.

Text Splitting: Splits the extracted text into manageable chunks for processing using LangChain.

Embedding: Uses OpenAI embeddings to convert text chunks into vectors for semantic search.

Vector Store: Stores the vectors using FAISS for efficient retrieval.

Querying: Accepts user queries, processes them, and retrieves relevant answers from the vector store.


Customization

Chunk Size and Overlap: Adjust the chunk_size and chunk_overlap parameters in the RecursiveCharacterTextSplitter to fine-tune text chunking.
Storage Location: Modify the storage location for vectorized content as needed.
