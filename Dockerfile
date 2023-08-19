# syntax=docker/dockerfile:1
   
FROM python
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000