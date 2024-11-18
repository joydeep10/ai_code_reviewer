# ai_code_reviewer

Overview
This project is an AI-powered code reviewer built using LangChain and the open-source Gemini models. Designed to automate and streamline Python code reviews, this app analyzes code snippets, identifies potential bugs, and suggests optimized improvements. By providing instant feedback, it helps developers ensure their code is clean, efficient, and error-free.

Features
Bug Detection: Automatically analyzes code for common errors, vulnerabilities, and inefficiencies.
Refactored Suggestions: Generates an optimized version of the input code, improving clarity and performance.
Interactive UI: Built with Streamlit, the user-friendly interface allows users to paste code and view results instantly.

Technology Stack
LangChain: Facilitates model and prompt handling for streamlined code analysis.
Gemini Models: Powers the app’s generative capabilities for analysis and suggestions.
Streamlit: Provides an interactive, responsive UI for users to easily input code and receive feedback.

Project Structure
main.py: Core file containing the Streamlit app setup, model selection, and code processing logic.
CodeReviewer Class: A Pydantic model defining the expected structure of the code review output.
requirements.txt: Dependencies needed to run the project.
