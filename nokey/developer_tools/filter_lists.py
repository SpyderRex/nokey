import requests_cache
from .. helperFuncs import make_request as mr

class FilterLists:
    """
    A class for interacting with the FilterLists API.
    
    Attributes:
    - base_url: The base URL of the FilterLists API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="filter_lists_cache", backend="sqlite", expire_after=3600):
        self.base_url = "http://filterlists.com/api/directory/"
        self.about = "The FilterLists Directory API provides lists of filters used by AD blockers."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the FilterLists API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://filterlists.com/api/#/"
        
    def get_languages(self):
        """
        Returns the languages targeted by the FilterLists.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing a list of languages targeted by the FilterLists.
        """
        endpoint = "languages"
        return mr.make_request(self.base_url+endpoint)
        
    def get_licenses(self):
        """
        Returns the licenses applied to the FilterLists.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing a list of licenses applied to the FilterLists.
        """
        endpoint = "licenses"
        return mr.make_request(self.base_url+endpoint)
        
    def get_lists(self):
        """
        Returns the FilterLists.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing the FilterLists.
        """
        endpoint = "lists"
        return mr.make_request(self.base_url+endpoint)
        
    def get_list_by_id(self, list_id):
        """
        Returns details of a specific FilterList matching the given id.
        
        Args:
        - list_id (int): A unique numerical identifier for a FilterList.
        
        Returns:
        - dict: A dictionary containing details of the FilterList.
        """
        endpoint = f"lists/{list_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_maintainers(self):
        """
        Returns the maintainers of the FilterLists.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing the maintainers of the FilterLists.
        """
        endpoint = "maintainers"
        return mr.make_request(self.base_url+endpoint)
        
    def get_software(self):
        """
        Returns the software that subscribes to the FilterLists.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing the software that subscribes to the FilterLists.
        """
        endpoint = "software"
        return mr.make_request(self.base_url+endpoint)
        
    def get_syntaxes(self):
        """
        Returns the syntaxes of the FilterLists.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing the syntaxes of the FilterLists.
        """
        endpoint = "syntaxes"
        return mr.make_request(self.base_url+endpoint)
        
    def get_tags(self):
        """
        Returns the tags of the FilterLists.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing the tags of the FilterLists.
        """
        endpoint = "tags"
        return mr.make_request(self.base_url+endpoint)
       
       
       
       
    
    
    
    