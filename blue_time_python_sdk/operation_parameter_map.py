operation_parameter_map = {
    '/CardOperations/brand-GET': {
        'parameters': [
            {
                'name': 'iin'
            },
        ]
    },
    '/CardOperations-POST': {
        'parameters': [
            {
                'name': 'ttl'
            },
            {
                'name': 'threeDsSessionModel'
            },
            {
                'name': 'vld'
            },
            {
                'name': '3ds'
            },
            {
                'name': 'crg'
            },
            {
                'name': 'tkn'
            },
            {
                'name': 'crg_d'
            },
        ]
    },
    '/CardOperations/topBrands-GET': {
        'parameters': [
        ]
    },
    '/CardOperations/charge-POST': {
        'parameters': [
            {
                'name': 'card'
            },
            {
                'name': 'payerDetails'
            },
            {
                'name': 'myRef'
            },
        ]
    },
    '/CardOperations/validate-POST': {
        'parameters': [
            {
                'name': 'countryCode'
            },
            {
                'name': 'iin'
            },
            {
                'name': 'city'
            },
            {
                'name': 'stateProvince'
            },
        ]
    },
    '/CardOperations/opValidate-GET': {
        'parameters': [
        ]
    },
    '/CardOperations/store-POST': {
        'parameters': [
            {
                'name': 'payload'
            },
        ]
    },
    '/CustomForms-GET': {
        'parameters': [
        ]
    },
    '/CustomForms/{name}-DELETE': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/CustomForms/{name}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'ContentType'
            },
            {
                'name': 'ContentDisposition'
            },
            {
                'name': 'Headers'
            },
            {
                'name': 'Length'
            },
            {
                'name': 'Name'
            },
            {
                'name': 'FileName'
            },
        ]
    },
    '/CvvOperations-POST': {
        'parameters': [
            {
                'name': 'ttl'
            },
            {
                'name': 'card'
            },
            {
                'name': 'crg_d'
            },
        ]
    },
    '/CvvOperations/charge-POST': {
        'parameters': [
            {
                'name': 'cvv'
            },
        ]
    },
    '/CvvOperations/opValidate-GET': {
        'parameters': [
        ]
    },
    '/NetworkToken-POST': {
        'parameters': [
            {
                'name': 'tokenizationRequest'
            },
            {
                'name': 'card'
            },
        ]
    },
    '/NetworkToken-DELETE': {
        'parameters': [
            {
                'name': 'source'
            },
            {
                'name': 'tokenId'
            },
            {
                'name': 'brand'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/PaymentGateway-GET': {
        'parameters': [
        ]
    },
    '/PaymentGateway/authorize-POST': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'card'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'isDigital'
            },
            {
                'name': 'orderDesc'
            },
            {
                'name': 'payerDetails'
            },
            {
                'name': 'myRef'
            },
            {
                'name': 'paymentGatewayAccountName'
            },
            {
                'name': 'certificateName'
            },
            {
                'name': 'paymentGatewayAccount'
            },
            {
                'name': 'networkTokenBrand'
            },
        ]
    },
    '/PaymentGateway/capture-PUT': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'refTransId'
            },
            {
                'name': 'card'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'myRef'
            },
            {
                'name': 'paymentGatewayAccountName'
            },
            {
                'name': 'certificateName'
            },
            {
                'name': 'paymentGatewayAccount'
            },
            {
                'name': 'networkTokenBrand'
            },
        ]
    },
    '/PaymentGateway/charge-POST': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'card'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'isDigital'
            },
            {
                'name': 'orderDesc'
            },
            {
                'name': 'payerDetails'
            },
            {
                'name': 'myRef'
            },
            {
                'name': 'paymentGatewayAccountName'
            },
            {
                'name': 'certificateName'
            },
            {
                'name': 'paymentGatewayAccount'
            },
            {
                'name': 'networkTokenBrand'
            },
        ]
    },
    '/PaymentGateway/refund-PUT': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'refTransId'
            },
            {
                'name': 'card'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'payerDetails'
            },
            {
                'name': 'myRef'
            },
            {
                'name': 'paymentGatewayAccountName'
            },
            {
                'name': 'certificateName'
            },
            {
                'name': 'paymentGatewayAccount'
            },
            {
                'name': 'networkTokenBrand'
            },
        ]
    },
    '/PaymentGateway/void-DELETE': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'refTransId'
            },
            {
                'name': 'card'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'myRef'
            },
            {
                'name': 'paymentGatewayAccountName'
            },
            {
                'name': 'certificateName'
            },
            {
                'name': 'paymentGatewayAccount'
            },
            {
                'name': 'networkTokenBrand'
            },
        ]
    },
    '/PaymentGatewayAccounts/{name}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'paymentGatewayName'
            },
            {
                'name': 'credentials'
            },
        ]
    },
    '/PaymentGatewayAccounts-GET': {
        'parameters': [
        ]
    },
    '/PaymentGatewayAccounts/{name}-GET': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/PaymentGatewayAccounts/{name}-DELETE': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/StringTokens/{token}-DELETE': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/StringTokens/{token}-GET': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/StringTokens/{token}/meta-GET': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/StringTokens-POST': {
        'parameters': [
            {
                'name': 'payload'
            },
        ]
    },
    '/ThreeDsMerchants/{name}-GET': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/ThreeDsMerchants-GET': {
        'parameters': [
        ]
    },
    '/ThreeDsMerchants/{name}-DELETE': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/ThreeDsMerchants/{name}-PUT': {
        'parameters': [
            {
                'name': 'merchantName'
            },
            {
                'name': 'merchantDisplayName'
            },
            {
                'name': 'merchantRequestorIdSuffix'
            },
            {
                'name': 'merchantCountry'
            },
            {
                'name': 'merchantUrl'
            },
            {
                'name': 'acquirerName'
            },
            {
                'name': 'name'
            },
            {
                'name': 'brands'
            },
        ]
    },
    '/ThreeDsSessions/challengeStatus-GET': {
        'parameters': [
        ]
    },
    '/ThreeDsSessions-POST': {
        'parameters': [
            {
                'name': 'merchantAccountName'
            },
            {
                'name': 'amt'
            },
            {
                'name': 'ttl'
            },
        ]
    },
    '/ThreeDsSessions/fingerprintCallback/{sessionId}-POST': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/ThreeDsSessions/mpiChallengeCallback/{sessionId}-GET': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/ThreeDsSessions/opValidate-GET': {
        'parameters': [
        ]
    },
    '/Tools/brand-GET': {
        'parameters': [
            {
                'name': 'iin'
            },
        ]
    },
    '/Tools/iin-GET': {
        'parameters': [
            {
                'name': 'iin'
            },
        ]
    },
    '/Tools/validate-POST': {
        'parameters': [
            {
                'name': 'clientIPAddress'
            },
            {
                'name': 'countryCode'
            },
            {
                'name': 'iin'
            },
            {
                'name': 'city'
            },
            {
                'name': 'stateProvince'
            },
        ]
    },
    '/Tools/luhn-GET': {
        'parameters': [
            {
                'name': 'number'
            },
            {
                'name': 'metaData'
            },
        ]
    },
    '/Utils/apiKey-GET': {
        'parameters': [
        ]
    },
};