import streamlit as st
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(api_key='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')  # Replace with your actual API key

# Streamlit app title
st.title("Groq Chatbot")

# Text input for the user's query
user_input = st.text_input("Enter your query:")

# Button to submit the query
if st.button("Submit"):
    if user_input:
        # Make a chat completion request
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama3-8b-8192",
        )
        
        # Extract and display the response
        response = chat_completion.choices[0].message.content
        st.write("Response:")
        st.write(response)
    else:
        st.write("Please enter a query.")
