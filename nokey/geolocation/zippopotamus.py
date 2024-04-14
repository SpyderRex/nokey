from .. helperFuncs import make_request as mr

class Zippopotomus:
    """
    A class to interact with the Zippopotomus API.
    
    Attributes:
    - base_url: The basee URL of the API.
    """
    def __init__(self):
        self.base_url = "http://api.zippopotam.us/"
        
    def get_docs_url(self):
        """
        Returns the URL for the Zippopotomus API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://www.zippopotam.us/"
        
    def get_info_by_zipcode(self, country, zipcode):
        """
        Returns information on a given zipcode in a given country.
        
        Args:
        - country (str): The country code as defined in the API docs. See docs for supported countries. 
        - zipcode (int): The zipcode in question. See docs for range and format of zipcodes by country.
        
        Returns:
        - dict: A dictionary containing information about the given zipcode in the given country.
        """
        endpoint = f"{country}/{zipcode}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_zipcode_by_city(self, country, state, city):
        """
        Returns the zipcode(s) of the city matching the parameters.
        
        Args:
        - country (str): The country code as defined in the API docs.
        - state (str): The state code.
        - city (str): The city in question.
        
        Returns:
        - dict: A dictionary containing the zipcode of the given location.
        """
        endpoint = f"{country}/{state}/{city}"
        return mr.make_request(self.base_url+endpoint)