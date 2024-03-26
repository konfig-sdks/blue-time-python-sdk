# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from blue_time_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CUSTOM_FORMS = "/CustomForms"
    CUSTOM_FORMS_NAME = "/CustomForms/{name}"
    THREE_DS_MERCHANTS = "/ThreeDsMerchants"
    THREE_DS_MERCHANTS_NAME = "/ThreeDsMerchants/{name}"
    CARD_OPERATIONS = "/CardOperations"
    CARD_OPERATIONS_VALIDATE = "/CardOperations/validate"
    CARD_OPERATIONS_CHARGE = "/CardOperations/charge"
    CARD_OPERATIONS_STORE = "/CardOperations/store"
    CARD_OPERATIONS_OP_VALIDATE = "/CardOperations/opValidate"
    CARD_OPERATIONS_TOP_BRANDS = "/CardOperations/topBrands"
    CARD_OPERATIONS_BRAND = "/CardOperations/brand"
    CVV_OPERATIONS = "/CvvOperations"
    CVV_OPERATIONS_CHARGE = "/CvvOperations/charge"
    CVV_OPERATIONS_OP_VALIDATE = "/CvvOperations/opValidate"
    NETWORK_TOKEN = "/NetworkToken"
    PAYMENT_GATEWAY_ACCOUNTS_NAME = "/PaymentGatewayAccounts/{name}"
    PAYMENT_GATEWAY_ACCOUNTS = "/PaymentGatewayAccounts"
    PAYMENT_GATEWAY = "/PaymentGateway"
    PAYMENT_GATEWAY_CHARGE = "/PaymentGateway/charge"
    PAYMENT_GATEWAY_AUTHORIZE = "/PaymentGateway/authorize"
    PAYMENT_GATEWAY_CAPTURE = "/PaymentGateway/capture"
    PAYMENT_GATEWAY_REFUND = "/PaymentGateway/refund"
    PAYMENT_GATEWAY_VOID = "/PaymentGateway/void"
    THREE_DS_SESSIONS = "/ThreeDsSessions"
    THREE_DS_SESSIONS_OP_VALIDATE = "/ThreeDsSessions/opValidate"
    THREE_DS_SESSIONS_CHALLENGE_STATUS = "/ThreeDsSessions/challengeStatus"
    THREE_DS_SESSIONS_MPI_CHALLENGE_CALLBACK_SESSION_ID = "/ThreeDsSessions/mpiChallengeCallback/{sessionId}"
    THREE_DS_SESSIONS_FINGERPRINT_CALLBACK_SESSION_ID = "/ThreeDsSessions/fingerprintCallback/{sessionId}"
    UTILS_API_KEY = "/Utils/apiKey"
    TOOLS_BRAND = "/Tools/brand"
    STRING_TOKENS = "/StringTokens"
    TOOLS_IIN = "/Tools/iin"
    STRING_TOKENS_TOKEN = "/StringTokens/{token}"
    STRING_TOKENS_TOKEN_META = "/StringTokens/{token}/meta"
    TOOLS_VALIDATE = "/Tools/validate"
    TOOLS_LUHN = "/Tools/luhn"
