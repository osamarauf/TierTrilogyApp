FROM python:3.8-slim
WORKDIR /app
COPY . .
EXPOSE 5000
RUN pip install -r requirements.txt
CMD [ "python", "app.py", "--host=0.0.0.0", "--port=5000"] 