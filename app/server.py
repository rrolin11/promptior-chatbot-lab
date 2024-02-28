from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain.schema import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes

FAISS_DATABASE_PATH = "app/vector_store/faiss"

# Plantilla de contexto utilizada para enviarle al LLM.
# {context} son los resultados relevantes obtenidos de la base de datos.
# {question} es la consulta realizada por el usuario.
PROMPT_TEMPLATE = """
Answer the following question based only on the provided context.

<context>
{context}
</context>

Question: {question}
"""
app = FastAPI()
llm = Ollama(model="llama2")
db = FAISS.load_local(FAISS_DATABASE_PATH, OllamaEmbeddings())
retriever = db.as_retriever()

rag_prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

entry_point_chain = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
)
rag_chain = entry_point_chain | rag_prompt | llm | StrOutputParser()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

add_routes(app, rag_chain, path="/chatbot")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
