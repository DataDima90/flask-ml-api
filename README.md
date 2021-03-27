# flask-ml-api

## Building a Machine Learning Microservice using Flask, Gunicorn, Nginx and Docker

Here we learn how machine learning models ca be deployed into production in a 
dockerized environment using Flask, Gunicorn and Nginx in Python environment.

**What we do:**
1. We write a simple API and make it easily extendable using Flask Blueprints
2. We make our Flask API production-ready using Gunicorn WSGI
3. We set up the Flask API and Nginx inside docker
4. We assemble our Docker Containers using docker-compose
5. We test our Flask API using pytest

**We cover the following frameworks:**
- Flask
- Gunicorn
- Nginx
- Docker
- Docker-Compose
- Pytest


## Setup

### Prerequisites

#### Create a conda environment

Use the terminal or an Anaconda Prompt for the following steps:

**1. Create an environment**
```
conda create --name <environment-name> python=3.7
```

**2. Activate the new environment:**

```
conda activate <env-name>
```

**3. Install the python dependencies:**

Go to the path where is the requirements file and type:

```
pip install -r requirements.txt
```

**4. Verify that the new environment with the corresponding packages was installed correctly:**

```
conda env list
```

**5. To boot up the default server, you can run:

```
bash api/run.sh
```

This will start a Gunicorn server that wraps the Flask app defined in `api/app.py`.

Now you can test the URL **GET** `http://0.0.0.0:8080/prediction` with Postman: The request body looks like:

```
{
    "pl": 2,
    "sl": 2,
    "pw": 0.5,
    "sw": 3
}
```
If succesful you should see a result like this:

```
{
    "prediction": "Setosa"
}
```


## How to start Docker

This repository contains Dockerfile and Docker Compose for a PostgreSQL database.

Install Docker following the installation guide for your platform: https://docs.docker.com/engine/installation/

#### Start building your docker image

Go to the directory `/api`. To build a containerised version of the API, run:

```
docker build . -t flask-ml-api
```

To launch the containerised app, run:

```
docker run -p 5000:5000 flask-ml-api
```

You should see your server boot up. With Postman you can again test the API via GET request.

## How to start docker-compose

Install Docker Compose following the installation guide for your platform: https://docs.docker.com/compose/install/

#### Start building your docker-compose yml file:

Open a terminal and type: 

```
docker-compose build
docker-compose up
```