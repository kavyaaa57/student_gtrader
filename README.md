# CERTIFY: Academic Grade Management System

A secure and user-friendly academic grade management system built using Django.

---

## Project Overview

CERTIFY is a web-based academic records management system designed for higher education institutions. It simplifies the process of entering, managing, and retrieving student grades. The system supports multiple user roles including Admin, Faculty, and Student. CERTIFY helps streamline academic workflows such as grade submission, GPA/CGPA calculation, and certificate generation.

---

## Key Features

- Secure login system with role-based access (Admin, Faculty, Student)
- Grade entry (individual and bulk upload)
- GPA and CGPA calculation
- Semester and course management
- PDF generation of grade reports and certificates using ReportLab
- Email notifications for grade updates and announcements

---

## Tech Stack

| Layer        | Technology                |
|--------------|---------------------------|
| Backend      | Django                    |
| Frontend     | HTML, CSS, JavaScript     |
| Database     | SQLite (development), PostgreSQL (production) |
| Authentication | Django Auth + Email OTP |
| PDF Reports  | ReportLab                 |
| Email        | SMTP Integration          |

---

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip
- Virtualenv
- Git

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/yourusername/certify.git
cd certify

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt

# Create a .env file for environment variables
cp .env.example .env
# (Edit the .env file to include secret keys and SMTP configuration)

# Apply database migrations
python manage.py migrate

# Create a superuser for accessing the Django admin panel
python manage.py createsuperuser

# Start the development server
python manage.py runserver

Contributing
We welcome contributions!

Fork the repository

Create a new branch:
git checkout -b feature/your-feature-name

Commit your changes:
git commit -m "Add feature"

Push to your branch:
git push origin feature/your-feature-name

Open a Pull Request on GitHub


