from typing import TypedDict
from app.base.common_enum import OrderType, OrderClass


class CreateOrderDto(TypedDict):
    order_type: OrderType
    order_class: OrderClass
    coin: str
    currency: str
    price: str
    volume: str
