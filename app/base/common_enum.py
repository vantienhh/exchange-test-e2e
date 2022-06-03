from enum import IntEnum


class OrderClass(IntEnum):
    MARKET = 1
    LIMIT = 2
    STOP_MARKET = 3
    STOP_LIMIT = 4


class OrderStatus(IntEnum):
    PENDING = 1
    FILLED = 2
    CANCELED = 3
    ERROR = 4
#    PartialFilled = 5
    PROCESSING_CANCEL = 6


class OrderType (IntEnum):
    BUY = 1
    SELL = 2


class UserType (IntEnum):
    USER = 1
    BOT_A = 2
    BOT_P = 3
    GATEKEPPER = 4


class StopDirection (IntEnum):
    UNDEFINED = 0
    UP = 1
    DOWN = 2


class OrderTransactionStatus(IntEnum):
    PENDING = 1
    SUCCESS = 2
