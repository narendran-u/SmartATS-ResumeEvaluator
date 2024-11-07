import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt="""
Act as an advanced Application Tracking System (ATS) with comprehensive knowledge in software engineering, data science, data analysis, big data engineering, and other key tech domains. Your task is to evaluate the provided resume based on the given job description (JD), accounting for current competitive job market standards and industry expectations for technical roles. Use a rigorous approach to assess the match between the resume and the JD by identifying crucial keywords, technologies, programming languages, tools, frameworks, methodologies, relevant certifications, and other specific requirements listed in the JD.

Break down and score the following areas:

Skill Match: Identify technical and non-technical skills from the JD that appear on the resume, and note any high-priority missing skills.
Project Relevance: Evaluate projects, tasks, or responsibilities the candidate has completed that align with the job role. Note any missing projects or experience critical to the JD.
Achievements & Impact: Look for quantifiable accomplishments, such as metrics (e.g., improved efficiency by X%, managed data sets of Y size) that demonstrate the candidate's impact. Note missing impact-based accomplishments if relevant.
Educational Alignment: Confirm that the candidate’s academic background aligns with JD requirements, and identify if any key educational qualifications or certifications are missing.
Soft Skills & Cultural Fit: Assess relevant soft skills like communication, problem-solving, and collaboration that match the JD, if included.
Provide your response in a structured JSON format with: "JD Match": "<percentage of match with JD based on overall relevance, missing skills, and experience alignment>", "MissingKeywords": ["list any critical keywords, skills, tools, or certifications missing from the resume that are essential to the role"], "Profile Summary": "<brief summary of the resume’s alignment, including strengths, and provide actionable suggestions for improvement to enhance relevance, clarity, or emphasis on critical areas>"
give evey thing paragraph by paragraph use bulletin points whereever it is needed not cluttered information  dont use { } to give information and use points and paragraphs
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        st.subheader(response)


      