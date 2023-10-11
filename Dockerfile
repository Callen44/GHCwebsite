# syntax=docker/dockerfile:1
   
FROM python
WORKDIR /app
RUN apt update
RUN apt install nginx -y
RUN mkdir /staticfiles
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN cp /app/config/nginx.conf /etc/nginx/conf.d
CMD ["python","manage.py","boot"]
EXPOSE 80