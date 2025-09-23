# JobMatch

JobMatch is a Streamlit-based web application designed to help candidates find personalized job opportunities. Powered by the Gemini API, JobMatch analyzes a candidate's resume to recommend the top 5 job matches based on their skills, experience, and job role. The platform offers a seamless and user-friendly experience for job seekers, with features for secure account management and job applications.

## Features

- **Personalized Job Recommendations**: Upload a PDF resume, and the AI-powered system matches you with the top 5 job opportunities, including job title, company, location, and direct application links.
- **Secure Authentication**: Create an account with email verification, log in securely, and manage your account with options to log out or delete your profile.
- **User-Friendly Interface**: Built with Streamlit, the platform provides an intuitive sidebar navigation to access the homepage, job recommendations, and account management features.
- **Candidate-Focused**: Tailored exclusively for job seekers, ensuring a streamlined experience for finding relevant job opportunities.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Integration**: Gemini API for resume analysis and job matching
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