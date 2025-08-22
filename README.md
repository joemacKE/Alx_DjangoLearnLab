Social Media API
A Django RESTful API for a social media platform, featuring user accounts, posts, and notifications.

Features
User authentication (custom user model)
Token-based authentication (DRF)
CRUD operations for posts
Notifications system
Secure settings for production
PostgreSQL database support
Project Structure

PROJECT STRUCTURE
accounts/         # User management (custom user model, authentication)
posts/            # Post creation, retrieval, update, deletion
notifications/    # User notifications
social_media_api/ # Project settings and configuration
manage.py         # Django management script
requirements.txt  # Python dependencies
.env              # Environment variables (not committed)

Setup
Prerequisites
Python 3.8+
PostgreSQL
pip

Installation
1. Clone the repository:
git clone https://github.com/joemacKE/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab then cd to social_media_api

2. CREATE AND ACTIVATE A VIRTUAL ENVIRONMENT:
   python3 -m venv env
   source env/bin/activate
3. Install dpendencies
   pip install -r requirements.txt
4. Configure environment variables
   SECRET_KEY=your-secret-key
    DEBUG=True
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=5432
5. Apply migrations
   python manage.py makemigrations
   python manage.py migrate
6. Create superuser
   python manage.py createsuperuser
7. Run development server
   python manage.py runserver

API Authentication
  Uses token-based authentication.
  Obtain a token by posting username and password to /api-token-auth/.


