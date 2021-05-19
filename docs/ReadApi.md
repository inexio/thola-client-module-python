# thola_client.ReadApi

All URIs are relative to *http://localhost:8237*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hardware_health**](ReadApi.md#hardware_health) | **POST** /read/hardware-health | Reads out hardware health data of a device.
[**read_available_components**](ReadApi.md#read_available_components) | **POST** /read/available-components | Returns the available components for the device.
[**read_count_interfaces**](ReadApi.md#read_count_interfaces) | **POST** /read/count-interfaces | Counts the interfaces of a device.
[**read_cpu_load**](ReadApi.md#read_cpu_load) | **POST** /read/cpu-load | Read out the CPU load of a device.
[**read_disk**](ReadApi.md#read_disk) | **POST** /read/disk | Reads out disk data of a device.
[**read_interfaces**](ReadApi.md#read_interfaces) | **POST** /read/interfaces | Reads out data of the interfaces of a device.
[**read_memory_usage**](ReadApi.md#read_memory_usage) | **POST** /read/memory-usage | Read out the memory usage of a device.
[**read_sbc**](ReadApi.md#read_sbc) | **POST** /read/sbc | Reads out SBC data of a device.
[**read_server**](ReadApi.md#read_server) | **POST** /read/server | Reads out server data of a device.
[**read_ups**](ReadApi.md#read_ups) | **POST** /read/ups | Reads out UPS data of a device.


# **hardware_health**
> ReadHardwareHealthResponse hardware_health(body)

Reads out hardware health data of a device.

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
api_instance = thola_client.ReadApi(thola_client.ApiClient(configuration))
body = thola_client.ReadHardwareHealthRequest() # ReadHardwareHealthRequest | Request to process.

try:
    # Reads out hardware health data of a device.
    api_response = api_instance.hardware_health(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->hardware_health: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReadHardwareHealthRequest**](ReadHardwareHealthRequest.md)| Request to process. | 

### Return type

[**ReadHardwareHealthResponse**](ReadHardwareHealthResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_available_components**
> ReadAvailableComponentsResponse read_available_components(body)

Returns the available components for the device.

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
api_instance = thola_client.ReadApi(thola_client.ApiClient(configuration))
body = thola_client.ReadAvailableComponentsRequest() # ReadAvailableComponentsRequest | Request to process.

try:
    # Returns the available components for the device.
    api_response = api_instance.read_available_components(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->read_available_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReadAvailableComponentsRequest**](ReadAvailableComponentsRequest.md)| Request to process. | 

### Return type

[**ReadAvailableComponentsResponse**](ReadAvailableComponentsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_count_interfaces**
> ReadCountInterfacesResponse read_count_interfaces(body)

Counts the interfaces of a device.

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
api_instance = thola_client.ReadApi(thola_client.ApiClient(configuration))
body = thola_client.ReadCountInterfacesRequest() # ReadCountInterfacesRequest | Request to process.

try:
    # Counts the interfaces of a device.
    api_response = api_instance.read_count_interfaces(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->read_count_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReadCountInterfacesRequest**](ReadCountInterfacesRequest.md)| Request to process. | 

### Return type

[**ReadCountInterfacesResponse**](ReadCountInterfacesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cpu_load**
> ReadCPULoadResponse read_cpu_load(body)

Read out the CPU load of a device.

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
api_instance = thola_client.ReadApi(thola_client.ApiClient(configuration))
body = thola_client.ReadCPULoadRequest() # ReadCPULoadRequest | Request to process.

try:
    # Read out the CPU load of a device.
    api_response = api_instance.read_cpu_load(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->read_cpu_load: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReadCPULoadRequest**](ReadCPULoadRequest.md)| Request to process. | 

### Return type

[**ReadCPULoadResponse**](ReadCPULoadResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_disk**
> ReadDiskResponse read_disk(body)

Reads out disk data of a device.

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
api_instance = thola_client.ReadApi(thola_client.ApiClient(configuration))
body = thola_client.ReadDiskRequest() # ReadDiskRequest | Request to process.

try:
    # Reads out disk data of a device.
    api_response = api_instance.read_disk(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->read_disk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReadDiskRequest**](ReadDiskRequest.md)| Request to process. | 

### Return type

[**ReadDiskResponse**](ReadDiskResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_interfaces**
> ReadInterfacesResponse read_interfaces(body)

Reads out data of the interfaces of a device.

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
api_instance = thola_client.ReadApi(thola_client.ApiClient(configuration))
body = thola_client.ReadInterfacesRequest() # ReadInterfacesRequest | Request to process.

try:
    # Reads out data of the interfaces of a device.
    api_response = api_instance.read_interfaces(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->read_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReadInterfacesRequest**](ReadInterfacesRequest.md)| Request to process. | 

### Return type

[**ReadInterfacesResponse**](ReadInterfacesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_memory_usage**
> ReadMemoryUsageResponse read_memory_usage(body)

Read out the memory usage of a device.

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
api_instance = thola_client.ReadApi(thola_client.ApiClient(configuration))
body = thola_client.ReadMemoryUsageRequest() # ReadMemoryUsageRequest | Request to process.

try:
    # Read out the memory usage of a device.
    api_response = api_instance.read_memory_usage(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->read_memory_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReadMemoryUsageRequest**](ReadMemoryUsageRequest.md)| Request to process. | 

### Return type

[**ReadMemoryUsageResponse**](ReadMemoryUsageResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_sbc**
> ReadSBCResponse read_sbc(body)

Reads out SBC data of a device.

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
api_instance = thola_client.ReadApi(thola_client.ApiClient(configuration))
body = thola_client.ReadSBCRequest() # ReadSBCRequest | Request to process.

try:
    # Reads out SBC data of a device.
    api_response = api_instance.read_sbc(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->read_sbc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReadSBCRequest**](ReadSBCRequest.md)| Request to process. | 

### Return type

[**ReadSBCResponse**](ReadSBCResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_server**
> ReadServerResponse read_server(body)

Reads out server data of a device.

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
api_instance = thola_client.ReadApi(thola_client.ApiClient(configuration))
body = thola_client.ReadServerRequest() # ReadServerRequest | Request to process.

try:
    # Reads out server data of a device.
    api_response = api_instance.read_server(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->read_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReadServerRequest**](ReadServerRequest.md)| Request to process. | 

### Return type

[**ReadServerResponse**](ReadServerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ups**
> ReadUPSResponse read_ups(body)

Reads out UPS data of a device.

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
api_instance = thola_client.ReadApi(thola_client.ApiClient(configuration))
body = thola_client.ReadUPSRequest() # ReadUPSRequest | Request to process.

try:
    # Reads out UPS data of a device.
    api_response = api_instance.read_ups(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->read_ups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReadUPSRequest**](ReadUPSRequest.md)| Request to process. | 

### Return type

[**ReadUPSResponse**](ReadUPSResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

