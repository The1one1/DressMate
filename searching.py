import streamlit as st
import pinecone

pinecone.init(
    api_key="237d235d-d44d-42f5-a359-8b8ce309050f",
    environment="us-west4-gcp"  # find next to API key in console
)

index = pinecone.Index("rahul")

from sentence_transformers import SentenceTransformer

device = 'cpu'

@st.cache_resource()
def load_mode():
    retriever = SentenceTransformer(
        "flax-sentence-embeddings/all_datasets_v3_mpnet-base", device=device)
    return retriever

retriever = load_mode()


@st.cache_resource()
def query_pinecone(query, top_k):
    xq = retriever.encode([query]).tolist()
    xc = index.query(xq, top_k=top_k, include_metadata=True)
    return xc