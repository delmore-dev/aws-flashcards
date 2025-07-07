   # Use official Python image as base
    FROM python:3.11-slim

    # Set working directory
    WORKDIR /app

    # Copy requirements if you have one, else install manually
     COPY requirements.txt .
    

    # Install Flask and requests
    RUN pip install -r requirements.txt

    # Copy app code
    COPY . .

    # Expose port
    EXPOSE 5000

    # Run the app
    CMD ["python", "app.py"]