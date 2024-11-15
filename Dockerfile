# Base image
FROM python:3.12-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code into the container
COPY app.py .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set the entry point command to run the Flask app
CMD ["python", "app.py"]
