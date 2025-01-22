import os
from dotenv import load_dotenv
from pymongo import MongoClient
# from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime
import google.generativeai as genai
from langchain_google_vertexai import ChatVertexAI
from langchain_google_vertexai import VertexAIEmbeddings

load_dotenv(override=True)

llm = ChatVertexAI(model="gemini-1.5-flash")
embeddings = VertexAIEmbeddings(model="text-embedding-004")

client = MongoClient(os.getenv('MONGO_URI'))
dbName = "langchain_demo"
collectionName = "collection_of_text_blobs"
collection = client[dbName][collectionName]

vectorStore = MongoDBAtlasVectorSearch(collection, embeddings)
