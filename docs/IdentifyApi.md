# thola_client.IdentifyApi

All URIs are relative to *http://localhost:8237*

Method | HTTP request | Description
------------- | ------------- | -------------
[**identify**](IdentifyApi.md#identify) | **POST** /identify | Identifies a device.


# **identify**
> IdentifyResponse identify(body)

Identifies a device.

### Example

```python
from __future__ import print_function
import time
import thola_client
from thola_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = thola_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = thola_client.IdentifyApi(thola_client.ApiClient(configuration))
body = thola_client.IdentifyRequest() # IdentifyRequest | Request to process.

try:
    # Identifies a device.
    api_response = api_instance.identify(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentifyApi->identify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentifyRequest**](IdentifyRequest.md)| Request to process. | 

### Return type

[**IdentifyResponse**](IdentifyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json<, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

