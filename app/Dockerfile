# Use official lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install dependencies
RUN pip install flask

# Expose the app port
EXPOSE 5000

# Command to run app
CMD ["python", "app.py"]
