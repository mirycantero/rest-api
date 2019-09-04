# RESTful API using Python and Flask

## Prerequisites

### Google Cloud SDK

The Cloud SDK is a set of tools for Cloud Platform. We are using BigQuery, so you will need to set it up:

1. [Install Google Cloud SDK](https://cloud.google.com/sdk/docs/quickstarts)
2. [Initializing Cloud SDK](https://cloud.google.com/sdk/docs/initializing)

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

4.  Make sure you have a `.env` file, you can base it on `.env.example` and set the needed variables. You can use the example values.

5.  Make sure you are logged in to Google Cloud (verify that your Lumiata GCP Account shows up)

        (env) $ gcloud auth list

6.  Run the development server:

        (env) $ python main.py

7.  Navigate to [http://localhost:8080](http://localhost:8080/) or use [postman](https://www.getpostman.com/)s

## Cloud SQL Proxy

1.  Install the proxy (For other operating systems refer [here](https://cloud.google.com/sql/docs/postgres/connect-admin-proxy))

        MacOS 64-bit: curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64

2.  Make the proxy executable

        $ chmod +x cloud_sql_proxy

3.  Start the proxy

        $ ./cloud_sql_proxy -instances=my-first-project-235017:us-central1:rest-api-tutorial=tcp:5432
