# Promptior Lab
 
## Introducción

Implementación de Chatbot utilizando LangChain y arquitecutra RAG, y el LLM Ollama Llama 2, con la finalidad de que `pueda responder preguntas la empresa [Promptior](https://www.promptior.ai/).

Se detallan a continuación instrucciones para correr la aplicación localmente.

## Dependencias de entorno

El siguiente laboratorio se realizará en el sistema operativo Windows 10 versión 22H2.

Será necesario instalar:

* Python 3.11.8: https://www.python.org/downloads/release/python-3118/

* Ollama para Windows 10 o posterior: https://ollama.com/download/windows
  

## Estructura del proyecto
 
El proyecto se compone de los siguientes elementos:

* data_source: Es la carpeta contenedora de la información que populará la base de datos. En este caso consta de archivos de extensión .txt.
* app/server.py: Contiene la implementación del chatbot. Script encargado de buscar la consulta en la base de datos y enviarla al LLM. Recibe como parámetro una cadena de texto (string).
* app/vector_store: La carpeta contiene la base de datos del contexto de negocio. De dicha base de dato se obtienen resultados relevantes según la consulta que se haga al Chatbot.
* create_database.py: Script de creación de base. Aquí también se fija el tamaño de los tramos de texto a convertir en vectores, su superposición, así como la función de incersión (embedding function), y ruta de la base. Tomará los archivos .txt de data_source.
* requirements.txt: Las dependencias del proyecto. Se pueden instalar individualmente con el comando "pip install" de Python, desde la consola.

## Dependencias del proyecto

Una vez descargado el repositorio, se deberá abrir la terminal sobre la carpeta raíz del mismo y ejecutar el siguiente comando:

    pip install -r requirements.txt

Se instalarán las dependencias necesarias para ejecutar el proyecto. Es importante que se hayan instalado las dependencias de entorno previamente. 

## Creación de base de datos

Antes de utilizar el Chatbot se deberá correr el script de creación de base de datos. El mismo consumirá los documentos que se encuentran en la carpeta data_soruce para generar los vectores y popular la base.

Ejecutar el siguiente comando:

    python create_database.py
 
## Corriendo la API

Para correr la aplicación en un puerto local como una API REST se deberá ejecutar el siguiente comando:

    langchain serve

De este modo, la terminal indicará en qué puerto está corriendo. Se puede interactuar con el chatbot navegando a la siguiente direción "/chatbot/playground/". 

Por defecto, la URL es: http://127.0.0.1:8000/chatbot/playground/

## Deploy con Docker en Azure

Se recomienda firmemente seguir este videotutorial: https://www.youtube.com/watch?v=HyCO6nMdxC0

## Glosario

**Chatbot:** Los bot de charla o bot conversacional, ​son aplicaciones software que simulan mantener una conversación con una persona al proveer respuestas automáticas.

**LLM:** Un modelo de lenguaje grande o LLM (siglas en inglés para Large Language Model), son modelos de aprendizaje profundo muy grandes que se preentrenan con grandes cantidades de datos. Buscan extraer significados de una secuencia de texto y comprenden las relaciones entre las palabras y las frases que contiene.

**RAG:** La generación mejorada por recuperación (en inglés Retrieval Augmented Generation) es el proceso de optimización de la salida de un modelo lingüístico de gran tamaño, de modo que haga referencia a una base de conocimientos autorizada fuera de los orígenes de datos de entrenamiento antes de generar una respuesta. RAG extiende las capacidades de los LLM a dominios específicos o a la base de conocimientos interna de una organización, todo ello sin la necesidad de volver a entrenar el modelo.

**Ollama:** Llama es un framework de inteligencia artificial que permite ejecutar grandes modelos de lenguaje localmente. 

**Llama 2:** Es un modelo de lenguaje de inteligencia artificial desarrollado por META. Utiliza una arquitectura de red neuronal llamada Transformer para entender y generar texto de manera coherente y relevante

**LangChain:** LangChain es un marco de orquestación de código abierto para el desarrollo de aplicaciones que utilizan modelos de lenguaje de gran tamaño (LLM). Disponibles en bibliotecas basadas en Python y Javascript, las herramientas y API de LangChain simplifican el proceso de creación de aplicaciones impulsadas por LLM, como chatbots y agentes virtuales.

**LangServe:** Herramienta que simplifica la construcción y despliegue de aplicaciones LangChain.

**FAISS:** En inglés "Facebook AI Similarity Search", es una biblioteca de Python que proporciona a los desarrolladores un medio rápido y eficiente para alojar buscar incrustaciones similares, alejándose de los enfoques convencionales basados en hash, siendo en realidad una base de indización vectorial.