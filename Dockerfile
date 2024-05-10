
FROM --platform=linux/amd64 python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY mlops_ud/mlops_ud .

EXPOSE 8080

# Command to run on container start
CMD [ "uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8080"]
