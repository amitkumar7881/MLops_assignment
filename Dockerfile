# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose the port that your application will run on (if needed)
# EXPOSE 8080

# Define environment variable (if needed)
# ENV NAME World

# Command to run your machine learning model script
CMD ["python", "Python script.py"]
