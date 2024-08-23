import streamlit as st
import google.generativeai as genai
import requests
import io
from PIL import Image

# Set up the Streamlit app
st.title("Welcome to StellarAI")

# Configure the Google Generative AI with your API key
genai.configure(api_key="AIzaSyAf4lE0j4NsLAHUICbQjD3WIS8etmeirOY")

# Get user input from Streamlit
user_input = st.text_input("Enter your input:")

# Layout for buttons
col1, col2 = st.columns(2)

# Generate Text
if col1.button('Generate Text'):
    if user_input:
        # Initialize the generative model
        model = genai.GenerativeModel('gemini-pro')
        
        # Start a chat session
        chat = model.start_chat(history=[])
        
        # Send the message and get a response
        response = chat.send_message(user_input)
        
        # Display the response in the Streamlit app
        st.write(response.text)

# Generate Image
if col2.button('Generate Image'):
    if user_input:
        API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.content

        image_bytes = query({"inputs": user_input})
        
        # Display the generated image
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image)
