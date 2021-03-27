# api/Dockerfile
FROM python:3.8

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install gcc make \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --no-cache-dir --upgrade pip

# set work directory
WORKDIR /api

# copy requirements.txt
COPY ./requirements.txt /api/requirements.txt

# install project requirements
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /api

# Generate pickle file
WORKDIR /

CMD ["gunicorn", "-w", "3", "-b", ":5000", "-t", "30", "--reload", "api.wsgi:app"]