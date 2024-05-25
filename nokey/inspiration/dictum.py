import requests_cache
from .. helperFuncs import make_request as mr

class Dictum:
    """
    A class for interacting with the Dictum API.
    
    Attributes:
    - base_url: The base URL of the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="dictum_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://api.fisenko.net/v1/"
        self.about = "Dictum API provides a programmatic way to access the most inspiring expressions of humanity."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Dictum API documentation.
        
        Args:
        - None
        
        Returns:
        -string: The URL for the API docs.
        """
        return "https://api.fisenko.net/swagger-ui/"
        
    def get_inspiring_authors(self, language="en", search_query=None, offset=0, limit=0):
        """
        Returns list of authors featured in the API based on the given parameters.
        
        Args:
        - language (str): The language of the author. Default is en (English). Only other value supported is ru (Russian).
        - search_query (str): The search query matching the author's name. Default is None.
        - offset (int): The page offset for the list of authors. Default is 0.
        - limit (int): The number of items.
        
        Returns:
        - dict: A dictionary containing the authors matching the given parameters, along with the unique identifier for the author.
        """
        if search_query is not None:
            endpoint = f"authors/{language}?query={search_query}&offset={offset}&limit={limit}"
        else:
            endpoint = f"authors/{language}?&offset={offset}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_inspiring_author_by_id(self, authorID, language="en"):
        """
        Returns the author matching the unique identifier.
        
        Args:
        - language (str): The language of the author. Defaults to en (English). Only other value supported is ru (Russian).
        - authorID (str): A unique hexadecimal string identifying a specific author in the API.
        
        Returns:
        - dict: A dictionary containing the author matching the given id.
        """
        endpoint = f"authors/{language}/{authorID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_inspiring_quotes_by_author_id(self, authorID, language="en"):
        """
        Returns quotes from an author matching the unique identifier.
        
        Args:
        - language (str): The language of the author. Defaults to en (English). Only other value supported is ru (Russian).
        - authorID (str): A unique hexadecimal string identifying a specific author in the API.
        
        Returns:
        - dict: A dictionary containing quotes from the author matching the given id.
        """
        endpoint = f"authors/{language}/{authorID}/quotes"
        return mr.make_request(self.base_url+endpoint)
        
    def get_languages(self):
      """
      Returns a list of author languages used in the API.
      
      Args:
      - None
      
      Returns:
      - dict: A dictionary containing a list of languages (as of this time, only Russian and English)
      """
      endpoint = "languages"
      return mr.make_request(self.base_url+endpoint)
      
    def get_inspiring_quotes(self, language="en", search_query=None, offset=0, limit=0):
        """
        Returns list of quotes matching the given parameters.
        
        Args:
        - language (str): The language of the author. Default is en (English). Only other value supported is ru (Russian).
        - search_query (str): The search query matching the quote. Default is None.
        - offset (int): The page offset for the list of quotes. Default is 0.
        - limit (int): The number of items.
        
        Returns:
        - dict: A dictionary containing the quotes matching the given parameters, along with the unique identifier for the author.
        """
        if search_query is not None:
            endpoint = f"quotes/{language}?query={search_query}&offset={offset}&limit={limit}"
        else:
            endpoint = f"quotes/{language}?&offset={offset}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_random_quote(self, language="en"):
        """
        Returns a random quote.
        
        Args:
        - language (str): Language of the quote. Defaults to en (English). Only other value supported is ru (Russian).
        
        Returns:
        - dict: A dictionary containing the random quote.
        """
        endpoint = f"quotes/{language}/random"
        return mr.make_request(self.base_url+endpoint)
        
    def get_inspiring_quote_by_quote_id(self, quoteID, language="en"):
        """
        Returns a quote  matching the unique identifier.
        
        Args:
        - language (str): The language of the author. Defaults to en (English). Only other value supported is ru (Russian).
        - quoteID (str): A unique hexadecimal string identifying a specific quote in the API.
        
        Returns:
        - dict: A dictionary containing a quote matching the given id.
        """
        endpoint = f"quotes/{language}/{quoteID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_number_of_quotes_and_authors(self, language="en"):
        """
        Returns the number of quotes and authors in the API for the given language.
        
        Args:
        - language (str). The language of the quotes. Defaults to en (English). Only other value supported is ru (Russian).
        
        Returns:
        - dict: Dictionary containing the number of authors and quotes for the given language.
        """
        endpoint = f"statistics/{language}"
        return mr.make_request(self.base_url+endpoint)
        
       
    
      
    
      
        