import requests_cache
from .. helperFuncs import make_request as mr


class RestCountries:
    """
    A class to interact with the RestCountries API.
    
    Attributes:
    - base_url: The base URL of the RestCountries API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="rest_country_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://restcountries.com/v3.1/"
        self.about = "REST Countries API is a simple REST API from RapidAPI that provides information about countries in the world In JSON format."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns url for API docs.
        
        Args:
        - None
        
        Returns:
        - string: Url for the API documentation.
        """
        return "https://restcountries.com/"
    
    def get_country_by_name(self, name):
        """
        Returns information about a country by its name.

        Args:
        - name (str): The name of the country.

        Returns:
        - dict: Information about the country, or an error if country not found.
        """
        endpoint = f"name/{name}"
        return mr.make_request(self.base_url+endpoint)
    
    def get_country_by_code(self, code):
        """
        Returns information about a country by its code (cca2, ccn3, cca3, or cioc).

        Args:
        - code (str): The country code.

        Returns:
        - dict: Information about the country, or an error if country not found.
        """
        endpoint = f"alpha/{code}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_country_by_currency(self, currency):
        """
        Returns information about countries that use a specific currency.

        Args:
        - currency (str): The currency code or name.

        Returns:
        - list: A list of dictionaries containing information about countries using the currency, or an error if no countries found.
        """
        endpoint = f"currency/{currency}"
        return mr.make_request(self.base_url+endpoint)

    def get_country_by_language(self, language):
        """
        Returns information about countries speaking a given language.

        Args:
        - language (str): The name of the spoken language of the country.

        Returns:
        - list: A list of dictionaries containing information about countries using the language, or an error if no countries found.
        """
        endpoint = f"lang/{language}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_country_by_capital(self, capital):
        """
        Returns information about a country with the given capital

        Args:
        - capital (str): The name of the capital city.

        Returns:
        - list: A list of dictionaries containing information about countries using the capital, or an error if no countries found.
        """
        endpoint = f"capital/{capital}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_country_by_region(self, region):
        """
        Returns information about countries based on a given region.

        Args:
        - region (str): The name of the region.

        Returns:
        - list: A list of dictionaries containing information about countries using the region, or an error if no country is found.
        """
        endpoint = f"region/{region}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_country_by_subregion(self, subregion):
        """
        Returns information about countries based on a given subregion.

        Args:
        - subregion (str): The name of the subregion.

        Returns:
        - list: A list of dictionaries containing information about countries using the region, or an error if no country is found.
        """
        endpoint = f"subregion/{subregion}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_country_by_translation(self, translation):
        """
        Returns information about countries based on a translation of the name.

        Args:
        - translation (str): The name in a given translation.

        Returns:
        - list: A list of dictionaries containing information about countries using the region, or an error if no country is found.
        """
        endpoint = f"translation/{translation}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_all_countries(self):
        """
        Returns information about all countries listed in the API.

        Args:
        - None

        Returns:
        - list: A list of dictionaries containing information about all the countries, or an error if no data is found.
        """
        endpoint = "all"
        return mr.make_request(self.base_url+endpoint)
    

