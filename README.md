# Code3CampProject

## Overview
Code3CampProject is a Django project designed to manage authors, books, publishers, courses, students, and instructors. The project consists of two applications: `App1` and `App2`. Each application includes models, views, templates, and URLs to handle CRUD operations.

## Applications
### App1
Manages authors, books, and publishers.

**Models:**
- **Author**: name, email
- **Book**: title, author, published_date
- **Publisher**: name, address

### App2
Manages courses, students, and instructors.

**Models:**
- **Course**: name, description, start_date
- **Student**: name, email, course
- **Instructor**: name, email, course

## Setup Instructions

### Prerequisites
- Python 3.8+
- Django 5.0.6
- SQLite (default database for Django)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Colline-Ssekiwala/Code3Camp
    cd Code3CampProject
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create and apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```


