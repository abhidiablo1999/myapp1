# Use a base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt psycopg2-binary

# Copy backend files
COPY . /app/

# Expose port
EXPOSE 5000

ENV PORT=5000

# Command to run the backend
CMD ["python", "app.py"]
