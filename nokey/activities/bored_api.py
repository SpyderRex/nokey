import requests_cache
from .. helperFuncs import make_request as mr

class BoredAPI:
    """
    A class to interact with Bored API.
    
    Attributes:
    - base_url: The base URL of the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="bored_api_cache", backend="sqlite", expire_after=3600):
        self.base_url = "http://www.boredapi.com/api/"
        self.about = "The Bored API helps you find things to do when you're bored. There are fields like the number of participants, activity type, and more that help you narrow down your results."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Bored API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://www.boredapi.com/documentation"
        
    def get_random_activity(self):
        """
        Returns a random activity with related information.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing an activity along with related information.
        """
        endpoint = "activity"
        return mr.make_request(self.base_url+endpoint)
        
    def get_activity_by_key(self, key):
        """
        Returns an activity by its key.
        
        Args:
        - key (int): A unique number identifying a specific activity listed in the API (from 1000001 to 9999998).
        
        Returns:
        - dict: A dictionary containing a specific activity along with related information.
        """
        endpoint = f"activity/?key={key}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_random_activity_by_type(self, activityType):
        """
        Returns a random activity by its type.
        
        Args:
        - activityType (str): The type of activity. Supported values are education, recreational, social, diy, charity, cooking, relaxation, music, busywork.
        
        Returns:
        - dict: A dictionary containing a random activity along with related information.
        """
        endpoint = f"activity/?type={activityType}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_random_activity_by_participants(self, numParticipants):
        """
        Returns a random activity by its number of participants.
        
        Args:
        - numParticipants (int): The number of participants required by the activity. Supported values are 1 to n.
        
        Returns:
        - dict: A dictionary containing a random activity along with related information.
        """
        endpoint = f"activity/?participants={numParticipants}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_random_activity_by_price(self, price):
        """
        Returns a random activity by a specified price.
        
        Args:
        - price (float): The price of the activity, as imagined within a range from 0.0 to 1.0.
        
        Returns:
        - dict: A dictionary containing a random activity along with related information.
        """
        endpoint = f"activity/?price={price}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_random_activity_within_price_range(self, minprice, maxprice):
        """
        Returns a random activity within a specified price range.
        
        Args:
        - minprice (float): The minimum price of the activity, starting from 0.0.
        - maxprice (float): The maximum price of the activity, no greater than 1.0.
        
        Returns:
        - dict: A dictionary containing a random activity along with related information.
        """
        endpoint = f"activity/?minprice={minprice}&maxprice={maxprice}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_random_activity_by_accessibility(self, accessibility):
        """
        Returns a random activity by a specified accessibility.
        
        Args:
        - accessibility (float): The accessibility of the activity, as imagined within a range from 0.0 to 1.0., with 0.0 being most accessible.
        
        Returns:
        - dict: A dictionary containing a random activity along with related information.
        """
        endpoint = f"activity/?accessibility={accessibility}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_random_activity_within_accessibility_range(self, minAccessibility, maxAccessibility):
        """
        Returns a random activity within a specified accessibility range.
        
        Args:
        - minAccessibility (float): The minimum accessibility of the activity, with 0.0 being the most accessible.
        - maxAccessibility (float): The maximum accessibility of the activity, no greater than 1.0.
        
        Returns:
        - dict: A dictionary containing a random activity along with related information.
        """
        endpoint = f"activity/?minaccessibility={minAccessibility}&maxaccessibility={maxAccessibility}"
        return mr.make_request(self.base_url+endpoint)
     
   
  
  
        
        
    
    
    
    
        
