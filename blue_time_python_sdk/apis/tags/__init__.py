# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from blue_time_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    CARD_OPERATIONS = "CardOperations"
    PAYMENT_GATEWAY = "PaymentGateway"
    THREE_DS_SESSIONS = "ThreeDsSessions"
    STRING_TOKENS = "StringTokens"
    TOOLS = "Tools"
    PAYMENT_GATEWAY_ACCOUNTS = "PaymentGatewayAccounts"
    THREE_DS_MERCHANTS = "ThreeDsMerchants"
    CUSTOM_FORMS = "CustomForms"
    CVV_OPERATIONS = "CvvOperations"
    NETWORK_TOKEN = "NetworkToken"
    UTILS = "Utils"
