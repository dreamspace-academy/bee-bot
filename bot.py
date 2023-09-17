from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate


def get_text_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            text = f.read()
        return text
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return ""
    except Exception as e:
        print(f"Error reading the file: {e}")
        return ""


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    template = """ You are an AI assistant for answering questions about DreamSpace Academy.if the question is a greeting answer with greeting else Use the following pieces of context to answer the question at the end. 
    If you don't know the answer, just say 'Sorry, I don't know', don't try to make up an answer. 
    Use three sentences maximum and keep the answer as concise as possible.
    If the question is not about the DreamSpace Academy, politely inform them that you are tuned to only answer questions about DreamSpace Academy. 
    {context}
    Question: {question}
    Helpful Answer:"""

    # question_prompt = PromptTemplate.from_template(template)

    llm = ChatOpenAI()

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
        verbose=True,
    )

    QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "question"], template=template)

    conversation_chain.combine_docs_chain.llm_chain.prompt.messages[0] = SystemMessagePromptTemplate(
        prompt=QA_CHAIN_PROMPT)

    return conversation_chain
