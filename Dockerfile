#use python as a base image
FROM tiangolo/uwsgi-nginx-flask:python3.7


#working directory
WORKDIR /app

#copy all the files which are required for our project would be copy in app folder
COPY requirements.txt /app
COPY templates /app/templates
COPY model.pkl /app


#this file will install all the dependencies in our virtual env
RUN pip install -r ./requirements.txt

COPY main.py /app