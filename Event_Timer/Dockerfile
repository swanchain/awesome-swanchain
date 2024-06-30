# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the current directory to the container
COPY . /app

# Expose port 8080 to the outside world
EXPOSE 8080

# Run the Python HTTP server when the container launches
CMD ["python", "-m", "http.server", "8080"]
