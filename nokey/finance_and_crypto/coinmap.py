from datetime import date
from typing import Optional
import requests_cache
from .. helperFuncs import make_request as mr

class Coinmap:
    """
    A class for interacting with the Coinmap API.
    
    Attributes:
    - base_url: The base URL of the Coinmap API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="coinmap_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://coinmap.org/api/v1/"
        self.about = "The CoinMap API is a free resource to access data about thousands of crypto merchants, ATMs, grocery stores, shops, cafes, and other venues. This API is really simple to use since it has a flat data structure, doesn't require authorization, and a well-described data format."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Coinmap API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://coinmap.org/api/"
        
    def get_venues(self, min_lat: Optional[float] = None, max_lat: Optional[float] = None, min_lon: Optional[float] = None,
                   max_lon: Optional[float] = None, query: Optional[str] = None, category: Optional[str] = None,
                   owner: Optional[str] = None, upvoter: Optional[str] = None, before: Optional[date] = None,
                   after: Optional[date] = None, promoted: Optional[bool] = None, limit: Optional[int] = None,
                   offset: Optional[int] = None):
        """
        Returns a list of venues with crypto ATMs.
        
        Args:
        - min_lat (float): Minimum latitude (>=)
        - max_lat (float): Maximum latitude (<=)
        - min_lon (float): Minimum longitude (>=)
        - max_lon (float): Maximum longitude (<=)
        - query (str): Substring search in venue names
        - category (str): Filter category
        - owner (str): Venue owner (userhash)
        - upvoter (str): User who upvoted the venue (userhash)
        - before (date): Only show venues created before YYYY-MM-DD
        - after (date): Only show venues created after YYYY-MM-DD
        - promoted (bool): Show promoted venues (unset = both)
        - limit (int): Limit number of results
        - offset (int): Skip first N results
        
        Returns:
        - dict: A dictionary containing a list of venues with crypto ATMs.
        """
        endpoint = "venues"
        params = {}

        if min_lat is not None:
            params['lat1'] = min_lat
        if max_lat is not None:
            params['lat2'] = max_lat
        if min_lon is not None:
            params['lon1'] = min_lon
        if max_lon is not None:
            params['lon2'] = max_lon
        if query is not None:
            params['query'] = query
        if category is not None:
            params['category'] = category
        if owner is not None:
            params['owner'] = owner
        if upvoter is not None:
            params['upvoter'] = upvoter
        if before is not None:
            params['before'] = before.strftime('%Y-%m-%d')
        if after is not None:
            params['after'] = after.strftime('%Y-%m-%d')
        if promoted is not None:
            params['promoted'] = promoted
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset

        return mr.make_request_with_params(self.base_url + endpoint, params=params)
        
    def get_venue_by_id(self, venue_id):
        """
        Returns a venue matching the given id.
        
        Args:
        - venue_id (str): A unique number identifying a specific venue.
        
        Returns:
        - dict: A dictionary containing information about the venue matching the given id.
        """
        endpoint = f"venues/{venue_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_comments_by_venue_id(self, venue_id):
        """
        Returns a list of comments about the venue matching the given id.
        
        Args:
        - venue_id (str): A unique number identifying a specific venue.
        
        Returns:
        - dict: A dictionary containing a list of comments about the venue matching the given id.
        """
        endpoint = f"venues/{venue_id}/comments"
        return mr.make_request(self.base_url+endpoint)
        
    def get_ratings_by_venue_id(self, venue_id):
        """
        Returns ratings about the venue matching the given id.
        
        Args:
        - venue_id (str): A unique number identifying a specific venue.
        
        Returns:
        - dict: A dictionary containing ratings about the venue matching the given id.
        """
        endpoint = f"venues/{venue_id}/ratings"
        return mr.make_request(self.base_url+endpoint)
        
    def get_atm_operators(self):
        """
        Returns a list of ATM operators.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing a list of ATM operators.
        """
        endpoint = "atm-operators"
        return mr.make_request(self.base_url+endpoint)
        
    def get_coins(self):
        """
        Returns a list of coins.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing a list of coins.
        """
        endpoint = "coins"
        return mr.make_request(self.base_url+endpoint)

# LISTED IN THE DOCS AS A VALID ENDPOINT, BUT IT THROWS UP AN ERROR. POSSIBLY DEPRECATED.    
#    def get_atm_providers(self):
#        """
#        Returns a list of ATM providers.
#        
#        Args:
#        - None
#        
#        Returns:
#        - dict: A dictionary containing a list of ATM providers.
#        """
#        endpoint = "providers"
#        return mr.make_request(self.base_url+endpoint)
        
    
    
        
        
        