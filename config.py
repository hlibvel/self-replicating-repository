import os

import dotenv


HERE = os.path.abspath(os.path.dirname(__file__))  # the path to the project directory
dotenv.load_dotenv(dotenv_path=f'{HERE}/.env')     # load variables from .env file


CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']

OWNER = os.environ.get('OWNER', 'hlibvel')
REPO_NAME = os.environ.get('REPO_NAME', 'self-replicating-repository')

