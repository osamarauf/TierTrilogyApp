# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --trusted-host pypi.python.org -r Backend/requirements.txt
EXPOSE 5000
CMD ["python", "Backend/app/app.py"]