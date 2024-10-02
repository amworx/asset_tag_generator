# Use your base image, for example:
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy your existing application code
COPY . /app

# Install MySQL connector library
RUN pip install mysql-connector-python

# Copy database initialization script
COPY database/init_db.py /app/database/init_db.py

# Run the initialization script (optional, depending on your setup)
CMD ["python", "database/init_db.py"]
