import requests_cache
from .. helperFuncs import make_request as mr

class NobelPrizeAPI:
    """
    A class to interact with the Nobel Prize API.
    
    Attributes:
    - base_url: The base url for the Nobel Prize API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="nobel_prize_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://api.nobelprize.org/2.1/"
        self.about = "The Nobel Prize API returns all information about Laureates and Nobel Prizes."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Nobel Prize API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the Nobel Prize API docs.
        """
        return "https://www.nobelprize.org/about/developer-zone-2/"
        
    def get_nobel_prize_laureates(self):
        """
        Returns a list of Nobel Prize laureates with information about the winners.
        
        Args:
        - None
        
        Returns
        - dict: A dictionary containing a list of Nobel Prize laureates and relevant information about the winners.
        """
        endpoint = "laureates"
        return mr.make_request(self.base_url+endpoint)
        
    def get_all_nobel_prizes(self):
        """
        Returns a list of all the Nobel Prizes award along with information about the specific prize and winners.
        
        Args:
        - None
        
        Returns
        - dict: A dictionary containing a list of Nobel Prizes awarded and relevant information about the prize.
        """
        endpoint = "nobelPrizes"
        return mr.make_request(self.base_url+endpoint)
        
    def get_one_nobel_prize(self, category, year):
        """
        Returns a specific Nobel Prize and information about the specific prize and winners.
        
        Args:
        - category (str): The category of the prize awarded. Possible values are che (chemistry), eco (economic sciences), lit (literature), pea (peace), phy (physics), and med (medicine). Any other strings passed for category will return all the pieces for specified year.
        - year (int): The year the prize was awarded.
        
        Returns
        - dict: A dictionary containing a specific Nobel Prize awarded and relevant information about the prize.
        """
        endpoint = f"nobelPrize/{category.lower()}/{year}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_nobel_laureate_by_id(self, laureateID):
        """
        Returns a specific Nobel Prize and information about the specific prize and winners.
        
        Args:
        - laureateID (int): A unique identifier for a specific Nobel laureate.
        
        Returns
        - dict: A dictionary containing a specific Nobel Prize awarded and relevant information about the prize.
        """
        endpoint = f"laureate/{laureateID}"
        return mr.make_request(self.base_url+endpoint)
    
     
          
        
 