import requests
from os import environ
from app.base.dto.create_order_dto import CreateOrderDto


def _get_headers(user_id: str) -> dict:
    return {
        'x-bce-uid': user_id,
    }


def create_order(user_id: str, order_data: CreateOrderDto) -> requests.Response:
    """
    Create an order in the Order API
    """
    create_order_url = environ['CREATE_ORDER_URL']

    return requests.post(url=create_order_url, json=order_data, headers=_get_headers(user_id))
