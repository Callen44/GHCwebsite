# syntax=docker/dockerfile:1
   
FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt update
RUN apt install nginx -y
COPY . .
RUN cp /app/config/nginx.conf /etc/nginx/conf.d
RUN mkdir /staticfiles
CMD ["python","manage.py","boot"]
EXPOSE 80