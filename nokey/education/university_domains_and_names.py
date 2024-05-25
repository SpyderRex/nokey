import requests_cache
from .. helperFuncs import make_request as mr

class UniversityDomainsAndNames:
    """
    A class to interact with the University Domains and Names API.
    
    Attributes:
    - base_url: The base url for the University Domains and Names API.
    - about: A short description of the API.
    """
    
    def __init__(self, use_caching=False, cache_name="university_cache", backend="sqlite", expire_after=3600):
        self.base_url = "http://universities.hipolabs.com/search?"
        self.about = "This API accesses a list of universities and their domain names."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the url for the University Domains and Names API documentation.
        
        Args:
        - None
        
        Returns:
        - string: URL for API documentation.
        """
        return "https://github.com/Hipo/university-domains-list"
        
    def get_university_name_and_domain(self, name, country, offset=None, limit=None):
        """
        Returns university names and domains for the given parameters.
        
        Args:
        - name (str): Whole or partial name of university in question.
        - country (str): Country of university in question.
        - offset (int): Optional pagination parameter to limit search. Defaults to None.
        - limit (int): Optional pagination parameter to limit number of results. Defaults to None.
        
        Returns:
        - dict: List containing universities matching parameters with their respective domains.
        """
        if offset is not None and limit is not None:
            endpoint = f"name={name}&country={country}&offset={offset}&limit={limit}"
        elif offset is not None:
            endpoint = f"name={name}&country={country}&offset={offset}"
        elif limit is not None:
            endpoint = f"name={name}&country={country}&limit={limit}"
        else:
            endpoint = f"name={name}&country={country}"
        return mr.make_request(self.base_url+endpoint)
        
    def update_list(self):
        """
        Forces a refresh of the API, since the API won't automatically update the dataset if it changes.
        
        Args:
        - None
        
        Returns:
        - dict: An updated, refreshed list of the university dataset.
        """
        endpoint = "update"
        return mr.make_request(self.base_url+endpoint)
        
        
        
      
        