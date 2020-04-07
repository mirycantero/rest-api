# RESTful API using Python and Flask

## Prerequisites

### Python

Make sure you have `python 3.7.x` installed.

        $ python3 --version

And that you have `virtualenv`

        $ pip install virtualenv
        $ virtualenv --version

## Quick start

1.  Clone the Project repository.

        $ git clone git@github.com:mirycantero/rest-api.git
        $ cd rest-api

2.  Initialize and activate a virtualenv:

        $ virtualenv --python python3 env
        $ source env/bin/activate

3.  Install the dependencies:

        (env) $ pip install -r requirements.txt

4.  Environment variables:

    Create a copy of `.env.example` and rename it as `.env`:

        (env) $ cp .env.example .env

    Set the needed environment in the `.env` file, if you are running this locally:

        # Environment
        FLASK_ENV=local

5.  Make sure you have a `json` file for the environment needed inside `/instance` folder, you can base it on `default.json` and set the needed variables. E.g. you would end up with a `./instance/local.json` file.

6.  Set your database configuration keys in the json file created in the previous step.

7.  To populate the database activate the following flag in the json file:

        "INITIALIZE_DATA": true

8.  Run the application:

        (env) $ python main.py

## Running the app - Docker

### Docker Build

To build the docker image, make sure that you are on the `root of the project` and run:

        docker build -t docker-flask-app:latest .

### Docker Run

You can run the build you just created with the `docker run` command.

       docker run -d -p 8080:8080 docker-flask-app:latest
