import langchain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
def get_split():
    laoder = PyPDFLoader(file_path ='Egyptian_Law(2025).pdf')
    pages = laoder.load()
    chunks = RecursiveCharacterTextSplitter(
        chunk_size = 600,
        chunk_overlap = 120,
        separators=["\n\n", "\n", ".", " "]
    )
    splits = chunks.split_documents(pages)
    return splits