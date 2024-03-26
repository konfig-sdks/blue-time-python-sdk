import typing_extensions

from blue_time_python_sdk.paths import PathValues
from blue_time_python_sdk.apis.paths.custom_forms import CustomForms
from blue_time_python_sdk.apis.paths.custom_forms_name import CustomFormsName
from blue_time_python_sdk.apis.paths.three_ds_merchants import ThreeDsMerchants
from blue_time_python_sdk.apis.paths.three_ds_merchants_name import ThreeDsMerchantsName
from blue_time_python_sdk.apis.paths.card_operations import CardOperations
from blue_time_python_sdk.apis.paths.card_operations_validate import CardOperationsValidate
from blue_time_python_sdk.apis.paths.card_operations_charge import CardOperationsCharge
from blue_time_python_sdk.apis.paths.card_operations_store import CardOperationsStore
from blue_time_python_sdk.apis.paths.card_operations_op_validate import CardOperationsOpValidate
from blue_time_python_sdk.apis.paths.card_operations_top_brands import CardOperationsTopBrands
from blue_time_python_sdk.apis.paths.card_operations_brand import CardOperationsBrand
from blue_time_python_sdk.apis.paths.cvv_operations import CvvOperations
from blue_time_python_sdk.apis.paths.cvv_operations_charge import CvvOperationsCharge
from blue_time_python_sdk.apis.paths.cvv_operations_op_validate import CvvOperationsOpValidate
from blue_time_python_sdk.apis.paths.network_token import NetworkToken
from blue_time_python_sdk.apis.paths.payment_gateway_accounts_name import PaymentGatewayAccountsName
from blue_time_python_sdk.apis.paths.payment_gateway_accounts import PaymentGatewayAccounts
from blue_time_python_sdk.apis.paths.payment_gateway import PaymentGateway
from blue_time_python_sdk.apis.paths.payment_gateway_charge import PaymentGatewayCharge
from blue_time_python_sdk.apis.paths.payment_gateway_authorize import PaymentGatewayAuthorize
from blue_time_python_sdk.apis.paths.payment_gateway_capture import PaymentGatewayCapture
from blue_time_python_sdk.apis.paths.payment_gateway_refund import PaymentGatewayRefund
from blue_time_python_sdk.apis.paths.payment_gateway_void import PaymentGatewayVoid
from blue_time_python_sdk.apis.paths.three_ds_sessions import ThreeDsSessions
from blue_time_python_sdk.apis.paths.three_ds_sessions_op_validate import ThreeDsSessionsOpValidate
from blue_time_python_sdk.apis.paths.three_ds_sessions_challenge_status import ThreeDsSessionsChallengeStatus
from blue_time_python_sdk.apis.paths.three_ds_sessions_mpi_challenge_callback_session_id import ThreeDsSessionsMpiChallengeCallbackSessionId
from blue_time_python_sdk.apis.paths.three_ds_sessions_fingerprint_callback_session_id import ThreeDsSessionsFingerprintCallbackSessionId
from blue_time_python_sdk.apis.paths.utils_api_key import UtilsApiKey
from blue_time_python_sdk.apis.paths.tools_brand import ToolsBrand
from blue_time_python_sdk.apis.paths.string_tokens import StringTokens
from blue_time_python_sdk.apis.paths.tools_iin import ToolsIin
from blue_time_python_sdk.apis.paths.string_tokens_token import StringTokensToken
from blue_time_python_sdk.apis.paths.string_tokens_token_meta import StringTokensTokenMeta
from blue_time_python_sdk.apis.paths.tools_validate import ToolsValidate
from blue_time_python_sdk.apis.paths.tools_luhn import ToolsLuhn

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CUSTOM_FORMS: CustomForms,
        PathValues.CUSTOM_FORMS_NAME: CustomFormsName,
        PathValues.THREE_DS_MERCHANTS: ThreeDsMerchants,
        PathValues.THREE_DS_MERCHANTS_NAME: ThreeDsMerchantsName,
        PathValues.CARD_OPERATIONS: CardOperations,
        PathValues.CARD_OPERATIONS_VALIDATE: CardOperationsValidate,
        PathValues.CARD_OPERATIONS_CHARGE: CardOperationsCharge,
        PathValues.CARD_OPERATIONS_STORE: CardOperationsStore,
        PathValues.CARD_OPERATIONS_OP_VALIDATE: CardOperationsOpValidate,
        PathValues.CARD_OPERATIONS_TOP_BRANDS: CardOperationsTopBrands,
        PathValues.CARD_OPERATIONS_BRAND: CardOperationsBrand,
        PathValues.CVV_OPERATIONS: CvvOperations,
        PathValues.CVV_OPERATIONS_CHARGE: CvvOperationsCharge,
        PathValues.CVV_OPERATIONS_OP_VALIDATE: CvvOperationsOpValidate,
        PathValues.NETWORK_TOKEN: NetworkToken,
        PathValues.PAYMENT_GATEWAY_ACCOUNTS_NAME: PaymentGatewayAccountsName,
        PathValues.PAYMENT_GATEWAY_ACCOUNTS: PaymentGatewayAccounts,
        PathValues.PAYMENT_GATEWAY: PaymentGateway,
        PathValues.PAYMENT_GATEWAY_CHARGE: PaymentGatewayCharge,
        PathValues.PAYMENT_GATEWAY_AUTHORIZE: PaymentGatewayAuthorize,
        PathValues.PAYMENT_GATEWAY_CAPTURE: PaymentGatewayCapture,
        PathValues.PAYMENT_GATEWAY_REFUND: PaymentGatewayRefund,
        PathValues.PAYMENT_GATEWAY_VOID: PaymentGatewayVoid,
        PathValues.THREE_DS_SESSIONS: ThreeDsSessions,
        PathValues.THREE_DS_SESSIONS_OP_VALIDATE: ThreeDsSessionsOpValidate,
        PathValues.THREE_DS_SESSIONS_CHALLENGE_STATUS: ThreeDsSessionsChallengeStatus,
        PathValues.THREE_DS_SESSIONS_MPI_CHALLENGE_CALLBACK_SESSION_ID: ThreeDsSessionsMpiChallengeCallbackSessionId,
        PathValues.THREE_DS_SESSIONS_FINGERPRINT_CALLBACK_SESSION_ID: ThreeDsSessionsFingerprintCallbackSessionId,
        PathValues.UTILS_API_KEY: UtilsApiKey,
        PathValues.TOOLS_BRAND: ToolsBrand,
        PathValues.STRING_TOKENS: StringTokens,
        PathValues.TOOLS_IIN: ToolsIin,
        PathValues.STRING_TOKENS_TOKEN: StringTokensToken,
        PathValues.STRING_TOKENS_TOKEN_META: StringTokensTokenMeta,
        PathValues.TOOLS_VALIDATE: ToolsValidate,
        PathValues.TOOLS_LUHN: ToolsLuhn,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CUSTOM_FORMS: CustomForms,
        PathValues.CUSTOM_FORMS_NAME: CustomFormsName,
        PathValues.THREE_DS_MERCHANTS: ThreeDsMerchants,
        PathValues.THREE_DS_MERCHANTS_NAME: ThreeDsMerchantsName,
        PathValues.CARD_OPERATIONS: CardOperations,
        PathValues.CARD_OPERATIONS_VALIDATE: CardOperationsValidate,
        PathValues.CARD_OPERATIONS_CHARGE: CardOperationsCharge,
        PathValues.CARD_OPERATIONS_STORE: CardOperationsStore,
        PathValues.CARD_OPERATIONS_OP_VALIDATE: CardOperationsOpValidate,
        PathValues.CARD_OPERATIONS_TOP_BRANDS: CardOperationsTopBrands,
        PathValues.CARD_OPERATIONS_BRAND: CardOperationsBrand,
        PathValues.CVV_OPERATIONS: CvvOperations,
        PathValues.CVV_OPERATIONS_CHARGE: CvvOperationsCharge,
        PathValues.CVV_OPERATIONS_OP_VALIDATE: CvvOperationsOpValidate,
        PathValues.NETWORK_TOKEN: NetworkToken,
        PathValues.PAYMENT_GATEWAY_ACCOUNTS_NAME: PaymentGatewayAccountsName,
        PathValues.PAYMENT_GATEWAY_ACCOUNTS: PaymentGatewayAccounts,
        PathValues.PAYMENT_GATEWAY: PaymentGateway,
        PathValues.PAYMENT_GATEWAY_CHARGE: PaymentGatewayCharge,
        PathValues.PAYMENT_GATEWAY_AUTHORIZE: PaymentGatewayAuthorize,
        PathValues.PAYMENT_GATEWAY_CAPTURE: PaymentGatewayCapture,
        PathValues.PAYMENT_GATEWAY_REFUND: PaymentGatewayRefund,
        PathValues.PAYMENT_GATEWAY_VOID: PaymentGatewayVoid,
        PathValues.THREE_DS_SESSIONS: ThreeDsSessions,
        PathValues.THREE_DS_SESSIONS_OP_VALIDATE: ThreeDsSessionsOpValidate,
        PathValues.THREE_DS_SESSIONS_CHALLENGE_STATUS: ThreeDsSessionsChallengeStatus,
        PathValues.THREE_DS_SESSIONS_MPI_CHALLENGE_CALLBACK_SESSION_ID: ThreeDsSessionsMpiChallengeCallbackSessionId,
        PathValues.THREE_DS_SESSIONS_FINGERPRINT_CALLBACK_SESSION_ID: ThreeDsSessionsFingerprintCallbackSessionId,
        PathValues.UTILS_API_KEY: UtilsApiKey,
        PathValues.TOOLS_BRAND: ToolsBrand,
        PathValues.STRING_TOKENS: StringTokens,
        PathValues.TOOLS_IIN: ToolsIin,
        PathValues.STRING_TOKENS_TOKEN: StringTokensToken,
        PathValues.STRING_TOKENS_TOKEN_META: StringTokensTokenMeta,
        PathValues.TOOLS_VALIDATE: ToolsValidate,
        PathValues.TOOLS_LUHN: ToolsLuhn,
    }
)
