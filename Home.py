import streamlit as st
from langchain.prompts import PromptTemplate

st.write("hello")

st.write([1, 2, 3, 4])

st.write({"x": 1})

# st.write(PromptTemplate)


p = PromptTemplate.from_template("xxxx")

## magic - just leave it, program will print into screen
p

st.selectbox(
    "Choose your model",
    (
        "GPT-3",
        "GPT-4",
    ),
)