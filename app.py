import os
import streamlit as st
from langchain_openai import OpenAI

# Input for API key
apikey = st.text_input("Enter your OpenAI API key:", type="password", key="api_key_input")

# Set the API key environment variable
if apikey:
    os.environ['OPENAI_API_KEY'] = apikey

# Display media files
st.audio("ttop008-67017.mp3")
st.image("6e8b479a2c76dbe51c6f92c81d9e9f8f.gif")

st.title(" 🦜️🔗This is a Dummy Website 🧟‍♂️")
#prompt = st.text_input("Type your homework question below", key="homework_prompt_input")

# LLMs
if apikey and prompt:
    llm = OpenAI(temperature=0.9)
    response = llm(prompt)
    st.write(response)
elif not apikey:
    st.warning("Please enter your OpenAI API key to proceed.")

with st.sidebar:
    st.write("About me")
    st.write("Keep Study and Work Hard")
    st.image("4364_gif_wh860.gif")
