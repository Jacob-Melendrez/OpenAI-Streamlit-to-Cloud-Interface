import streamlit as st 
import openai
import os 

openai.api_key = st.secrets["openai"]["api_key"]

st.set_page_config(layout="wide")
st.title ("Streamlit Web App")
st.subheader("This is also a Subheader")
st.header("This is a header.")
st.text("This is a long string of text so you can see what text looks like in the streamlit web application.")

# First user input. 
movie = st.text_input("What's your favorite movie?")
st.write(f"Your favorite movie is: {movie}")

prompt = st.text_input("Ask something to OpenAI")

if st.button("Get OpenAI Response"):
    try:
        # Correct API method: ChatCompletion
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # Or use "gpt-4" if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )

        # Access the content correctly
        assistant_response = response['choices'][0]['text'].strip()

        # Display the response
        st.text_area("OpenAI's Response", assistant_response)

    except Exception as e:
        st.error(f"Error: {e}")