import logging
from dotenv import load_dotenv
from app.base.redis import flushall_redis
from app.test_case import run_test_market_buy
from app.base.db import truncate_db

load_dotenv()
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def run() -> None:
    logging.info('Start test new exchange e2e')

    truncate_db()
    flushall_redis()
    run_test_market_buy()


run()
