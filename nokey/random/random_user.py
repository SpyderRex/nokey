import requests_cache
from .. helperFuncs import make_request as mr

class RandomUserGenerator:
    """
    A class to interact with the Random User Generator API.
    
    Attributes:
    - base_url: The base url of the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="random_user_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://randomuser.me/api/"
        self.about = "The Random User Generator API is a free, open-source API for generating random user data, like Lorem Ipsum for people."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the url for the Random User Generator API documentation.
        
        Args:
        - None
        
        Returns:
        - string: URL for API documentation.
        """
        return "https://randomuser.me/"
        
    def generate_random_user(self):
        """
        Returns randomly generated data for a random user.
        
        Args:
        - None
        
        Returns:
        -dict: Dictionary containing random information (such as name, DOB, SSN, address, etc) for a random user.
        """
        return mr.make_request(self.base_url)
        