import requests_cache
from .. helperFuncs import make_request as mr

class ExchangeAPI:
    """
    A class for interacting with Exchange API.
    
    Attributes:
    - base_url: The base URL of the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="exchange_api_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@"
        self.about = "ExchangeAPI is a free currency exchange rates API with 150+ currencies and no rate limits."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the ExchangeAPI documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://github.com/fawazahmed0/exchange-api"
        
    def get_available_currencies(self, minified_version=False):
        """
        Returns all the available currencies in the API.
        
        Args:
        - minified_version (bool): An optional parameter for getting a minified version of the currency list. Default is false.
        
        Returns:
        - dict: A dictionary containing a list of the available currencies.
        """
        if minified_version:
            endpoint = "latest/v1/currencies.min.json"
            print(endpoint)
            return mr.make_request(self.base_url+endpoint)
        else:
            endpoint = "latest/v1/currencies.json"
            return mr.make_request(self.base_url+endpoint)
            
    def get_rates_from_base(self, currency_code, date="latest", minified_version=False):
        """
        Returns exchange rates list for the given currency code on the given date.
        
        Args:
        - currency_code (str): The code for the base currency used to get exchange rates.
        - date (str): Date for the exchange rates. Default is latest, but other values must be in YYYY-MM-DD format.
        - minified_version (bool): An optional parameter for getting a minified version of the currency list. Default is false.
        
        Returns:
        - dict: A dictionary containing a list of exchange rates.
        """
        if minified_version:
            endpoint = f"{date}/v1/currencies/{currency_code.lower()}.min.json"
            print(endpoint)
            return mr.make_request(self.base_url+endpoint)
        else:
            endpoint = f"{date}/v1/currencies/{currency_code.lower()}.json"
            return mr.make_request(self.base_url+endpoint)
            
    
            
    
        
        
        