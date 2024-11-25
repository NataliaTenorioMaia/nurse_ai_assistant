import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from llm_functions import get_response
from api_functions import get_data

# app title
st.image("logo.jpeg",width=50)
st.write("# AI Assistant")
st.write("### Patient Appointment Scheduling")
st.write("\n\n")

# request patient id from user
patient_id = st.text_input("Before starting a conversation with the AI Assistant, you must first provide a valid patient id.")
patient_data = None
if patient_id:
    try:
        patient_data = get_data(patient_id)
        if patient_data is None:
            st.failure(f"The patient id {patient_id} was not found in our system. Please provide a valid patient id.")
    except:
        st.error("Invalid patient id format. Please provide a valid patient id. For example: 1")

if patient_data:
    st.success("Patient data successfully retrieved! You may now start a conversation with the AI Assistant.")

    # session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello! I am an AI Assistant. How can I help you?"),
        ]

    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)

    # user input
    user_query = st.chat_input("Type your message here...")

    if user_query:
        st.session_state.chat_history.append(HumanMessage(content=user_query))

        with st.chat_message("Human"):
            st.markdown(user_query)

        with st.chat_message("AI"):
            ai_response = get_response(patient_data, user_query, st.session_state.chat_history)
            st.markdown(ai_response)

        st.session_state.chat_history.append(AIMessage(content=ai_response))