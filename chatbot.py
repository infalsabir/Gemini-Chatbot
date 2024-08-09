# using Streamlit
import streamlit as st
import google.generativeai as genai

# Configure the global Generative AI API
API_KEY = "AIzaSyCLFYTD2P4S8KXLU0r7lhCvJ3C0y-reoSI"
genai.configure(api_key=API_KEY)

# Initialize the model

model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text


# Streamlit UI
st.title("Generative AI Model")

# Get user input through a text input box
user_input = st.text_input("Enter your text here")

# craete a button that when clicked, will generate the response
if st.button("Generate Response"):
    if user_input:
        output = getResponseFromModel(user_input)
        st.write(f"Chatbot Response: {output}")
    else:
            st.write("Please enter some text to generate a response")


# user_input = input("Enter Your Prompt = ")
# output = getResponseFromModel(user_input)
# print(output)