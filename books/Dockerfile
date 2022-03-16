#Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH "$PATH:C:/Program Files/Mozilla Firefox"

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

