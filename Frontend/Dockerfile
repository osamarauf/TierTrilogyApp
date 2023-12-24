FROM python:3.8-slim
WORKDIR /frontend
COPY . /frontend
EXPOSE 3000
RUN apt-get update && apt-get install -y curl libpq-dev gcc
RUN pip install -r requirements.txt
CMD [ "python", "app.py"] 