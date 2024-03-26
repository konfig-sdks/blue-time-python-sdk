import typing_extensions

from blue_time_python_sdk.apis.tags import TagValues
from blue_time_python_sdk.apis.tags.card_operations_api import CardOperationsApi
from blue_time_python_sdk.apis.tags.payment_gateway_api import PaymentGatewayApi
from blue_time_python_sdk.apis.tags.three_ds_sessions_api import ThreeDsSessionsApi
from blue_time_python_sdk.apis.tags.string_tokens_api import StringTokensApi
from blue_time_python_sdk.apis.tags.tools_api import ToolsApi
from blue_time_python_sdk.apis.tags.payment_gateway_accounts_api import PaymentGatewayAccountsApi
from blue_time_python_sdk.apis.tags.three_ds_merchants_api import ThreeDsMerchantsApi
from blue_time_python_sdk.apis.tags.custom_forms_api import CustomFormsApi
from blue_time_python_sdk.apis.tags.cvv_operations_api import CvvOperationsApi
from blue_time_python_sdk.apis.tags.network_token_api import NetworkTokenApi
from blue_time_python_sdk.apis.tags.utils_api import UtilsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CARD_OPERATIONS: CardOperationsApi,
        TagValues.PAYMENT_GATEWAY: PaymentGatewayApi,
        TagValues.THREE_DS_SESSIONS: ThreeDsSessionsApi,
        TagValues.STRING_TOKENS: StringTokensApi,
        TagValues.TOOLS: ToolsApi,
        TagValues.PAYMENT_GATEWAY_ACCOUNTS: PaymentGatewayAccountsApi,
        TagValues.THREE_DS_MERCHANTS: ThreeDsMerchantsApi,
        TagValues.CUSTOM_FORMS: CustomFormsApi,
        TagValues.CVV_OPERATIONS: CvvOperationsApi,
        TagValues.NETWORK_TOKEN: NetworkTokenApi,
        TagValues.UTILS: UtilsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CARD_OPERATIONS: CardOperationsApi,
        TagValues.PAYMENT_GATEWAY: PaymentGatewayApi,
        TagValues.THREE_DS_SESSIONS: ThreeDsSessionsApi,
        TagValues.STRING_TOKENS: StringTokensApi,
        TagValues.TOOLS: ToolsApi,
        TagValues.PAYMENT_GATEWAY_ACCOUNTS: PaymentGatewayAccountsApi,
        TagValues.THREE_DS_MERCHANTS: ThreeDsMerchantsApi,
        TagValues.CUSTOM_FORMS: CustomFormsApi,
        TagValues.CVV_OPERATIONS: CvvOperationsApi,
        TagValues.NETWORK_TOKEN: NetworkTokenApi,
        TagValues.UTILS: UtilsApi,
    }
)
