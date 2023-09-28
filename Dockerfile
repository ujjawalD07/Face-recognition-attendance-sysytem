# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . .
# Expose a port that the application will listen on
EXPOSE 8080

# Define environment variable
ENV APP_ENV env

# Run the command to start your application
CMD ["python", "attendance_system.py"]
