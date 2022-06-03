import logging
import redis
from os import environ


def get_redis() -> redis.Redis:
    host = environ['REDIS_EXCHANGE_HOST']
    port = int(environ['REDIS_EXCHANGE_PORT'])

    return redis.Redis(host=host, port=port)


def flushall_redis():
    logging.info('Flushall redis')
    redis_client = get_redis()
    redis_client.flushall()
