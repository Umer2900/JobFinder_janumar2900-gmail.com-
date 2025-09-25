# JobMatch

JobMatch is a Streamlit-based web application designed to help candidates find personalized job opportunities. Powered by the Gemini API for resume analysis and NLP techniques for job matching, JobMatch extracts skills, experience, and job roles from a candidate's resume and recommends the top 5 job matches sourced from real-time data on Naukri.com using web scraping. The platform offers a seamless and user-friendly experience for job seekers, with features for secure account management and job applications.

## Features

- **Resume Analysis**: Upload a PDF resume, and the Gemini API extracts skills, experience, and job roles.
- **Personalized Job Recommendations**: Using NLP techniques (TF-IDF vectorization and cosine similarity), the platform matches your resume with the top 5 job opportunities scraped from Naukri.com, including job title, company, location, and direct application links.
- **Secure Authentication**: Create an account with email verification, log in securely, and manage your account with options to log out or delete your profile.
- **User-Friendly Interface**: Built with Streamlit, the platform provides an intuitive sidebar navigation to access the homepage, job recommendations, and account management features.
- **Candidate-Focused**: Tailored exclusively for job seekers, ensuring a streamlined experience for finding relevant job opportunities.
- **Web Scraping Integration**: Fetches real-time job listings from Naukri.com to provide up-to-date and relevant job recommendations.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Resume Analysis**: Gemini API for extracting skills, experience, and job roles
- **Job Matching**: NLP techniques using `TfidfVectorizer` and `cosine_similarity` from `scikit-learn`
- **Web Scraping**: Libraries like `beautifulsoup4` and `requests` for scraping job listings from Naukri.com
- **Email Service**: SMTP (Gmail) for sending verification codes
- **Database**: SQLite (or other database, depending on `database.py` implementation)
- **Environment Variables**: Managed via `os.environ` for secure email credentials

## Prerequisites

To run JobMatch locally, ensure you have the following installed:
- Python 3.8+
- Streamlit
- Required Python packages (listed in `requirements.txt`)
- A Gmail account with an App Password for email verification
- Access to the Gemini API (configure API key as needed)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/jobmatch.git
   cd jobmatch
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


4. **Configure Environment Variables**:
   Create a `.env` file in the project root and add the following:
   ```plaintext
   GMAIL_USER=your-email@gmail.com
   GMAIL_APP_PASSWORD=your-app-password
   GEMINI_API_KEY=your-gemini-api-key
   ```
   Replace `your-email@gmail.com` with your Gmail address, `your-app-password` with a Gmail App Password (generate one in your Google Account settings), and `your-gemini-api-key` with your Gemini API key.

5. **Run the Application**:
   ```bash
   streamlit run main.py
   ```
   The app will be available at `http://localhost:8501`.


## Job Matching Process

The job recommendation system uses NLP to match resumes with job listings:
- **Resume Parsing**: The Gemini API extracts relevant details (skills, experience, job roles) from the uploaded PDF resume.
- **Vectorization**: Job descriptions from Naukri.com and the parsed resume text are vectorized using `TfidfVectorizer` from `scikit-learn`.
- **Similarity Calculation**: Cosine similarity is computed between the resume vector and job vectors to identify the top 5 most relevant jobs.
- **Output**: Results are displayed in an HTML table with clickable application links.


---
*Last Updated: September 25, 2025*