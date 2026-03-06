from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.embeddings import get_embeddings
from langchain_community.vectorstores.faiss import FAISS

loader = DirectoryLoader("data/", loader_cls=TextLoader)
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

embeddings = get_embeddings()

db = FAISS.from_documents(chunks, embeddings)

db.save_local("vectorstore")