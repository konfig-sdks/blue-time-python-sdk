<div align="center">

[![Visit Bluetime](./header.png)](https://bluetime.io&#x2F;)

# Bluetime<a id="bluetime"></a>

Code Version 1.0.7.15


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`bluetime.card_operations.get_brand_prefix`](#bluetimecard_operationsget_brand_prefix)
  * [`bluetime.card_operations.get_token_start_operation`](#bluetimecard_operationsget_token_start_operation)
  * [`bluetime.card_operations.get_top_brands_lookup`](#bluetimecard_operationsget_top_brands_lookup)
  * [`bluetime.card_operations.perform_universal_payment_gateway_charge`](#bluetimecard_operationsperform_universal_payment_gateway_charge)
  * [`bluetime.card_operations.perform_validation`](#bluetimecard_operationsperform_validation)
  * [`bluetime.card_operations.perform_validation_0`](#bluetimecard_operationsperform_validation_0)
  * [`bluetime.card_operations.tokenize_and_store`](#bluetimecard_operationstokenize_and_store)
  * [`bluetime.custom_forms.get_list`](#bluetimecustom_formsget_list)
  * [`bluetime.custom_forms.remove_form`](#bluetimecustom_formsremove_form)
  * [`bluetime.custom_forms.upload_form_folder`](#bluetimecustom_formsupload_form_folder)
  * [`bluetime.cvv_operations.get_token_cvv_operation`](#bluetimecvv_operationsget_token_cvv_operation)
  * [`bluetime.cvv_operations.perform_universal_payment_gateway_charge`](#bluetimecvv_operationsperform_universal_payment_gateway_charge)
  * [`bluetime.cvv_operations.validate_operation`](#bluetimecvv_operationsvalidate_operation)
  * [`bluetime.network_token.card_tokenize`](#bluetimenetwork_tokencard_tokenize)
  * [`bluetime.network_token.delete`](#bluetimenetwork_tokendelete)
  * [`bluetime.payment_gateway.list_gateways`](#bluetimepayment_gatewaylist_gateways)
  * [`bluetime.payment_gateway.perform_authorize_operation`](#bluetimepayment_gatewayperform_authorize_operation)
  * [`bluetime.payment_gateway.perform_capture_operation`](#bluetimepayment_gatewayperform_capture_operation)
  * [`bluetime.payment_gateway.perform_charge_operation`](#bluetimepayment_gatewayperform_charge_operation)
  * [`bluetime.payment_gateway.perform_refund_operation`](#bluetimepayment_gatewayperform_refund_operation)
  * [`bluetime.payment_gateway.void_operation`](#bluetimepayment_gatewayvoid_operation)
  * [`bluetime.payment_gateway_accounts.add_or_replace`](#bluetimepayment_gateway_accountsadd_or_replace)
  * [`bluetime.payment_gateway_accounts.get_all`](#bluetimepayment_gateway_accountsget_all)
  * [`bluetime.payment_gateway_accounts.get_info`](#bluetimepayment_gateway_accountsget_info)
  * [`bluetime.payment_gateway_accounts.remove_account`](#bluetimepayment_gateway_accountsremove_account)
  * [`bluetime.string_tokens.delete_by_token`](#bluetimestring_tokensdelete_by_token)
  * [`bluetime.string_tokens.get_content`](#bluetimestring_tokensget_content)
  * [`bluetime.string_tokens.get_meta_data`](#bluetimestring_tokensget_meta_data)
  * [`bluetime.string_tokens.store_and_tokenize`](#bluetimestring_tokensstore_and_tokenize)
  * [`bluetime.three_ds_merchants.get_merchant_info`](#bluetimethree_ds_merchantsget_merchant_info)
  * [`bluetime.three_ds_merchants.list_merchants`](#bluetimethree_ds_merchantslist_merchants)
  * [`bluetime.three_ds_merchants.remove_merchant`](#bluetimethree_ds_merchantsremove_merchant)
  * [`bluetime.three_ds_merchants.update_merchant_info`](#bluetimethree_ds_merchantsupdate_merchant_info)
  * [`bluetime.three_ds_sessions.get_challenge_status`](#bluetimethree_ds_sessionsget_challenge_status)
  * [`bluetime.three_ds_sessions.get_token_start_operation`](#bluetimethree_ds_sessionsget_token_start_operation)
  * [`bluetime.three_ds_sessions.handle_fingerprint_callback`](#bluetimethree_ds_sessionshandle_fingerprint_callback)
  * [`bluetime.three_ds_sessions.handle_mpi_challenge_callback`](#bluetimethree_ds_sessionshandle_mpi_challenge_callback)
  * [`bluetime.three_ds_sessions.perform_validation_operation`](#bluetimethree_ds_sessionsperform_validation_operation)
  * [`bluetime.tools.get_brand_lookup`](#bluetimetoolsget_brand_lookup)
  * [`bluetime.tools.lookup_metadata`](#bluetimetoolslookup_metadata)
  * [`bluetime.tools.validate_card_details`](#bluetimetoolsvalidate_card_details)
  * [`bluetime.tools.validate_luhn_card`](#bluetimetoolsvalidate_luhn_card)
  * [`bluetime.utils.validate_api_key`](#bluetimeutilsvalidate_api_key)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=BlueTime&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from blue_time_python_sdk import BlueTime, ApiException

bluetime = BlueTime(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Return brand of card prefix.
    get_brand_prefix_response = bluetime.card_operations.get_brand_prefix(
        iin="48072888",
    )
    print(get_brand_prefix_response)
except ApiException as e:
    print("Exception when calling CardOperationsApi.get_brand_prefix: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from blue_time_python_sdk import BlueTime, ApiException

bluetime = BlueTime(

    access_token = 'YOUR_BEARER_TOKEN'
)

async def main():
    try:
        # Return brand of card prefix.
        get_brand_prefix_response = await bluetime.card_operations.aget_brand_prefix(
            iin="48072888",
        )
        print(get_brand_prefix_response)
    except ApiException as e:
        print("Exception when calling CardOperationsApi.get_brand_prefix: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from blue_time_python_sdk import BlueTime, ApiException

bluetime = BlueTime(

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Return brand of card prefix.
    get_brand_prefix_response = bluetime.card_operations.raw.get_brand_prefix(
        iin="48072888",
    )
    pprint(get_brand_prefix_response.body)
    pprint(get_brand_prefix_response.body["brand"])
    pprint(get_brand_prefix_response.body["brand_logo_url"])
    pprint(get_brand_prefix_response.headers)
    pprint(get_brand_prefix_response.status)
    pprint(get_brand_prefix_response.round_trip_time)
except ApiException as e:
    print("Exception when calling CardOperationsApi.get_brand_prefix: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `bluetime.card_operations.get_brand_prefix`<a id="bluetimecard_operationsget_brand_prefix"></a>

Return brand of card prefix.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_brand_prefix_response = bluetime.card_operations.get_brand_prefix(
    iin="48072888",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### iin: `str`<a id="iin-str"></a>

Card prefix

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsBrandLookupResult`](./blue_time_python_sdk/pydantic/pay_tools_api_models_brand_lookup_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CardOperations/brand` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.card_operations.get_token_start_operation`<a id="bluetimecard_operationsget_token_start_operation"></a>

Get a token to start a card operation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_token_start_operation_response = bluetime.card_operations.get_token_start_operation(
    ttl=60,
    three_ds_session_model={
        "merchant_account_name": "merchant_account_name_example",
        "amt": {
            "cur": "AFN",
            "amt": 3.14,
        },
    },
    vld="VeryHigh",
    _3ds="Mandatory",
    crg=True,
    tkn="Always",
    crg_d={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ttl: `int`<a id="ttl-int"></a>

Time to live for the returned token

##### three_ds_session_model: [`PayToolsBlAuthenticationThreeDsSessionModel`](./blue_time_python_sdk/type/pay_tools_bl_authentication_three_ds_session_model.py)<a id="three_ds_session_model-paytoolsblauthenticationthreedssessionmodelblue_time_python_sdktypepay_tools_bl_authentication_three_ds_session_modelpy"></a>


##### vld: [`PciBookingIINLookupLibraryRiskLevel`](./blue_time_python_sdk/type/pci_booking_iin_lookup_library_risk_level.py)<a id="vld-pcibookingiinlookuplibraryrisklevelblue_time_python_sdktypepci_booking_iin_lookup_library_risk_levelpy"></a>

##### _3ds: [`PayToolsSharedEnumsPerform3ds`](./blue_time_python_sdk/type/pay_tools_shared_enums_perform3ds.py)<a id="_3ds-paytoolssharedenumsperform3dsblue_time_python_sdktypepay_tools_shared_enums_perform3dspy"></a>

##### crg: `bool`<a id="crg-bool"></a>

Is Card charge required for this session

##### tkn: [`PayToolsBlAuthenticationTokenizationAction`](./blue_time_python_sdk/type/pay_tools_bl_authentication_tokenization_action.py)<a id="tkn-paytoolsblauthenticationtokenizationactionblue_time_python_sdktypepay_tools_bl_authentication_tokenization_actionpy"></a>

##### crg_d: [`PayToolsBlAuthenticationChargePresetData`](./blue_time_python_sdk/type/pay_tools_bl_authentication_charge_preset_data.py)<a id="crg_d-paytoolsblauthenticationchargepresetdatablue_time_python_sdktypepay_tools_bl_authentication_charge_preset_datapy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsBlAuthenticationPreSignedDataModel`](./blue_time_python_sdk/type/pay_tools_bl_authentication_pre_signed_data_model.py)
The data to be validated in further requests

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsJwsMultipleOutputModel`](./blue_time_python_sdk/pydantic/pay_tools_api_models_jws_multiple_output_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CardOperations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.card_operations.get_top_brands_lookup`<a id="bluetimecard_operationsget_top_brands_lookup"></a>

The result is an array of 5 elements, where each element represents iin prefixes for a givel size as well as the list of logo Url's for all brands.
Each element in the top-level array is an object where members are prefixes and data is the brand.
For a quick lookup:
1. get the element by the size of your prefix.
2. try to obtain the prefix as a member name; The member value is the brand

For logo lookup finf thr brand name as the key to the logos member.
If not found, you can try using 'DEFAULT'.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_top_brands_lookup_response = bluetime.card_operations.get_top_brands_lookup()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsTopBrands`](./blue_time_python_sdk/pydantic/pay_tools_api_models_top_brands.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CardOperations/topBrands` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.card_operations.perform_universal_payment_gateway_charge`<a id="bluetimecard_operationsperform_universal_payment_gateway_charge"></a>

Perform Univesal payment gateway charge operation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_universal_payment_gateway_charge_response = bluetime.card_operations.perform_universal_payment_gateway_charge(
    card={
        "card_type": "Visa",
        "card_holder_name": "card_holder_name_example",
        "card_number": "@Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4",
        "expiration_year": 1,
        "expiration_month": 1,
    },
    payer_details={
        "country_code": "AE",
    },
    my_ref="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card: [`PayToolsApiModelsCardInputModel`](./blue_time_python_sdk/type/pay_tools_api_models_card_input_model.py)<a id="card-paytoolsapimodelscardinputmodelblue_time_python_sdktypepay_tools_api_models_card_input_modelpy"></a>


##### payer_details: [`PayToolsApiModelsPayerDetailsNoIpAddress`](./blue_time_python_sdk/type/pay_tools_api_models_payer_details_no_ip_address.py)<a id="payer_details-paytoolsapimodelspayerdetailsnoipaddressblue_time_python_sdktypepay_tools_api_models_payer_details_no_ip_addresspy"></a>


##### my_ref: `Optional[str]`<a id="my_ref-optionalstr"></a>

Your custom reference for this transaction

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsCardOpsChargeRequest`](./blue_time_python_sdk/type/pay_tools_api_models_card_ops_charge_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsJwsOutputModel1PaymentsOperationResultPaymentsVersion0000CultureneutralPublicKeyTokennull`](./blue_time_python_sdk/pydantic/pay_tools_api_models_jws_output_model1_payments_operation_result_payments_version0000_cultureneutral_public_key_tokennull.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CardOperations/charge` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.card_operations.perform_validation`<a id="bluetimecard_operationsperform_validation"></a>

Perform card validation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_validation_response = bluetime.card_operations.perform_validation(
    country_code="AE",
    iin="48072888",
    city="string_example",
    state_province="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country_code: `str`<a id="country_code-str"></a>

2 letter country code (<a href=\\\"https://en.wikipedia.org/wiki/ISO_3166-2#Current_codes\\\" target=\\\"_blank\\\">ISO 3166-2 <img src=\\\"https://files.readme.io/b676144-openNewWindow.png\\\" width=\\\"10\\\" /></a>)

##### iin: `str`<a id="iin-str"></a>

Card prefix

##### city: `Optional[str]`<a id="city-optionalstr"></a>

City

##### state_province: `Optional[str]`<a id="state_province-optionalstr"></a>

State or Province

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsPayerBase`](./blue_time_python_sdk/type/pay_tools_api_models_payer_base.py)
Payer details

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsJwsOutputModel1pciBookingIINLookupLibraryCardValidationResultpciBookingIINLookupLibraryVersion1040CultureneutralPublicKeyTokennull`](./blue_time_python_sdk/pydantic/pay_tools_api_models_jws_output_model1pci_booking_iin_lookup_library_card_validation_resultpci_booking_iin_lookup_library_version1040_cultureneutral_public_key_tokennull.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CardOperations/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.card_operations.perform_validation_0`<a id="bluetimecard_operationsperform_validation_0"></a>

Perform validation of the operation using to signed data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_validation_0_response = bluetime.card_operations.perform_validation_0()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsBlAuthenticationSignedData`](./blue_time_python_sdk/pydantic/pay_tools_bl_authentication_signed_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CardOperations/opValidate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.card_operations.tokenize_and_store`<a id="bluetimecard_operationstokenize_and_store"></a>

Tokenize and store card number

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
tokenize_and_store_response = bluetime.card_operations.tokenize_and_store(
    payload="a",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payload: `str`<a id="payload-str"></a>

The content of the string you would like to tokenize

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsStringTokenIntputModel`](./blue_time_python_sdk/type/pay_tools_api_models_string_token_intput_model.py)
Model with card number to be tokenized

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsJwsOutputModel1PayToolsApiModelsStringTokenMetaDataOutputModelPayToolsApiVersion10715CultureneutralPublicKeyTokennull`](./blue_time_python_sdk/pydantic/pay_tools_api_models_jws_output_model1_pay_tools_api_models_string_token_meta_data_output_model_pay_tools_api_version10715_cultureneutral_public_key_tokennull.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CardOperations/store` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.custom_forms.get_list`<a id="bluetimecustom_formsget_list"></a>

This method allows you to retrieve the list of custom forms stored in PCI Booking

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = bluetime.custom_forms.get_list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsCustomFormMetaModel`](./blue_time_python_sdk/pydantic/pay_tools_api_models_custom_form_meta_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CustomForms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.custom_forms.remove_form`<a id="bluetimecustom_formsremove_form"></a>

This method allows you to delete a custom form that was previously stored in PCI Booking.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluetime.custom_forms.remove_form(
    name="name_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The unique identifier provided to this custom form when originally uploaded

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CustomForms/{name}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.custom_forms.upload_form_folder`<a id="bluetimecustom_formsupload_form_folder"></a>

This method allows you to upload a custom form into PCI Booking. You can design your custom form copletely on your own and upload any and all related content (JavaScript, stylesheet, images, etc) to PCI Booking. All content should be stored in one ZIP file that you will provide in this request.
The uploaded data should be a zip file, properly encoded as a part named 'zipFile' in the body.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_form_folder_response = bluetime.custom_forms.upload_form_folder(
    name="name_example",
    content_type="string_example",
    content_disposition="string_example",
    headers={
        "key": [
            "string_example"
        ],
    },
    length=1,
    name="string_example",
    file_name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The unique name to identify this form in PCI Booking. You will use this value whenever referencing this custom form.

##### content_type: `str`<a id="content_type-str"></a>

##### content_disposition: `str`<a id="content_disposition-str"></a>

##### headers: [`CustomFormsUploadFormFolderRequest1Headers`](./blue_time_python_sdk/type/custom_forms_upload_form_folder_request1_headers.py)<a id="headers-customformsuploadformfolderrequest1headersblue_time_python_sdktypecustom_forms_upload_form_folder_request1_headerspy"></a>

##### length: `int`<a id="length-int"></a>

##### name: `str`<a id="name-str"></a>

##### file_name: `str`<a id="file_name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomFormsUploadFormFolderRequest1`](./blue_time_python_sdk/type/custom_forms_upload_form_folder_request1.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsCustomFormUploadModel`](./blue_time_python_sdk/pydantic/pay_tools_api_models_custom_form_upload_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CustomForms/{name}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.cvv_operations.get_token_cvv_operation`<a id="bluetimecvv_operationsget_token_cvv_operation"></a>

Get a token to start a CVV operation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_token_cvv_operation_response = bluetime.cvv_operations.get_token_cvv_operation(
    ttl=60,
    card={
        "card_token": "@gCu2LC4aWwWL9Y864DZtaGRyyGFZKkkp",
        "expiration_year": 2023,
        "expiration_month": 1,
        "card_type": "Visa",
        "card_holder_name": "card_holder_name_example",
    },
    crg_d={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ttl: `int`<a id="ttl-int"></a>

Time to live for the returned token

##### card: [`PayToolsSharedModelsCardStoredCard`](./blue_time_python_sdk/type/pay_tools_shared_models_card_stored_card.py)<a id="card-paytoolssharedmodelscardstoredcardblue_time_python_sdktypepay_tools_shared_models_card_stored_cardpy"></a>


##### crg_d: [`PayToolsBlAuthenticationChargePresetData`](./blue_time_python_sdk/type/pay_tools_bl_authentication_charge_preset_data.py)<a id="crg_d-paytoolsblauthenticationchargepresetdatablue_time_python_sdktypepay_tools_bl_authentication_charge_preset_datapy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsBlAuthenticationCvvSignedDataModel`](./blue_time_python_sdk/type/pay_tools_bl_authentication_cvv_signed_data_model.py)
The data to be validated in further requests

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsJwsOutputModel`](./blue_time_python_sdk/pydantic/pay_tools_api_models_jws_output_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CvvOperations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.cvv_operations.perform_universal_payment_gateway_charge`<a id="bluetimecvv_operationsperform_universal_payment_gateway_charge"></a>

Perform Univesal payment gateway charge operation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_universal_payment_gateway_charge_response = bluetime.cvv_operations.perform_universal_payment_gateway_charge(
    cvv="4807",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cvv: `str`<a id="cvv-str"></a>

The card details that should be charged. You can either provide us with the raw card details or provide a reference to the stored card details in a token.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsCvvOpsChargeRequest`](./blue_time_python_sdk/type/pay_tools_api_models_cvv_ops_charge_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsJwsOutputModel1PayToolsBlAuthenticationChargeCardSignedModelPayToolsBlVersion1000CultureneutralPublicKeyTokennull`](./blue_time_python_sdk/pydantic/pay_tools_api_models_jws_output_model1_pay_tools_bl_authentication_charge_card_signed_model_pay_tools_bl_version1000_cultureneutral_public_key_tokennull.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CvvOperations/charge` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.cvv_operations.validate_operation`<a id="bluetimecvv_operationsvalidate_operation"></a>

Perform validation of the operation using signed data from charge operation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_operation_response = bluetime.cvv_operations.validate_operation()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsBlAuthenticationCvvSignedDataModel`](./blue_time_python_sdk/pydantic/pay_tools_bl_authentication_cvv_signed_data_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/CvvOperations/opValidate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.network_token.card_tokenize`<a id="bluetimenetwork_tokencard_tokenize"></a>

Network-tokenize a card

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
card_tokenize_response = bluetime.network_token.card_tokenize(
    tokenization_request={
        "card_source": "OnFile",
    },
    card={
        "card_number": "@Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4",
        "expiration_year": 1,
        "expiration_month": 1,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tokenization_request: [`PayToolsApiModelsTokenizationRequest`](./blue_time_python_sdk/type/pay_tools_api_models_tokenization_request.py)<a id="tokenization_request-paytoolsapimodelstokenizationrequestblue_time_python_sdktypepay_tools_api_models_tokenization_requestpy"></a>


##### card: [`PayToolsApiModelsCardBaseWithSecurityCode`](./blue_time_python_sdk/type/pay_tools_api_models_card_base_with_security_code.py)<a id="card-paytoolsapimodelscardbasewithsecuritycodeblue_time_python_sdktypepay_tools_api_models_card_base_with_security_codepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsNetworkTokenizationTokenizeRequest`](./blue_time_python_sdk/type/pay_tools_api_models_network_tokenization_tokenize_request.py)
Tokenization Request

#### 🔄 Return<a id="🔄-return"></a>

[`NetworkTokenTokenizationResult`](./blue_time_python_sdk/pydantic/network_token_tokenization_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/NetworkToken` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.network_token.delete`<a id="bluetimenetwork_tokendelete"></a>

Delete a Network-token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = bluetime.network_token.delete(
    source="Merchant",
    token_id="a",
    brand="Visa",
    reason="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### source: [`NetworkTokenRequestSource`](./blue_time_python_sdk/type/network_token_request_source.py)<a id="source-networktokenrequestsourceblue_time_python_sdktypenetwork_token_request_sourcepy"></a>

##### token_id: `str`<a id="token_id-str"></a>

Token Id within the Brand

##### brand: [`PaymentsNetworkTokenSchemes`](./blue_time_python_sdk/type/payments_network_token_schemes.py)<a id="brand-paymentsnetworktokenschemesblue_time_python_sdktypepayments_network_token_schemespy"></a>

##### reason: `Optional[str]`<a id="reason-optionalstr"></a>

Reason for deletion

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsNetworkTokenizationDeleteTokenRequest`](./blue_time_python_sdk/type/pay_tools_api_models_network_tokenization_delete_token_request.py)
Delete Request

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/NetworkToken` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.payment_gateway.list_gateways`<a id="bluetimepayment_gatewaylist_gateways"></a>

To provide you with full payment orchestration capabilities, we have integrated with many different payment gateways and processors around the world. This method allows you to retrieve the list of all integrated payment gateways in our system and provide you with the relevant connection settings required for each of them.
To see a graphical list of the supported payment gateways, please visit our website.
If you would like us to support a new payment gateway not on the list, please contact our support.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_gateways_response = bluetime.payment_gateway.list_gateways()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentGatewayListGatewaysResponse`](./blue_time_python_sdk/pydantic/payment_gateway_list_gateways_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/PaymentGateway` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.payment_gateway.perform_authorize_operation`<a id="bluetimepayment_gatewayperform_authorize_operation"></a>

This method allows you to perform an "authorize" operation (also called "preauthorization" or "authorization") through your payment gateway. When you perform the "authorize" operation, the bank that issued the credit card will place an authorization of the total amount of the funds. This is how the bank determines if the funds are available to make the purchase. The card will not actually be “charged” until you perform the "capture" operation (using our `[PUT] /PaymentGateway/capture` method).
**Please note**, different card brands and different banks allow for different time frames on the lifespan of a payment authorization. You will need to check with your payment processor on how long you would have between performing an "authorize" operation and a "charge" operation".
If needed, you can void this "authorize" operation by using the `[DELETE] /PaymentGateway/void` method

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_authorize_operation_response = bluetime.payment_gateway.perform_authorize_operation(
    currency="a",
    card={
        "card_type": "Visa",
        "card_holder_name": "card_holder_name_example",
        "card_number": "@Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4",
        "expiration_year": 1,
        "expiration_month": 1,
    },
    amount=3.14,
    is_digital=True,
    order_desc="string_example",
    payer_details={
        "client_ip_address": "client_ip_address_example",
        "country_code": "AE",
    },
    my_ref="string_example",
    payment_gateway_account_name="string_example",
    certificate_name="string_example",
    payment_gateway_account={
    },
    network_token_brand="Visa",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

The currency of the transaction. Based on the <a href=\\\"https://en.wikipedia.org/wiki/ISO_4217#Active_codes\\\" target=\\\"_blank\\\">ISO 4217</a> standard.

##### card: [`PayToolsApiModelsCardInputModel`](./blue_time_python_sdk/type/pay_tools_api_models_card_input_model.py)<a id="card-paytoolsapimodelscardinputmodelblue_time_python_sdktypepay_tools_api_models_card_input_modelpy"></a>


##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The amount to be charged (the amount should be in major units - for example, 10.23)

##### is_digital: `bool`<a id="is_digital-bool"></a>

This field is an additional optional parameter used by some of our payment processors. Please read our additional guidance section for payment processors that use this and other parameters

##### order_desc: `Optional[str]`<a id="order_desc-optionalstr"></a>

This field is an additional optional parameter used by some of our payment processors. Please read our additional guidance section for payment processors that use this and other parameters

##### payer_details: [`PayToolsApiModelsPayerDetails`](./blue_time_python_sdk/type/pay_tools_api_models_payer_details.py)<a id="payer_details-paytoolsapimodelspayerdetailsblue_time_python_sdktypepay_tools_api_models_payer_detailspy"></a>


##### my_ref: `Optional[str]`<a id="my_ref-optionalstr"></a>

Your custom reference for this transaction

##### payment_gateway_account_name: `Optional[str]`<a id="payment_gateway_account_name-optionalstr"></a>

The reference name provided to the stored Payment Gateway Account as set in `PUT /PaymentGatewayAccounts/{name}`.  **Please note**, if you provide us with both this parameter and the raw credentials in the `paymentGatewayAccount` object, this parameter will be ignored and the raw credentials will take precedence.

##### certificate_name: `Optional[str]`<a id="certificate_name-optionalstr"></a>

Optional parameter if the payment gateway requires authentication using a client certificate. The name of the certificate that was stored in our system via our <a href=\\\"https://portal.epaytools.com\\\" target=\\\"_blank\\\">users portal</a>

##### payment_gateway_account: [`PayToolsApiModelsPaymentGatewayAccount`](./blue_time_python_sdk/type/pay_tools_api_models_payment_gateway_account.py)<a id="payment_gateway_account-paytoolsapimodelspaymentgatewayaccountblue_time_python_sdktypepay_tools_api_models_payment_gateway_accountpy"></a>


##### network_token_brand: [`PaymentsNetworkTokenSchemes`](./blue_time_python_sdk/type/payments_network_token_schemes.py)<a id="network_token_brand-paymentsnetworktokenschemesblue_time_python_sdktypepayments_network_token_schemespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsAuthRequestModel`](./blue_time_python_sdk/type/pay_tools_api_models_auth_request_model.py)
Card charge model

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsOperationResult`](./blue_time_python_sdk/pydantic/payments_operation_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/PaymentGateway/authorize` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.payment_gateway.perform_capture_operation`<a id="bluetimepayment_gatewayperform_capture_operation"></a>

This method allows you to perform a "capture" operation on a previously created "authorize" operation (see our `[POST] /PaymentGateway/authorize` method for additional information).
When you perform the "authorize" operation, the bank that issued the credit card will place an authorization of the total amount of the funds. This is how the bank determines if the funds are available to make the purchase. The card will not actually be “charged” until you perform the "capture" operation.
**Please note**, different card brands and different banks allow for different time frames on the lifespan of a payment authorization. You will need to check with your payment processor on how long you would have between performing an "authorize" operation and a "charge" operation".

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_capture_operation_response = bluetime.payment_gateway.perform_capture_operation(
    currency="a",
    ref_trans_id="a",
    card={
        "card_type": "Visa",
        "card_holder_name": "card_holder_name_example",
        "card_number": "@Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4",
        "expiration_year": 1,
        "expiration_month": 1,
    },
    amount=3.14,
    my_ref="string_example",
    payment_gateway_account_name="string_example",
    certificate_name="string_example",
    payment_gateway_account={
    },
    network_token_brand="Visa",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

The currency of the transaction. Based on the <a href=\\\"https://en.wikipedia.org/wiki/ISO_4217#Active_codes\\\" target=\\\"_blank\\\">ISO 4217</a> standard.

##### ref_trans_id: `str`<a id="ref_trans_id-str"></a>

The transaction ID that this operation is referring to.

##### card: [`PayToolsApiModelsCardInputModel`](./blue_time_python_sdk/type/pay_tools_api_models_card_input_model.py)<a id="card-paytoolsapimodelscardinputmodelblue_time_python_sdktypepay_tools_api_models_card_input_modelpy"></a>


##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The amount to be charged (the amount should be in major units - for example, 10.23)

##### my_ref: `Optional[str]`<a id="my_ref-optionalstr"></a>

Your custom reference for this transaction

##### payment_gateway_account_name: `Optional[str]`<a id="payment_gateway_account_name-optionalstr"></a>

The reference name provided to the stored Payment Gateway Account as set in `PUT /PaymentGatewayAccounts/{name}`.  **Please note**, if you provide us with both this parameter and the raw credentials in the `paymentGatewayAccount` object, this parameter will be ignored and the raw credentials will take precedence.

##### certificate_name: `Optional[str]`<a id="certificate_name-optionalstr"></a>

Optional parameter if the payment gateway requires authentication using a client certificate. The name of the certificate that was stored in our system via our <a href=\\\"https://portal.epaytools.com\\\" target=\\\"_blank\\\">users portal</a>

##### payment_gateway_account: [`PayToolsApiModelsPaymentGatewayAccount`](./blue_time_python_sdk/type/pay_tools_api_models_payment_gateway_account.py)<a id="payment_gateway_account-paytoolsapimodelspaymentgatewayaccountblue_time_python_sdktypepay_tools_api_models_payment_gateway_accountpy"></a>


##### network_token_brand: [`PaymentsNetworkTokenSchemes`](./blue_time_python_sdk/type/payments_network_token_schemes.py)<a id="network_token_brand-paymentsnetworktokenschemesblue_time_python_sdktypepayments_network_token_schemespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsCaptureVoidRequestModel`](./blue_time_python_sdk/type/pay_tools_api_models_capture_void_request_model.py)
Capture or Void Request Model

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsOperationResult`](./blue_time_python_sdk/pydantic/payments_operation_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/PaymentGateway/capture` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.payment_gateway.perform_charge_operation`<a id="bluetimepayment_gatewayperform_charge_operation"></a>

This method allows you to perform a "charge" operation through your payment gateway. A "charge" operation will request immediate payment from the card and the card owner will see this listed as a transaction in their card statement.
If needed, you can void this "charge" operation by using the `[DELETE] /PaymentGateway/void` method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_charge_operation_response = bluetime.payment_gateway.perform_charge_operation(
    currency="a",
    card={
        "card_type": "Visa",
        "card_holder_name": "card_holder_name_example",
        "card_number": "@Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4",
        "expiration_year": 1,
        "expiration_month": 1,
    },
    amount=3.14,
    is_digital=True,
    order_desc="string_example",
    payer_details={
        "client_ip_address": "client_ip_address_example",
        "country_code": "AE",
    },
    my_ref="string_example",
    payment_gateway_account_name="string_example",
    certificate_name="string_example",
    payment_gateway_account={
    },
    network_token_brand="Visa",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

The currency of the transaction. Based on the <a href=\\\"https://en.wikipedia.org/wiki/ISO_4217#Active_codes\\\" target=\\\"_blank\\\">ISO 4217</a> standard.

##### card: [`PayToolsApiModelsCardInputModel`](./blue_time_python_sdk/type/pay_tools_api_models_card_input_model.py)<a id="card-paytoolsapimodelscardinputmodelblue_time_python_sdktypepay_tools_api_models_card_input_modelpy"></a>


##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The amount to be charged (the amount should be in major units - for example, 10.23)

##### is_digital: `bool`<a id="is_digital-bool"></a>

This field is an additional optional parameter used by some of our payment processors. Please read our additional guidance section for payment processors that use this and other parameters

##### order_desc: `Optional[str]`<a id="order_desc-optionalstr"></a>

This field is an additional optional parameter used by some of our payment processors. Please read our additional guidance section for payment processors that use this and other parameters

##### payer_details: [`PayToolsApiModelsPayerDetails`](./blue_time_python_sdk/type/pay_tools_api_models_payer_details.py)<a id="payer_details-paytoolsapimodelspayerdetailsblue_time_python_sdktypepay_tools_api_models_payer_detailspy"></a>


##### my_ref: `Optional[str]`<a id="my_ref-optionalstr"></a>

Your custom reference for this transaction

##### payment_gateway_account_name: `Optional[str]`<a id="payment_gateway_account_name-optionalstr"></a>

The reference name provided to the stored Payment Gateway Account as set in `PUT /PaymentGatewayAccounts/{name}`.  **Please note**, if you provide us with both this parameter and the raw credentials in the `paymentGatewayAccount` object, this parameter will be ignored and the raw credentials will take precedence.

##### certificate_name: `Optional[str]`<a id="certificate_name-optionalstr"></a>

Optional parameter if the payment gateway requires authentication using a client certificate. The name of the certificate that was stored in our system via our <a href=\\\"https://portal.epaytools.com\\\" target=\\\"_blank\\\">users portal</a>

##### payment_gateway_account: [`PayToolsApiModelsPaymentGatewayAccount`](./blue_time_python_sdk/type/pay_tools_api_models_payment_gateway_account.py)<a id="payment_gateway_account-paytoolsapimodelspaymentgatewayaccountblue_time_python_sdktypepay_tools_api_models_payment_gateway_accountpy"></a>


##### network_token_brand: [`PaymentsNetworkTokenSchemes`](./blue_time_python_sdk/type/payments_network_token_schemes.py)<a id="network_token_brand-paymentsnetworktokenschemesblue_time_python_sdktypepayments_network_token_schemespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsAuthRequestModel`](./blue_time_python_sdk/type/pay_tools_api_models_auth_request_model.py)
Card charge model

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsOperationResult`](./blue_time_python_sdk/pydantic/payments_operation_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/PaymentGateway/charge` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.payment_gateway.perform_refund_operation`<a id="bluetimepayment_gatewayperform_refund_operation"></a>

This method allows you to submit a "refund" operation against a previously created "charge" (using `[POST] /PaymentGateway/charge`) or "capture" (using `[POST] /PaymentGateway/capture`) operations.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
perform_refund_operation_response = bluetime.payment_gateway.perform_refund_operation(
    currency="a",
    ref_trans_id="a",
    card={
        "card_type": "Visa",
        "card_holder_name": "card_holder_name_example",
        "card_number": "@Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4",
        "expiration_year": 1,
        "expiration_month": 1,
    },
    amount=3.14,
    payer_details={
        "client_ip_address": "client_ip_address_example",
        "country_code": "AE",
    },
    my_ref="string_example",
    payment_gateway_account_name="string_example",
    certificate_name="string_example",
    payment_gateway_account={
    },
    network_token_brand="Visa",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

The currency of the transaction. Based on the <a href=\\\"https://en.wikipedia.org/wiki/ISO_4217#Active_codes\\\" target=\\\"_blank\\\">ISO 4217</a> standard.

##### ref_trans_id: `str`<a id="ref_trans_id-str"></a>

The transaction ID that this operation is referring to.

##### card: [`PayToolsApiModelsCardInputModel`](./blue_time_python_sdk/type/pay_tools_api_models_card_input_model.py)<a id="card-paytoolsapimodelscardinputmodelblue_time_python_sdktypepay_tools_api_models_card_input_modelpy"></a>


##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The amount to be charged (the amount should be in major units - for example, 10.23)

##### payer_details: [`PayToolsApiModelsPayerDetails`](./blue_time_python_sdk/type/pay_tools_api_models_payer_details.py)<a id="payer_details-paytoolsapimodelspayerdetailsblue_time_python_sdktypepay_tools_api_models_payer_detailspy"></a>


##### my_ref: `Optional[str]`<a id="my_ref-optionalstr"></a>

Your custom reference for this transaction

##### payment_gateway_account_name: `Optional[str]`<a id="payment_gateway_account_name-optionalstr"></a>

The reference name provided to the stored Payment Gateway Account as set in `PUT /PaymentGatewayAccounts/{name}`.  **Please note**, if you provide us with both this parameter and the raw credentials in the `paymentGatewayAccount` object, this parameter will be ignored and the raw credentials will take precedence.

##### certificate_name: `Optional[str]`<a id="certificate_name-optionalstr"></a>

Optional parameter if the payment gateway requires authentication using a client certificate. The name of the certificate that was stored in our system via our <a href=\\\"https://portal.epaytools.com\\\" target=\\\"_blank\\\">users portal</a>

##### payment_gateway_account: [`PayToolsApiModelsPaymentGatewayAccount`](./blue_time_python_sdk/type/pay_tools_api_models_payment_gateway_account.py)<a id="payment_gateway_account-paytoolsapimodelspaymentgatewayaccountblue_time_python_sdktypepay_tools_api_models_payment_gateway_accountpy"></a>


##### network_token_brand: [`PaymentsNetworkTokenSchemes`](./blue_time_python_sdk/type/payments_network_token_schemes.py)<a id="network_token_brand-paymentsnetworktokenschemesblue_time_python_sdktypepayments_network_token_schemespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsRefundRequestModel`](./blue_time_python_sdk/type/pay_tools_api_models_refund_request_model.py)
Capture or Void Request Model

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsOperationResult`](./blue_time_python_sdk/pydantic/payments_operation_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/PaymentGateway/refund` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.payment_gateway.void_operation`<a id="bluetimepayment_gatewayvoid_operation"></a>

This method allows you to submit a "void" operation against a previously created "charge" (using `[POST] /PaymentGateway/charge`) or "authorize" (using `[POST] /PaymentGateway/authorize`) operations.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
void_operation_response = bluetime.payment_gateway.void_operation(
    currency="a",
    ref_trans_id="a",
    card={
        "card_type": "Visa",
        "card_holder_name": "card_holder_name_example",
        "card_number": "@Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4",
        "expiration_year": 1,
        "expiration_month": 1,
    },
    amount=3.14,
    my_ref="string_example",
    payment_gateway_account_name="string_example",
    certificate_name="string_example",
    payment_gateway_account={
    },
    network_token_brand="Visa",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

The currency of the transaction. Based on the <a href=\\\"https://en.wikipedia.org/wiki/ISO_4217#Active_codes\\\" target=\\\"_blank\\\">ISO 4217</a> standard.

##### ref_trans_id: `str`<a id="ref_trans_id-str"></a>

The transaction ID that this operation is referring to.

##### card: [`PayToolsApiModelsCardInputModel`](./blue_time_python_sdk/type/pay_tools_api_models_card_input_model.py)<a id="card-paytoolsapimodelscardinputmodelblue_time_python_sdktypepay_tools_api_models_card_input_modelpy"></a>


##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The amount to be charged (the amount should be in major units - for example, 10.23)

##### my_ref: `Optional[str]`<a id="my_ref-optionalstr"></a>

Your custom reference for this transaction

##### payment_gateway_account_name: `Optional[str]`<a id="payment_gateway_account_name-optionalstr"></a>

The reference name provided to the stored Payment Gateway Account as set in `PUT /PaymentGatewayAccounts/{name}`.  **Please note**, if you provide us with both this parameter and the raw credentials in the `paymentGatewayAccount` object, this parameter will be ignored and the raw credentials will take precedence.

##### certificate_name: `Optional[str]`<a id="certificate_name-optionalstr"></a>

Optional parameter if the payment gateway requires authentication using a client certificate. The name of the certificate that was stored in our system via our <a href=\\\"https://portal.epaytools.com\\\" target=\\\"_blank\\\">users portal</a>

##### payment_gateway_account: [`PayToolsApiModelsPaymentGatewayAccount`](./blue_time_python_sdk/type/pay_tools_api_models_payment_gateway_account.py)<a id="payment_gateway_account-paytoolsapimodelspaymentgatewayaccountblue_time_python_sdktypepay_tools_api_models_payment_gateway_accountpy"></a>


##### network_token_brand: [`PaymentsNetworkTokenSchemes`](./blue_time_python_sdk/type/payments_network_token_schemes.py)<a id="network_token_brand-paymentsnetworktokenschemesblue_time_python_sdktypepayments_network_token_schemespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsCaptureVoidRequestModel`](./blue_time_python_sdk/type/pay_tools_api_models_capture_void_request_model.py)
Capture or Void Request Model

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsOperationResult`](./blue_time_python_sdk/pydantic/payments_operation_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/PaymentGateway/void` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.payment_gateway_accounts.add_or_replace`<a id="bluetimepayment_gateway_accountsadd_or_replace"></a>

A Payment Gateway Account is the set of information necessary for connecting to a specific payment gateway through our system.
This method allows you to add a new stored Payment Gateway Account in the system or to replace an existing one.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_or_replace_response = bluetime.payment_gateway_accounts.add_or_replace(
    name="Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4zca0U0gGbVVjd",
    payment_gateway_name="string_example",
    credentials=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

A unique name of this Payment Gateway Account

##### payment_gateway_name: `Optional[str]`<a id="payment_gateway_name-optionalstr"></a>

Unique name of the Payment Gateway the account information relates to.

##### credentials: List[`SystemCollectionsGenericKeyValuePair2SystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798eSystemStringSystemPrivateCoreLibVersion6000CultureneutralPublicKeyToken7cec85d7bea7798e`]<a id="credentials-listsystemcollectionsgenerickeyvaluepair2systemstringsystemprivatecorelibversion6000cultureneutralpublickeytoken7cec85d7bea7798esystemstringsystemprivatecorelibversion6000cultureneutralpublickeytoken7cec85d7bea7798e"></a>

A list of key-value pairs that represents your credentials within the Payment gateway.   Each key should represent a parameter listed in the \\\"CredentialsNames\\\" element of the response from the list all payment gateways method at `[GET] /paymentGateway`  Example:  \\\"Credentials\\\": [     {         \\\"Key\\\": \\\"PrivateKey\\\",         \\\"Value\\\": \\\"VBtt666M/G098098vgdewvk0Mc-GH\\\"     }  ]

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsPaymentGatewayAccountInputModel`](./blue_time_python_sdk/type/pay_tools_api_models_payment_gateway_account_input_model.py)
Payment gateway account data

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsPaymentGatewayAccountFullOutputModel`](./blue_time_python_sdk/pydantic/pay_tools_api_models_payment_gateway_account_full_output_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/PaymentGatewayAccounts/{name}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.payment_gateway_accounts.get_all`<a id="bluetimepayment_gateway_accountsget_all"></a>

This method allows you to list all stored Payment Gateway Accounts in the system

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = bluetime.payment_gateway_accounts.get_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentGatewayAccountsGetAllResponse`](./blue_time_python_sdk/pydantic/payment_gateway_accounts_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/PaymentGatewayAccounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.payment_gateway_accounts.get_info`<a id="bluetimepayment_gateway_accountsget_info"></a>

A Payment Gateway Account is the set of information necessary for connecting to a specific payment gateway through our system.
This method allows you to retrieve the information set on a particular payment gateway account. You can then update it using the `[PUT] PaymentGatewayAccounts/{name}` method

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_info_response = bluetime.payment_gateway_accounts.get_info(
    name="Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4zca0U0gGbVVjd",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

A unique name of this Payment Gateway Account

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsPaymentGatewayAccountFullOutputModel`](./blue_time_python_sdk/pydantic/pay_tools_api_models_payment_gateway_account_full_output_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/PaymentGatewayAccounts/{name}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.payment_gateway_accounts.remove_account`<a id="bluetimepayment_gateway_accountsremove_account"></a>

This method allows you to delete a stored Payment Gateway Account in the system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluetime.payment_gateway_accounts.remove_account(
    name="Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4zca0U0gGbVVjd",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

A unique name of this Payment Gateway Account

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/PaymentGatewayAccounts/{name}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.string_tokens.delete_by_token`<a id="bluetimestring_tokensdelete_by_token"></a>

This method allows you to delete a stringToken by its token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluetime.string_tokens.delete_by_token(
    token="gCu2LC4aWwWL9Y864DZtaGRyyGFZKkkp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### token: `str`<a id="token-str"></a>

The token ID representing the string to be deleted

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/StringTokens/{token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.string_tokens.get_content`<a id="bluetimestring_tokensget_content"></a>

This method allows you to retrieve the stored content of the StringToken.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_content_response = bluetime.string_tokens.get_content(
    token="gCu2LC4aWwWL9Y864DZtaGRyyGFZKkkp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### token: `str`<a id="token-str"></a>

The token ID of the StringToken you would like to retrieve the content for

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsStringTokenOutputModel`](./blue_time_python_sdk/pydantic/pay_tools_api_models_string_token_output_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/StringTokens/{token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.string_tokens.get_meta_data`<a id="bluetimestring_tokensget_meta_data"></a>

This method allows you to retrieve the meta data of a StringToken.
The response to this method will **not** retrieve the content of the StringToken (you can do that by using `GET /StringTokens/{token}`)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meta_data_response = bluetime.string_tokens.get_meta_data(
    token="gCu2LC4aWwWL9Y864DZtaGRyyGFZKkkp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### token: `str`<a id="token-str"></a>

Token representing the string to be retrieved

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsStringTokenMetaDataOutputModel`](./blue_time_python_sdk/pydantic/pay_tools_api_models_string_token_meta_data_output_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/StringTokens/{token}/meta` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.string_tokens.store_and_tokenize`<a id="bluetimestring_tokensstore_and_tokenize"></a>

This method allows you to submit a string to be stored and tokenized in our system.
Once tokenized, the token ID will be returned in the body of the response and the full token URI will be returned in the `Location` header.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
store_and_tokenize_response = bluetime.string_tokens.store_and_tokenize(
    payload="a",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payload: `str`<a id="payload-str"></a>

The content of the string you would like to tokenize

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsStringTokenIntputModel`](./blue_time_python_sdk/type/pay_tools_api_models_string_token_intput_model.py)
StringToken input model

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsStringTokenMetaDataOutputModel`](./blue_time_python_sdk/pydantic/pay_tools_api_models_string_token_meta_data_output_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/StringTokens` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.three_ds_merchants.get_merchant_info`<a id="bluetimethree_ds_merchantsget_merchant_info"></a>

Get a Merchant

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_merchant_info_response = bluetime.three_ds_merchants.get_merchant_info(
    name="Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4zca0U0gGbVVjd",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of merchant

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsThreeDsMerchantOutputModel`](./blue_time_python_sdk/pydantic/pay_tools_api_models_three_ds_merchant_output_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ThreeDsMerchants/{name}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.three_ds_merchants.list_merchants`<a id="bluetimethree_ds_merchantslist_merchants"></a>

List Merchants

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_merchants_response = bluetime.three_ds_merchants.list_merchants()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ThreeDsMerchantsListMerchantsResponse`](./blue_time_python_sdk/pydantic/three_ds_merchants_list_merchants_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ThreeDsMerchants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.three_ds_merchants.remove_merchant`<a id="bluetimethree_ds_merchantsremove_merchant"></a>

Delete a Merchant

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluetime.three_ds_merchants.remove_merchant(
    name="Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4zca0U0gGbVVjd",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of merchant

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ThreeDsMerchants/{name}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.three_ds_merchants.update_merchant_info`<a id="bluetimethree_ds_merchantsupdate_merchant_info"></a>

Set a merchant

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_merchant_info_response = bluetime.three_ds_merchants.update_merchant_info(
    merchant_name="a",
    merchant_display_name="a",
    merchant_requestor_id_suffix="a",
    merchant_country="a",
    merchant_url="a",
    acquirer_name="a",
    name="Cu2LC4aWwWL9Y864DZtaGRyyGFZKkkp4zca0U0gGbVVjd",
    brands=[
        {
            "brand": "Visa",
            "bin": "bin_example",
            "merchant_id": "merchant_id_example",
            "mcc": "mcc_example",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_name: `str`<a id="merchant_name-str"></a>

##### merchant_display_name: `str`<a id="merchant_display_name-str"></a>

##### merchant_requestor_id_suffix: `str`<a id="merchant_requestor_id_suffix-str"></a>

##### merchant_country: `str`<a id="merchant_country-str"></a>

##### merchant_url: `str`<a id="merchant_url-str"></a>

##### acquirer_name: `str`<a id="acquirer_name-str"></a>

##### name: `str`<a id="name-str"></a>

Name of merchant

##### brands: List[`PayToolsDalEntitiesThreeDsBrand`]<a id="brands-listpaytoolsdalentitiesthreedsbrand"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsDalEntitiesThreeDsMerchant`](./blue_time_python_sdk/type/pay_tools_dal_entities_three_ds_merchant.py)
3DS Merchant

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsDalEntitiesThreeDsMerchant`](./blue_time_python_sdk/pydantic/pay_tools_dal_entities_three_ds_merchant.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ThreeDsMerchants/{name}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.three_ds_sessions.get_challenge_status`<a id="bluetimethree_ds_sessionsget_challenge_status"></a>

Get challenge ststus, as stored on server

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_challenge_status_response = bluetime.three_ds_sessions.get_challenge_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsSharedModelsThreeDsClientMessage`](./blue_time_python_sdk/pydantic/pay_tools_shared_models_three_ds_client_message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ThreeDsSessions/challengeStatus` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.three_ds_sessions.get_token_start_operation`<a id="bluetimethree_ds_sessionsget_token_start_operation"></a>

Get a token to start a card operation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_token_start_operation_response = bluetime.three_ds_sessions.get_token_start_operation(
    merchant_account_name="a",
    amt={
        "cur": "AFN",
        "amt": 3.14,
    },
    ttl=60,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant_account_name: `str`<a id="merchant_account_name-str"></a>

The name of the stored merchant account

##### amt: [`PayToolsSharedModelsMoneyModel`](./blue_time_python_sdk/type/pay_tools_shared_models_money_model.py)<a id="amt-paytoolssharedmodelsmoneymodelblue_time_python_sdktypepay_tools_shared_models_money_modelpy"></a>


##### ttl: `int`<a id="ttl-int"></a>

Time to live for the returned token

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsBlAuthenticationThreeDsSessionModel`](./blue_time_python_sdk/type/pay_tools_bl_authentication_three_ds_session_model.py)
The data to be validated in further requests

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsJwsOutputModel`](./blue_time_python_sdk/pydantic/pay_tools_api_models_jws_output_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ThreeDsSessions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.three_ds_sessions.handle_fingerprint_callback`<a id="bluetimethree_ds_sessionshandle_fingerprint_callback"></a>

Handle a callback (redirect from device fingerprint)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluetime.three_ds_sessions.handle_fingerprint_callback(
    session_id="gCu2LC4aWwWL9Y864DZtaGRyyGFZKkkp",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

The value containing data to designate the client

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ThreeDsSessions/fingerprintCallback/{sessionId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.three_ds_sessions.handle_mpi_challenge_callback`<a id="bluetimethree_ds_sessionshandle_mpi_challenge_callback"></a>

Handle a callback (redirect from challenge)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluetime.three_ds_sessions.handle_mpi_challenge_callback(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

The value containing data to designate the client

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ThreeDsSessions/mpiChallengeCallback/{sessionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.three_ds_sessions.perform_validation_operation`<a id="bluetimethree_ds_sessionsperform_validation_operation"></a>

Perform validation of the operation using to signed data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bluetime.three_ds_sessions.perform_validation_operation()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ThreeDsSessions/opValidate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.tools.get_brand_lookup`<a id="bluetimetoolsget_brand_lookup"></a>

This method allows you to lookup the brand of the card provided. 
            By providing the card's BIN / IIN (the first 6 to 11 digits of the card number), we lookup and return the brand of the card (Visa, Mastercard, Amex, etc.).
            In addition, we will also provide the URL to the logo of the card brand - you can then reference this image in your card capture form.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_brand_lookup_response = bluetime.tools.get_brand_lookup(
    iin="48072888",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### iin: `str`<a id="iin-str"></a>

Card's BIN / IIN (the first 6 to 11 digits of the card number)

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsBrandLookupResult`](./blue_time_python_sdk/pydantic/pay_tools_api_models_brand_lookup_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Tools/brand` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.tools.lookup_metadata`<a id="bluetimetoolslookup_metadata"></a>

This method allows you to lookup the metadata of the card provided. 
By providing the card's BIN / IIN (the first 6 to 11 digits of the card number), we lookup and return the full metadata available for this card./r/nI
In addition, we will also provide the URL to the logo of the card brand - you can then reference this image in your card capture form.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_metadata_response = bluetime.tools.lookup_metadata(
    iin="48072888",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### iin: `str`<a id="iin-str"></a>

Card's BIN / IIN (the first 6 to 11 digits of the card number)

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsIinData`](./blue_time_python_sdk/pydantic/pay_tools_api_models_iin_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Tools/iin` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.tools.validate_card_details`<a id="bluetimetoolsvalidate_card_details"></a>

This method allows you to validate the card details against the card's meta data. By providing the billing address and IP address of the card owner, we validate those against the metadata of the card and provide a risk assessment for this transaction.
All you would need is the card's BIN / IIN (the first 6 to 11 digits of the card number), the billing address and IP address.
The response of this method will include the full metadata information for this BIN including the risk assessment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_card_details_response = bluetime.tools.validate_card_details(
    client_ip_address="a",
    country_code="AE",
    iin="48072888",
    city="string_example",
    state_province="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_ip_address: `str`<a id="client_ip_address-str"></a>

Client IP address

##### country_code: `str`<a id="country_code-str"></a>

2 letter country code (<a href=\\\"https://en.wikipedia.org/wiki/ISO_3166-2#Current_codes\\\" target=\\\"_blank\\\">ISO 3166-2 <img src=\\\"https://files.readme.io/b676144-openNewWindow.png\\\" width=\\\"10\\\" /></a>)

##### iin: `str`<a id="iin-str"></a>

Card's BIN / IIN (the first 6 to 11 digits of the card number)

##### city: `Optional[str]`<a id="city-optionalstr"></a>

City

##### state_province: `Optional[str]`<a id="state_province-optionalstr"></a>

State or Province

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayToolsApiModelsPayerBaseWithClientIp`](./blue_time_python_sdk/type/pay_tools_api_models_payer_base_with_client_ip.py)
payer details

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsCardValidationResults`](./blue_time_python_sdk/pydantic/pay_tools_api_models_card_validation_results.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Tools/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.tools.validate_luhn_card`<a id="bluetimetoolsvalidate_luhn_card"></a>

This method allows you to provide the card number and validate it against the<a href="https://en.wikipedia.org/wiki/Luhn_algorithm" target="_blank"> Luhn algorithm</a>.In addition, you can choose to receive the card's metadata in the response.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_luhn_card_response = bluetime.tools.validate_luhn_card(
    number="number_example",
    meta_data=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### number: `str`<a id="number-str"></a>

The full card number to be validated.

##### meta_data: `bool`<a id="meta_data-bool"></a>

An optional indicator to specify whether the card metadata should be included in the response.

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsLuhnCheckResultsWithIinData`](./blue_time_python_sdk/pydantic/pay_tools_api_models_luhn_check_results_with_iin_data.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Tools/luhn` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `bluetime.utils.validate_api_key`<a id="bluetimeutilsvalidate_api_key"></a>

This operation allows you to validate your API key and make sure that it is operational. Additionally, this method will allow you to test and check that the API is functioning properly

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_api_key_response = bluetime.utils.validate_api_key()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PayToolsApiModelsAuthenticationResult`](./blue_time_python_sdk/pydantic/pay_tools_api_models_authentication_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/Utils/apiKey` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
