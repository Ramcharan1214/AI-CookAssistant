from langchain.prompts import (
    ChatPromptTemplate, 
    HumanMessagePromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate,
)

from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser

import streamlit as st
# Title and initial description
st.set_page_config(page_title="AI Cook Assistant", page_icon="🍳")
st.title("AI Cook Assistance")
st.write("This chatbot helps you with cooking-related questions!")
st.image("https://img.freepik.com/premium-photo/ai-assistant-can-detect-adjust-any-errors-made-by-cook-ensuring-successful_216520-112957.jpg",  use_container_width=True)


# Apply custom CSS
st.markdown("""
    <style>
        body { background-color: #1c1a1a; }
        h1 { color: #FFFFFF; text-align: center; }
    </style>
""", unsafe_allow_html=True)


# Function to get and store the API key securely in session state
def get_api_key():
    if "api_key" not in st.session_state:
        st.session_state["api_key"] = ""
    api_key = st.text_input("Enter your Google API Key:", type="password", key="api_key")
    return api_key

# Prompt user for API key input
api_key = get_api_key()

# Ensure the API key is available
if not api_key:
    st.warning("Please enter your API Key to continue.")
else:
    # Create a prompt template
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                "You are ChefAI, a highly skilled and friendly AI Cooking Assistant. Your goal is to help users with all aspects of cooking, including recipe suggestions, ingredient substitutions, step-by-step instructions, meal planning, and answering cooking-related questions. You are knowledgeable about cuisines from around the world, dietary restrictions, and cooking techniques.Dont answer the querrys which are not related to cooking.Focus strongly only one the cooking related questions not on any others."
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{question}"),
        ]
    )

    # Initialize message history
    msgs = StreamlitChatMessageHistory(key="langchain_messages")

    # Set up the Google AI model using the provided API key
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

    # Combine prompt, model, and output parser
    chain = prompt | model | StrOutputParser()

    # Combine chain with history for maintaining session
    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: msgs,
        input_messages_key="question",
        history_messages_key="chat_history",
    )

    # Get user input
    user_input = st.text_input("Enter your question in English:", "")

    # Check if user input is provided
    if user_input:
        st.chat_message("human").write(user_input)

        # Assistant's response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            # Configuration dictionary
            config = {"configurable": {"session_id": "any"}}

            # Get response from AI model
            response = chain_with_history.stream({"question": user_input}, config)

            # Stream and display response in real-time
            for res in response:
                full_response += res or ""
                message_placeholder.markdown(full_response + "|")
                message_placeholder.markdown(full_response)

    else:
        st.warning("Please enter your question.")
        