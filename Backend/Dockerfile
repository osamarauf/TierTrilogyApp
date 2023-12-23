FROM python:3.8-slim
WORKDIR /BACKEND
COPY . .
EXPOSE 5000
RUN apt-get update && apt-get install -y curl
RUN pip install -r requirements.txt
CMD [ "python", "app.py"] 