"""Main RAG pipeline implementation."""

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA


class GutenbergRAG:
    """RAG pipeline for Gutenberg Bible text."""
    
    def __init__(self, api_key: str):
        self.embeddings = OpenAIEmbeddings(api_key=api_key)
        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)
        self.vectorstore = None
        self.qa_chain = None
    
    def create_index(self, text: str):
        """Create vector index from text."""
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = splitter.split_text(text)
        self.vectorstore = Chroma.from_texts(
            texts=chunks,
            embedding=self.embeddings
        )
        return self
    
    def query(self, question: str) -> str:
        """Query the RAG pipeline."""
        if not self.qa_chain:
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                retriever=self.vectorstore.as_retriever()
            )
        return self.qa_chain.invoke({"query": question})["result"]
