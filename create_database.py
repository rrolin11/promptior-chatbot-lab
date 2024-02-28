from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import os

FAISS_DATABASE_PATH = "./app/vector_store/faiss"
DATA_SOURCE_PATH = "data_source"


def main():
    generate_vector_store()


def generate_vector_store():
    if os.path.exists(FAISS_DATABASE_PATH):
        print(f"Abortado: Existe una base de datos en la ruta \"{FAISS_DATABASE_PATH}\"." + 
              "Elimine la base manualmente antes de continuar.")
    else:
        print("Comienza la generación de la base de vectores.")
        documents = load_documents()
        chunks = split_text(documents)
        create_chroma_database(chunks)


def load_documents():
    loader = DirectoryLoader(DATA_SOURCE_PATH, glob="*.txt")
    documents = loader.load()
    print(f"Cargando todos los documentos desde la ruta {DATA_SOURCE_PATH}.")
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=120,
        length_function=len,
        add_start_index=True
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Se dividieron {len(documents)} documentos en {len(chunks)} tramos.")
    return chunks


def create_chroma_database(chunks: list[Document]):
    print("Comienza la creación de la base. Esto puede tardar algunos minutos...")    
    db = FAISS.from_documents(
        documents=chunks, 
        embedding=OllamaEmbeddings()
    )
    db.save_local(FAISS_DATABASE_PATH)
    print(f"Creación exitosa. Se guardaron {len(chunks)} tramos en la base Chroma. Ruta: {FAISS_DATABASE_PATH}.")


if __name__ == "__main__":
    main()
