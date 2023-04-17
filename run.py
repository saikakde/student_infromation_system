from sis import create_app
from dotenv import load_dotenv
from os import getenv

app = create_app()

load_dotenv('.env')
app.secret_key = os.environ.get('SECRET_KEY')
if __name__ == '__main__':
    app.run()
    