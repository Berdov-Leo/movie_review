
---

# Movie Review Sentiment Analysis

This is a Django web application that allows users to submit movie reviews and predicts whether the sentiment of the review is positive or negative using a trained machine learning model (Logistic Regression).

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [License](#license)

## Features

- **Submit a Movie Review**: Users can submit a movie review through a form.
- **Sentiment Prediction**: The machine learning model predicts the sentiment of the review (positive or negative).
- **Storage**: Submitted reviews along with predictions are stored in the SQLite database.
- **User Interface**: A simple user interface for submitting reviews and viewing results.

## Installation

To get this project running on your local machine, follow these steps:

### Prerequisites

- Python 3.x
- Django 4.x
- pip

### Step-by-step Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Berdov-Leo/movie_review.git
   cd your_repository_name
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Make migrations and migrate the database:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Collect static files:**

   ```bash
   python manage.py collectstatic
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Enter a movie review in the text area and submit it.
3. The model will predict whether the sentiment is positive or negative, and the result will be displayed on the page.

## Project Structure

```
movie_review/
│
├── movie_review/              # Project configuration files
│   ├── __init__.py
│   ├── settings.py            # Main settings for the Django project
│   ├── urls.py                # URL routing for the project
│   ├── wsgi.py                # WSGI configuration for deploying the project
│
├── reviews/                   # Main app for review processing
│   ├── migrations/            # Database migration files
│   ├── models.py              # Database models (Review model)
│   ├── views.py               # Main view for handling requests
│   ├── forms.py               # Form for submitting reviews
│   ├── templates/             # HTML templates for the project
│   │   ├── review_form.html   # Template for submitting a review
│   │   ├── result.html        # Template for displaying the prediction result
│
├── static/                    # Collected static files (CSS, JS)
│
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django project management script
├── requirements.txt           # Project dependencies
```

## Technologies Used

- **Python**: The core language for the project.
- **Django**: A high-level Python web framework for rapid development.
- **Scikit-learn**: A Python library for machine learning (used for Logistic Regression).
- **SQLite**: Lightweight database used for storing reviews and predictions.
- **Gunicorn**: WSGI HTTP Server used in production for serving Django apps.
- **HTML/CSS**: Used for creating the front-end of the web application.

---