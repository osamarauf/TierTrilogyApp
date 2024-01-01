FROM postgres:latest
WORKDIR /app
COPY . .
EXPOSE 5432
CMD ["postgres", "-c", "config_file=/app/.env"]