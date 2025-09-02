# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Create directory for allure results
RUN mkdir -p /app/allure-results

# Set the default command to run pytest with allure JSON results only
CMD ["pytest", "test/", "--alluredir=/app/allure-results"]