import requests_cache
from .. helperFuncs import make_request as mr

class APIsGuru:
    """
    A class to interact with the APIs.guru API.
    
    Attributes:
    - base_url: The base url for the APIs.guru API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="api_gurus_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://api.apis.guru/v2/"
        self.about = "The APIs.guru API is a self-proclaimed Wikipedia for APIs, maintaining an Open API directory."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the APIs.guru API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://apis.guru/api-doc/"
        
    def get_all_providers(self):
        """
        Returns a list of all the providers in the API directory.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing a list of all the providers in the directory.
        """
        endpoint = "providers.json"
        return mr.make_request(self.base_url+endpoint)
        
    def get_apis_by_provider(self, provider):
        """
        Returns a list of all the APIs for a particular provider.
        
        Args:
        - provider (str): The name of the api provider.
        
        Returns:
        - dict: A dictionary containing a list of all the APIs for a particular provider.
        """
        endpoint = f"{provider}.json"
        return mr.make_request(self.base_url+endpoint)
        
    def get_service_names_by_provider(self, provider):
        """
        Returns a list of all the services for a particular provider.
        
        Args:
        - provider (str): The name of the provider.
        
        Returns:
        - dict: A dictionary containing a list of all the services for a particular provider.
        """
        endpoint = f"{provider}/services.json"
        return mr.make_request(self.base_url+endpoint)
        
    def get_particular_api_version_no_service_name(self, provider, api):
        """
        Returns the API entry for one specific version of an API where there is no service name.
        
        Args:
        - provider (str): The name of the provider.
        - api (str): The api.
        
        Returns:
        - dict: A dictionary containing the API entry for one specific version of an API where there is no service name.
        """
        endpoint = f"specs/{provider}/{api}.json"
        return mr.make_request(self.base_url+endpoint)
        
    def get_particular_api_version_with_service_name(self, provider, service, api):
        """
        Returns the API entry for one specific version of an API where there is a s ervice name.
        
        Args:
        - provider (str): The name of the provider.
        - service (str): The name of the service.
        - api (str): The name of the API.
        
        Returns:
        - dict: A dictionary containing the API entry for one specific version of an API where there is a service name.
        """
        endpoint = f"specs/{provider}/{service}/{api}.json"
        return mr.make_request(self.base_url+endpoint)
        
    def get_all_apis(self):
        """
        Returns a list of all the APIs in the API directory.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing a list of all the APIs in the directory.
        """
        endpoint = "list.json"
        return mr.make_request(self.base_url+endpoint)
        
    def get_basic_metrics(self):
        """
        Returns basic metrics for the entire API directory.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing basic metrics for the entire directory.
        """
        endpoint = "metrics.json"
        return mr.make_request(self.base_url+endpoint)
  
  
        
        
    
      
      
      
        