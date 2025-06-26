# backend/Dockerfile
FROM python:3.11

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy your backend code
COPY . .

# Run the Flask app
CMD ["python", "app.py"]
