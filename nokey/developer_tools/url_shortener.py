import requests_cache
from .. helperFuncs import make_request as mr
from .. helperFuncs.throttler import throttle_class

@throttle_class(rate_limit=200, period=3600)
class UrlShortener:
    """
    A class for interacting with the URL Shortener API.
    
    Attributes:
    - base_url: The base URL of the URL Shortener API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="url_shortener_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://is.gd/create.php?"
        self.about = "This URL Shortener API (from is.gd) is a URL shortener service."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the URL Shortener API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs
        """
        return "https://is.gd/apishorteningreference.php?"
        
    def shorten_url(self, url, shorturl=None):
        """
        Returns the shortened URL for the given parameters.
        
        Args:
        - url (str): The original URL to be shortened.
        - shorturl (str): Optional parameter for a desired short URL if available (case sensitive). Must be between 5 and 30 characters. Defaults to None.
        
        Returns:
        - dict: Dictionary containing the shortened URL.
        """
        if shorturl is not None:
            if len(shorturl) < 31 and len(shorturl) > 4:
                endpoint = f"format=json&url={url}&shorturl={shorturl}"
            else:
                print("Chosen shortened URL must be between 5 and 30 characters")
                return ""
        else:
            endpoint = f"format=json&url={url}"
            return mr.make_request(self.base_url+endpoint)
                    
                    