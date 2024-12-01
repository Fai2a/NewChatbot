import streamlit as st
import google.generativeai as genai

# Configure the API key
GOOGLE_API_KEY = "AIzaSyDI3-_3fu1U9UD3kpLSlX5p4rUbGzJAz2Q"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get response from the user
def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit Interface
st.set_page_config(page_title="Gemini Chatbot", layout="centered", page_icon="🤖")
st.markdown(
    """
    <style>
        .main {
            background-color: gray;
        }
        .chat-bubble {
            background-color: #e8f5e9;
            border-radius: 10px;
            padding: 10px 15px;
            margin-bottom: 10px;
            display: inline-block;
            color: #000;
        }
        .chat-bubble.user {
            background-color: #bbdefb;
            color: #000;
        }
        .chat-bubble.bot {
            background-color: #000;
            color: #fff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Gemini Chatbot 🤖")
st.write("**Powered by Google Generative AI**")
st.markdown("<hr>", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state["history"] = []

# Chat form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Enter your message:", max_chars=2000, placeholder="Type your message here...")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if user_input:
            response = get_chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
        else:
            st.warning("Please enter a prompt!")

# Display chat history
if st.session_state["history"]:
    st.markdown("<h3>Chat History</h3>", unsafe_allow_html=True)
    for user_msg, bot_msg in st.session_state["history"]:
        st.markdown(
            f"""
            <div class='chat-bubble user'><b>You:</b> {user_msg}</div>
            <div class='chat-bubble bot'><b>Gemini:</b> {bot_msg}</div>
            """,
            unsafe_allow_html=True
        )
