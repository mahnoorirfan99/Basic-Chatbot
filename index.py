import streamlit as st
from spellchecker import SpellChecker

# Initialize spell checker
spell = SpellChecker()

# Predefined chatbot responses
responses = {
    "hello": ["Hi there! 😊", "Hello!", "Hey! How can I assist you?"],
    "how are you": ["I'm great! How about you? 🤖", "Feeling chatty today!"],
    "your name": ["I'm a chatbot! 🤖", "Just call me ChatBot."],
    "bye": ["Goodbye! 👋", "See you later!", "Bye! Have a great day!"],
}

# Function to correct spelling
def correct_spelling(sentence):
    words = sentence.split()
    corrected_words = [spell.correction(word) or word for word in words]
    return " ".join(corrected_words)

# Function to get chatbot response
def chatbot_response(user_input):
    corrected_input = correct_spelling(user_input.lower())
    for key in responses.keys():
        if key in corrected_input:
            return responses[key][0]
    return "Sorry, I don't understand that. 🤔"

# Page Config
st.set_page_config(page_title="AI ChatBot", page_icon="🤖", layout="wide")

# Header
st.markdown("<h1 style='text-align: center;'>🤖 AI ChatBot</h1>", unsafe_allow_html=True)

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
chat_history = st.empty()  # Placeholder for chat history
with chat_history.container():
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["text"])

# Input Box Fixed at Bottom
st.markdown(
    """
    <style>
    .css-1v0mbdj {position: fixed; bottom: 0; left: 0; width: 100%; padding: 10px; background-color: #f5f5f5;}
    .css-2y3b16 {padding-right: 15px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# User input field
user_input = st.text_input("Type your message...", key="user_input", label_visibility="collapsed")

# Handle input and responses
if user_input:
    # Store and display user message
    st.session_state.messages.append({"role": "user", "text": f"🧑‍💻 {user_input}"})
    
    # Generate bot response
    response = chatbot_response(user_input)
    st.session_state.messages.append({"role": "bot", "text": f"🤖 {response}"})

    # Refresh the chat history display
    chat_history.empty()  # Clear previous content
    with chat_history.container():
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["text"])


