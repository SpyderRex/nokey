import requests_cache
from .. helperFuncs import make_request as mr

class Fruityvice:
    """
    A class to interact with the Fruityvice API.
    
    Attributes:
    - base_url: The base url of the Fruityvice API.
    - about: A short description of the API.
    """
    
    def __init__(self, use_caching=False, cache_name="fruityvice_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://www.fruityvice.com/api/fruit/"
        self.about = "Fruityvice is an API that provides information on fruits and their nutritional value."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the url for the Fruityvice API documentation.
        
        Args:
        - None
        
        Returns:
        - string: URL for API documentation.
        """
        return "https://www.fruityvice.com/doc/index.html"
        
    def get_all_fruit(self):
        """
        Returns all the fruit listed in the Fruityvice API.
        
        Args:
        - None
        
        Returns:
        - dict: Dictionary containing all the fruit listed in the API.
        """
        endpoint = "all"
        return mr.make_request(self.base_url+endpoint)
        
    def get_fruit_by_nutrition(self, nutrition, minVal=0, maxVal=1000):
        """
        Returns a fruit with its information based on a minimum and maximum range of values for the specified nutritional component.
        
        Args:
        - nutrition (str): A nutritional component. Possible values are carbohydrates, protein, fat, calories, and sugar.
        - minVal (float): The minimum value of the range specified for nutritional component (per 100g of the fruit). Defaults to its minimum possible value, which is 0.
        - maxVal (float): The maximum value of the range specified for nutritional component (per 100g of the fruit). Defaults to its maximum possible value, which is 1000.
        
        Returns:
        - dict: Dictionary containing information on the fruit matching the specified values.
        """
        endpoint = f"{nutrition}?min={minVal}&max={maxVal}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_fruit_by_family(self, family):
        """
        Returns fruit matching the given family.
        
        Args:
        - family (str): The name of a fruit family.
        
        Returns:
        -dict: Dictionary containing fruit of the given family.
        """
        endpoint = f"family/{family}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_fruit_by_genus(self, genus):
        """
        Returns fruit matching the given genus.
        
        Args:
        - genus (str): The name of a fruit genus.
        
        Returns:
        -dict: Dictionary containing fruit of the given genus.
        """
        endpoint = f"genus/{genus}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_fruit_by_order(self, order):
        """
        Returns fruit matching the given order.
        
        Args:
        - order (str): The name of a fruit order.
        
        Returns:
        -dict: Dictionary containing fruit of the given order.
        """
        endpoint = f"order/{order}"
        return mr.make_request(self.base_url+endpoint)
     
     
        
    
