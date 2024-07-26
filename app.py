from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

import streamlit as st
import os
import textwrap
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Load API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API key not found. Please set it in the .env file.")

# Function to Get AI Response 
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Streamlit Application Setup
st.set_page_config(page_title="Q&A Demo", page_icon=":sparkles:", layout="centered")

# Customizing the header
st.title("Gemini Application :sparkles:")
st.markdown("## Ask your question and get responses from the AI")

# User input section with improved layout
input_question = st.text_input("Enter your question:", key="input", help="Type your question here and press the button to get a response.")

# Adding a button with a better design
submit = st.button("Ask the Question", key="submit")

# Handling User Interaction
if submit:
    if input_question:
        with st.spinner('Getting response...'):
            response = get_gemini_response(input_question)
        st.subheader("The Response is")
        st.success(response)
    else:
        st.error("Please enter a question.")
