###########
# BUILDER #
###########

# pull official base image
FROM python:3.8.1-slim-buster as builder

# create directory for the app user
RUN mkdir -p /home/app

# set work directory
WORKDIR /home/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV PYTHONIOENCODING=utf8


# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# lint
RUN pip install --upgrade pip
COPY . /home/app/

# install python dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /home/app/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.8.1-slim-buster

# create the app user
RUN adduser app

# create the appropriate directories
ENV APP_HOME=/home/app/
ENV PYTHONIOENCODING=utf8
WORKDIR $APP_HOME

# set timezone
ENV TZ=Asia/Jakarta
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat && apt-get install --reinstall -y locales-all
COPY --from=builder /home/app/wheels /wheels
COPY --from=builder /home/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app