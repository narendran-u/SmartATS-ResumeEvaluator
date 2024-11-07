

---

# SmartATS-ResumeEvaluator

**SmartATS-ResumeEvaluator** is an AI-powered resume evaluation tool designed to assess resumes against job descriptions with high precision. Utilizing Google’s Generative AI models, this Application Tracking System (ATS) matches resume skills, keywords, and experience to the demands of specific job postings. Built with a streamlined interface in Streamlit, the app provides actionable feedback and highlights missing keywords and skills to help candidates improve their resumes.

### Live Demo
Explore the live application here: [SmartATS-ResumeEvaluator on Streamlit](https://smartats-resumeevaluator.streamlit.app/)

## Features
- **AI-Powered Resume Matching**: Uses Google’s LLM models to match resumes against job descriptions and provide a match percentage.
- **Missing Keywords Detection**: Identifies essential keywords and skills missing from the resume based on the job description.
- **Profile Summary**: Provides a summary analysis of the resume’s alignment with the job description, including actionable feedback.
- **Interactive Interface**: Built with Streamlit for a simple, interactive, and user-friendly experience.

## Technology Stack
- **Streamlit**: Frontend framework for building a fast and interactive user interface.
- **PyPDF2**: Library for parsing PDF files, allowing users to upload resumes in PDF format.
- **google.generativeai**: Utilized for the LLM-based evaluation of resumes and job descriptions.
- **python-dotenv**: Used to manage environment variables, including API keys securely.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/SmartATS-ResumeEvaluator.git
   cd SmartATS-ResumeEvaluator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your API key for Google Generative AI:
     ```plaintext
     GOOGLE_API_KEY=your_google_api_key
     ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Upload a resume (PDF format) to the app.
2. Paste the job description in the provided field.
3. The app will analyze and display:
   - **JD Match**: Percentage match of the resume with the job description.
   - **Missing Keywords**: Key terms and skills missing in the resume.
   - **Profile Summary**: A detailed summary of alignment and suggested improvements.

## Contributing
Contributions are welcome! If you’d like to improve this project or add features, please submit a pull request.

## License
This project is licensed under the MIT License.

---
