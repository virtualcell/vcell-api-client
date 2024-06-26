# VCell API client


[![pypi](https://img.shields.io/pypi/v/vcell-api-client.svg)](https://pypi.org/project/vcell-api-client/)
[![python](https://img.shields.io/pypi/pyversions/vcell-api-client.svg)](https://pypi.org/project/vcell-api-client/)
[![Build Status](https://github.com/virtualcell/vcell-api-client/actions/workflows/python.yml/badge.svg)](https://github.com/virtualcell/vcell-api-client/actions/workflows/python.yml)
[![codecov](https://codecov.io/gh/virtualcell/vcell-api-client/branch/main/graphs/badge.svg)](https://codecov.io/github/virtualcell/vcell-api-client)



Client library to connect to VCell remote API


* Documentation: <https://virtualcell.github.io/vcell-api-client>
* GitHub: <https://github.com/virtualcell/vcell-api-client>
* PyPI: <https://pypi.org/project/vcell-api-client/>
* Free software: MIT


## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.

## Background

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.1
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [http://exampleurl.com/contact](http://exampleurl.com/contact)

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import vcell_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import vcell_api_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import vcell_api_client
from vcell_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://vcellapi-test.cam.uchc.edu
# See configuration.py for a list of all supported configuration parameters.
configuration = vcell_api_client.Configuration(
    host = "https://vcellapi-test.cam.uchc.edu"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.


# Enter a context with an instance of the API client
with vcell_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vcell_api_client.AdminResourceApi(api_client)

    try:
        # Get usage summary
        api_response = api_instance.get_usage()
        print("The response of AdminResourceApi->get_usage:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminResourceApi->get_usage: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://vcellapi-test.cam.uchc.edu*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminResourceApi* | [**get_usage**](docs/AdminResourceApi.md#get_usage) | **GET** /api/v1/admin/usage | Get usage summary
*BioModelResourceApi* | [**delete_bio_model**](docs/BioModelResourceApi.md#delete_bio_model) | **DELETE** /api/v1/bioModel/{bioModelID} | Delete the BioModel from VCell&#39;s database.
*BioModelResourceApi* | [**get_biomodel_by_id**](docs/BioModelResourceApi.md#get_biomodel_by_id) | **GET** /api/v1/bioModel/{bioModelID} | Get BioModel information in JSON format by ID.
*BioModelResourceApi* | [**upload_bio_model**](docs/BioModelResourceApi.md#upload_bio_model) | **POST** /api/v1/bioModel/upload_bioModel | Upload the BioModel to VCell database. Returns BioModel ID.
*HelloWorldApi* | [**get_hello_world**](docs/HelloWorldApi.md#get_hello_world) | **GET** /api/v1/helloworld | Get hello world message.
*PublicationResourceApi* | [**create_publication**](docs/PublicationResourceApi.md#create_publication) | **POST** /api/v1/publications | Create publication
*PublicationResourceApi* | [**delete_publication**](docs/PublicationResourceApi.md#delete_publication) | **DELETE** /api/v1/publications/{id} | Delete publication
*PublicationResourceApi* | [**get_publication_by_id**](docs/PublicationResourceApi.md#get_publication_by_id) | **GET** /api/v1/publications/{id} | Get publication by ID
*PublicationResourceApi* | [**get_publications**](docs/PublicationResourceApi.md#get_publications) | **GET** /api/v1/publications | Get all publications
*PublicationResourceApi* | [**update_publication**](docs/PublicationResourceApi.md#update_publication) | **PUT** /api/v1/publications | Create publication
*UsersResourceApi* | [**forgot_legacy_password**](docs/UsersResourceApi.md#forgot_legacy_password) | **POST** /api/v1/users/forgotLegacyPassword | The end user has forgotten the legacy password they used for VCell, so they will be emailed it.
*UsersResourceApi* | [**get_legacy_api_token**](docs/UsersResourceApi.md#get_legacy_api_token) | **POST** /api/v1/users/bearerToken | Get token for legacy API
*UsersResourceApi* | [**get_mapped_user**](docs/UsersResourceApi.md#get_mapped_user) | **GET** /api/v1/users/mappedUser | Get mapped VCell identity
*UsersResourceApi* | [**get_me**](docs/UsersResourceApi.md#get_me) | **GET** /api/v1/users/me | Get current user
*UsersResourceApi* | [**map_new_user**](docs/UsersResourceApi.md#map_new_user) | **POST** /api/v1/users/newUser | create vcell user
*UsersResourceApi* | [**map_user**](docs/UsersResourceApi.md#map_user) | **POST** /api/v1/users/mapUser | map vcell user
*UsersResourceApi* | [**unmap_user**](docs/UsersResourceApi.md#unmap_user) | **PUT** /api/v1/users/unmapUser/{userName} | remove vcell identity mapping


## Documentation For Models

 - [AccesTokenRepresentationRecord](docs/AccesTokenRepresentationRecord.md)
 - [BioModel](docs/BioModel.md)
 - [BiomodelRef](docs/BiomodelRef.md)
 - [HelloWorldMessage](docs/HelloWorldMessage.md)
 - [Identity](docs/Identity.md)
 - [MathmodelRef](docs/MathmodelRef.md)
 - [Publication](docs/Publication.md)
 - [Simulation](docs/Simulation.md)
 - [UserIdentityJSONSafe](docs/UserIdentityJSONSafe.md)
 - [UserLoginInfoForMapping](docs/UserLoginInfoForMapping.md)
 - [UserRegistrationInfo](docs/UserRegistrationInfo.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="openId"></a>
### openId



## Author

vcell_support@uchc.com


