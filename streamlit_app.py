import streamlit as st

st.title("Length of input text")

# Create a text input box and get user input
user_input = st.text_input("Enter some text")

# Calculate length of user input and display it
input_length = len(user_input)
st.write("The input text is", input_length, "characters long")
