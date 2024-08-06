FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install necessary system dependencies
RUN apt-get update && \
    apt-get install -y build-essential gcc

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Set the entrypoint
CMD ["python", "daily_sales_data.py"]
