# swagger_client.CheckApi

All URIs are relative to *http://localhost:8237*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_cpu_load**](CheckApi.md#check_cpu_load) | **POST** /check/cpu-load | Check the cpu load of a device.
[**check_disk**](CheckApi.md#check_disk) | **POST** /check/disk | Check the disk of a device.
[**check_hardware_health**](CheckApi.md#check_hardware_health) | **POST** /check/hardware-health | Check an hardware health of an device.
[**check_identify**](CheckApi.md#check_identify) | **POST** /check/identify | Checks if identify matches the expectations.
[**check_interface_metrics**](CheckApi.md#check_interface_metrics) | **POST** /check/interface-metrics | Check to read out interface metrics.
[**check_memory_usage**](CheckApi.md#check_memory_usage) | **POST** /check/memory-usage | Check the memory usage of a device.
[**check_sbc**](CheckApi.md#check_sbc) | **POST** /check/sbc | Check an sbc device.
[**check_server**](CheckApi.md#check_server) | **POST** /check/server | Check a linux server.
[**check_snmp**](CheckApi.md#check_snmp) | **POST** /check/snmp | Checks SNMP availability.
[**check_thola_server**](CheckApi.md#check_thola_server) | **POST** /check/thola-server | Check existence of thola servers.
[**check_ups**](CheckApi.md#check_ups) | **POST** /check/ups | Checks whether a UPS device has its main voltage applied.


# **check_cpu_load**
> CheckResponse check_cpu_load(body)

Check the cpu load of a device.

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
api_instance = thola_client.CheckApi(thola_client.ApiClient(configuration))
body = thola_client.CheckCPULoadRequest() # CheckCPULoadRequest | Request to process.

try:
    # Check the cpu load of a device.
    api_response = api_instance.check_cpu_load(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckApi->check_cpu_load: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckCPULoadRequest**](CheckCPULoadRequest.md)| Request to process. | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_disk**
> CheckResponse check_disk(body)

Check the disk of a device.

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
api_instance = thola_client.CheckApi(thola_client.ApiClient(configuration))
body = thola_client.CheckDiskRequest() # CheckDiskRequest | Request to process.

try:
    # Check the disk of a device.
    api_response = api_instance.check_disk(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckApi->check_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckDiskRequest**](CheckDiskRequest.md)| Request to process. | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_hardware_health**
> CheckResponse check_hardware_health(body)

Check an hardware health of an device.

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
api_instance = thola_client.CheckApi(thola_client.ApiClient(configuration))
body = thola_client.CheckHardwareHealthRequest() # CheckHardwareHealthRequest | Request to process.

try:
    # Check an hardware health of an device.
    api_response = api_instance.check_hardware_health(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckApi->check_hardware_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckHardwareHealthRequest**](CheckHardwareHealthRequest.md)| Request to process. | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_identify**
> CheckResponse check_identify(body)

Checks if identify matches the expectations.

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
api_instance = thola_client.CheckApi(thola_client.ApiClient(configuration))
body = thola_client.CheckIdentifyRequest() # CheckIdentifyRequest | Request to process.

try:
    # Checks if identify matches the expectations.
    api_response = api_instance.check_identify(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckApi->check_identify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckIdentifyRequest**](CheckIdentifyRequest.md)| Request to process. | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_interface_metrics**
> CheckResponse check_interface_metrics(body)

Check to read out interface metrics.

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
api_instance = thola_client.CheckApi(thola_client.ApiClient(configuration))
body = thola_client.CheckInterfaceMetricsRequest() # CheckInterfaceMetricsRequest | Request to process.

try:
    # Check to read out interface metrics.
    api_response = api_instance.check_interface_metrics(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckApi->check_interface_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckInterfaceMetricsRequest**](CheckInterfaceMetricsRequest.md)| Request to process. | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_memory_usage**
> CheckResponse check_memory_usage(body)

Check the memory usage of a device.

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
api_instance = thola_client.CheckApi(thola_client.ApiClient(configuration))
body = thola_client.CheckMemoryUsageRequest() # CheckMemoryUsageRequest | Request to process.

try:
    # Check the memory usage of a device.
    api_response = api_instance.check_memory_usage(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckApi->check_memory_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckMemoryUsageRequest**](CheckMemoryUsageRequest.md)| Request to process. | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_sbc**
> CheckResponse check_sbc(body)

Check an sbc device.

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
api_instance = thola_client.CheckApi(thola_client.ApiClient(configuration))
body = thola_client.CheckSBCRequest() # CheckSBCRequest | Request to process.

try:
    # Check an sbc device.
    api_response = api_instance.check_sbc(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckApi->check_sbc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckSBCRequest**](CheckSBCRequest.md)| Request to process. | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_server**
> CheckResponse check_server(body)

Check a linux server.

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
api_instance = thola_client.CheckApi(thola_client.ApiClient(configuration))
body = thola_client.CheckServerRequest() # CheckServerRequest | Request to process.

try:
    # Check a linux server.
    api_response = api_instance.check_server(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckApi->check_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckServerRequest**](CheckServerRequest.md)| Request to process. | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_snmp**
> CheckResponse check_snmp(body)

Checks SNMP availability.

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
api_instance = thola_client.CheckApi(thola_client.ApiClient(configuration))
body = thola_client.CheckSNMPRequest() # CheckSNMPRequest | Request to process.

try:
    # Checks SNMP availability.
    api_response = api_instance.check_snmp(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckApi->check_snmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckSNMPRequest**](CheckSNMPRequest.md)| Request to process. | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_thola_server**
> CheckResponse check_thola_server(body)

Check existence of thola servers.

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
api_instance = thola_client.CheckApi(thola_client.ApiClient(configuration))
body = thola_client.CheckTholaServerRequest() # CheckTholaServerRequest | Request to process.

try:
    # Check existence of thola servers.
    api_response = api_instance.check_thola_server(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckApi->check_thola_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckTholaServerRequest**](CheckTholaServerRequest.md)| Request to process. | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_ups**
> CheckResponse check_ups(body)

Checks whether a UPS device has its main voltage applied.

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
api_instance = thola_client.CheckApi(thola_client.ApiClient(configuration))
body = thola_client.CheckUPSRequest() # CheckUPSRequest | Request to process.

try:
    # Checks whether a UPS device has its main voltage applied.
    api_response = api_instance.check_ups(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckApi->check_ups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckUPSRequest**](CheckUPSRequest.md)| Request to process. | 

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

