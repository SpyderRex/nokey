import requests_cache
from .. helperFuncs import make_request as mr

class StephenKingAPI:
    """
    A class to interact with the Stephen King API.
    
    Attributes:
    - base_url: The base URL of the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="stephen_king_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://stephen-king-api.onrender.com/api/"
        self.about = "The Stephen King API is for accessing the varied worked and villains of Stephen King's books and stories. (Note: This API is not entirely up to date.)"
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Stephen King API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://stephen-king-api.onrender.com/"
        
    def get_stephen_king_books(self):
        """
        Returns all of the Stephen King books and related metadata.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing book metadata.
        """
        endpoint = "books"
        return mr.make_request(self.base_url+endpoint)
        
    def get_stephen_king_book_by_id(self, book_id):
        """
        Returns the Stephen King book matching the id, with related metadata.
        
        Args:
        - book_id (int): A unique number identifying the Stephen King book.
        
        Returns:
        - dict: A dictionary containing book metadata.
        """
        endpoint = f"book/{book_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_stephen_king_short_stories(self):
        """
        Returns all of the Stephen King short stories and related metadata.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing short story metadata.
        """
        endpoint = "shorts"
        return mr.make_request(self.base_url+endpoint)
        
    def get_stephen_king_short_story_by_id(self, story_id):
        """
        Returns the Stephen King short story matching the id, with related metadata.
        
        Args:
        - story_id (int): A unique number identifying the Stephen King short story.
        
        Returns:
        - dict: A dictionary containing short story metadata.
        """
        endpoint = f"short/{story_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_stephen_king_villains(self):
        """
        Returns all of the Stephen King villains and related metadata.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing villain metadata.
        """
        endpoint = "villains"
        return mr.make_request(self.base_url+endpoint)
        
    def get_stephen_king_villain_by_id(self, villain_id):
        """
        Returns the Stephen King villain matching the id, with related metadata.
        
        Args:
        - villain_id (int): A unique number identifying the Stephen King villain.
        
        Returns:
        - dict: A dictionary containing villain metadata.
        """
        endpoint = f"villain/{villain_id}"
        return mr.make_request(self.base_url+endpoint)
   
   
  
   
 
        
        