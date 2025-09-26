from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st

# Load the environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]           # REPLACEMENT CODE (for Streamlit Cloud)

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel(model_name="gemini-1.5-flash")   # OLD
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")


def parse_resume_for_candidate(resume_text):
    response = model.generate_content(
        f"""
        You are an expert resume analyst.

        From the candidate's resume text provided below, extract and return the following three fields:

        1. JobRole
        2. Experience (special format instructions, with extra importance)
        3. Skills

        **Important Instructions:**
        - **JobRole**: Identify the main jobRole candidate wants to apply for.
        - **Experience**: Calculate the total professional experience by adding all durations from different companies.
          - Format the experience naturally:
            - **First bullet**: Write only the total experience in plain format (e.g., "2 years 4 months" or "10 months").
              - If more than 1 year: "X years Y months" (e.g., "2 years 4 months").
              - If less than 1 year: only months (e.g., "10 months").
        
        - **Skills**: Extract and list the candidate's main skills normally.
        - **Format the output as plain text** as shown below:

          1. JobRole: (Mention the jobRole)

          2. Experience: (Mention the experience)


          3. Skills:
          - (Skill 1)
          - (Skill 2)
          - (Skill 3)
          - (Skill 4)
          - (Skill 5)

        - Add one blank line between each section.
        - No extra commentary.

        Resume Text:
        {resume_text}
        """
    )
    return response.text

