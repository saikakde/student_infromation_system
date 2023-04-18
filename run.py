from sis import create_app
from dotenv import load_dotenv
# from os import getenv
import os

app = create_app()

load_dotenv('.env')
# app.secret_key = os.environ.get('SECRET_KEY')
app.secret_key = os.getenv('SECRET_KEY')

if __name__ == '__main__':
    app.run(debug = True)
    