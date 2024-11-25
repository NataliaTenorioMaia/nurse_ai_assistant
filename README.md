# Nurse AI Assistant for Patient Appointment Scheduling

This application leverages AI to help nurses with scheduling patient appointments. We apply Retrieval Augmented Generation (RAG) technique via LangChain and OpenAI to build a chatbot that has access to both patient and hospital system information in order to answer any questions a nurse might ask during the process of scheduling a patient appointment. This user-friendly application substantially decreases the time a nurse spends to find relevant information, and it ultimately helps patients get access to the best care faster.

Before start a conversation with the AI Assistant, the nurse must provide a patient ID that will be used to retrieve the patient data. Once the patient data has been retrieved, the AI Assistant is initialized allowing the conversation to start.

If you want to run this app in your machine, git clone this repo and follow the instructions below.

1. Create a virtual environment preferrably with python 3.11 to avoild packages conflicts
2. Run `pip install -r requirements.txt`
3. Create a `.env` file and save your private OPENAI_API_KEY there
4. Make sure your default browser is Google Chrome and not Safari to avoid conflicts
4. Run `streamlit run app.py`