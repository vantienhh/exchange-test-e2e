from os import environ
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from dotenv import load_dotenv

load_dotenv()

host = environ['DB_EXCHANGE_SLAVE_HOST']
port = environ['DB_EXCHANGE_SLAVE_PORT']
user = environ['DB_EXCHANGE_SLAVE_USERNAME']
password = environ['DB_EXCHANGE_SLAVE_PASSWORD']
database = environ['DB_EXCHANGE_SLAVE_DATABASE']

db_balance_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(db_balance_url)

balance_connection: Connection = engine.connect()
