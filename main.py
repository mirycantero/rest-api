import os

from dotenv import load_dotenv

from app import create_app

load_dotenv()

FLASK_ENV = os.getenv('FLASK_ENV', 'dev')

app = create_app(FLASK_ENV)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
