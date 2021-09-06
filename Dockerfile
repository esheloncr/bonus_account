# pull official base image
FROM python:3.8.3-alpine
# set work directory
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# create the appropriate directories
ENV APP_HOME=/usr/src
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME
# copy project
COPY . $APP_HOME