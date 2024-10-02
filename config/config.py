import os

# Set configuration variables
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Uncomment if using a database
# SQLALCHEMY_TRACK_MODIFICATIONS = False
