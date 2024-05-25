import requests_cache
from .. helperFuncs import make_request as mr

class Microlink:
    """
    A class for interacting with the Microlink API.
    
    Attributes:
    - base_url: The base URL of the API.
    - about: A short description of the API.
    """
    
    def __init__(self, use_caching=False, cache_name="microlink_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://api.microlink.io"
        self.about = "Microlink API provides a powerful API for automating any browser action. Free use is limited to 50 requests a day."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Microlink API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://microlink.io/docs/api/getting-started/overview"
        
    def get_metadata_for_target_url(self, url):
        """
        Returns metadata for the target URL.
        
        Args:
        - url (str): The target URL.
        
        Returns:
        - dict: A dictionary containing metadata for the target URL.
        """
        params = {'url': url}
        return mr.make_request_with_params(self.base_url, params)
        
    def get_screenshot_of_target_url(self, url):
        """
        Returns the URL for a screenshot of the target URL.
        
        Args:
        - url (str): The target URL.
        
        Returns:
        - string: The URL for the screenshot of the target URL.
        """
        params = {'url': url, "screenshot": True}
        metadata = mr.make_request_with_params(self.base_url, params)
        return metadata["data"]["screenshot"]["url"]
        
    def get_pdf_of_target_url(self, url):
        """
        Returns the URL for a pdf of the target URL.
        
        Args:
        - url (str): The target URL.
        
        Returns:
        - string: The URL for the pdf of the target URL.
        """
        params = {'url': url, "pdf": True}
        metadata = mr.make_request_with_params(self.base_url, params)
        return metadata["data"]["pdf"]["url"]
        
    def get_color_palette_for_target_url(self, url):
        """
        Returns metadata containing the predominant color pallette for each image detected over the target URL.
        
        Args:
        - url (str): The target URL.
        
        Returns:
        - dict: A dictionary of metadata containing the predominant color pallette for each image detected over the target URL.
        """
        params = {'url': url, "palette": True}
        metadata = mr.make_request_with_params(self.base_url, params)
        return metadata
        
        

        
        