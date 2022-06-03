import logging
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

db_exchange_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(db_exchange_url)

exchange_connection: Connection = engine.connect()


def truncate_db():
    logging.info('Start truncate db')

    tables_truncate = [
        'order',
        'order_transaction',
        'failure_process',
        'order_balance_rollback'
    ]

    for table in tables_truncate:
        exchange_connection.execute(f'TRUNCATE TABLE `{table}`')
