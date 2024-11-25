from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv

load_dotenv()

HOSP_SYS_DATA_PATH = "data/data_sheet.txt"

def get_complete_data(patient_data):
    """
    Return string containing with both patient and hospital system information.
    """
    patient_data_with_header = "Patient Information Dictionary:\n\n"+str(patient_data)
    
    hospital_sys_data = open(HOSP_SYS_DATA_PATH, 'r').read()
    hospital_sys_with_header = "Hospital System Information:\n\n"+ hospital_sys_data

    return patient_data_with_header + "\n\n" + hospital_sys_with_header

def build_retriever_tools(complete_data):
    """ 
    Build LangChain retriever tool.
    """
    doc =  Document(page_content=complete_data, metadata={"source": "local"})
    mydocuments = [doc]

    text_splitter = CharacterTextSplitter(chunk_size=1000)
    texts = text_splitter.split_documents(mydocuments)

    # Use OpenAI default embedding model
    embeddings = OpenAIEmbeddings()

    # Use LangChain API functions to interact with FAISS
    db = FAISS.from_documents(texts,embeddings)

    # Using LangChain retriever 
    retriever = db.as_retriever()
    tool = create_retriever_tool(retriever, "appointment_info", "searches and returns info about patient and hospital system")
    return [tool]

def build_agent_executor(patient_data, chat_history):
    """ 
    Build LangChain RAG agent.
    """
    sys_message = f""" 
    You are a helpful assistant. Your task is to answer the user questions about the patient data \
    and the hospital system data that you have access to.

    So far, this is the chat history that you have had with this user:
    {chat_history}

    Your task is the answer the user questions that will be provided to you.
    """
    complete_data = get_complete_data(patient_data)
    retriever_tools = build_retriever_tools(complete_data)
    model = ChatOpenAI(temperature=0,max_tokens=200)
    return create_conversational_retrieval_agent(llm=model,tools=retriever_tools,system_message=SystemMessage(content=sys_message))

def get_response(patient_data, user_query, chat_history):
    """
    Get retrieval augmented LLM response.
    """
    agent_executor = build_agent_executor(patient_data, chat_history)
    response = agent_executor.invoke({"input": user_query})
    return response['output']