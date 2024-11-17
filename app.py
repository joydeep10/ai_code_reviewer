from typing import List
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import google.generativeai as genai
import os
import streamlit as st
from langchain.prompts import PromptTemplate  # Correct import

# App description at the top
st.title("֎ An AI Code Reviewer")
st.write("This app analyzes Python code, identifies bugs, suggests improvements, and provides optimized code.")

# Model initialization (using only Gemini-1.5-Flash)
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = ChatGoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"),
                               model="gemini-1.5-flash",
                               temperature=0)


# Define Pydantic model for code review output
class CodeReviwer(BaseModel):
    title: str = Field(description="Display the text '## Code Reviewer' as a level 2 heading (H2 tag).")
    section_1: str = Field(description="Display the text '### Bug Analysis' as a level 3 heading (H3 tag).")
    intro_bugs: str = Field(description="Below are the issues found in the provided code:")
    issues: List[str] = Field(
        description="Analyze the provided code snippet for potential errors, vulnerabilities, or inefficiencies. Identify and list all anticipated issues directly in a comma-separated format, omitting any subheadings or introductory statements.")
    section_2: str = Field(description="Display the text '### Refactored Code' as a level 3 heading (H3 tag).")
    optimized_code: str = Field(
        description="Provide the optimized version of the code after analysis without any comments in it. Ensure the code is wrapped in triple backticks (```) to format it as a code block.")


# Pydantic output parser for structured results
parser = PydanticOutputParser(pydantic_object=CodeReviwer)

prompt_template = "Assume the role of a meticulous Code Reviewer. Your task is to answer the user's query.\n{format_instructions}\n{query}\n"
prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["query"],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)

chain = prompt | model | parser

# Input text box at the bottom for code review
prompt = st.text_area("Enter your Python code here...", key="code_input")

if st.button("Generate", key="generate_button"):
    response = chain.invoke({"query": prompt})

    # Display structured output
    st.write(response.title)
    st.write(response.section_1)
    st.write(response.intro_bugs)
    for i, issue in enumerate(response.issues, 1):
        st.write(f"{i}. {issue}")
    st.write(response.section_2)
    st.write(response.optimized_code)
