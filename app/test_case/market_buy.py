import logging
from requests import RequestException

from app.base import create_order
from app.base.constant import FRIST_USER_ID, SECOND_USER_ID, UNI, USDT
from app.base.common_enum import OrderType, OrderClass
from app.base.dto import CreateOrderDto
from app.base.db import exchange_connection


def _buy_sell_same_value() -> None:
    """
        - T1 Mở market buy (current price = 40.000) volume = 1 --> hold -40.000
        - T2 Mở sell limit, price = 40.000, volume = 1
        Expected:
        - Amount = -40.000
        - Resolved_amount = -40.000,
        - Rollbacked = 0
        - Balance_locks.status update từ Locked --> Resolved,
        - Order.status = Filled
    """
    logging.info('Start test market buy and sell same value')

    try:
        data_order_market_buy: CreateOrderDto = CreateOrderDto(order_type=OrderType.BUY,
                                                               order_class=OrderClass.MARKET,
                                                               coin=UNI,
                                                               currency=USDT,
                                                               price='40000',
                                                               volume='1')

        data_order_limit_sell: CreateOrderDto = CreateOrderDto(order_type=OrderType.SELL,
                                                               order_class=OrderClass.LIMIT,
                                                               coin=UNI,
                                                               currency=USDT,
                                                               price='40000',
                                                               volume='1')

        create_order(FRIST_USER_ID, data_order_market_buy)
        create_order(SECOND_USER_ID, data_order_limit_sell)

    except RequestException as err:
        logging.error(err)
        raise err
    except Exception as e:
        logging.error(e)
        raise e


def run_test_market_buy():
    logging.info('Run test market buy')
    _buy_sell_same_value()
