import requests_cache
from .. helperFuncs import make_request as mr
from .. helperFuncs.throttler import throttle_class

@throttle_class(rate_limit=120, period=60)
class JokeAPI:
    """
    A class to interact with the JokeAPI API.
    
    Attributes:
    - base_url: Base URL for interacting with the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching="False", cache_name="joke_api_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://v2.jokeapi.dev/joke/"
        self.about = "JokeAPI is a REST API that serves uniformly and well formatted jokes. It can be used without any API token, membership, registration or payment. It supports a variety of filters that can be applied to get just the right jokes you need."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the JokeAPI documentation.
        
        Args:
        - None
        
        Returns:
        - string: The url for the API documentation.
        """
        return "https://sv443.net/jokeapi/v2/"
        
    def get_joke(self, category=None, lang=None, flags=None, joke_type=None, search_string=None, amount=None):
        """
        Returns joke(s) matching the given parameters.
    
        Args:
        - category (str): Joke category. Defaults to Any. Possible non-default values are Programming, Misc, Dark, Pin, Spooky, and Christmas.
        - lang (str): Language of the joke. Defaults to en (English). Possible other values are cs (Czech), de (German), es (Spanish), fr (French), and pt (Portuguese).
        - flags (str): Optional flags to blacklist. Possible values are nsfw, religious, political, racist, sexist, and explicit.
        - joke_type (str): Optional parameter for either single or twopart joke(s). Defaults to None.
        - search_string (str): Optional search string contained in desired joke(s). Defaults to None.
        - amount (int): Number of jokes returned. Defaults to 1.
    
        Returns:
        - dict: A dictionary containing joke(s) matching given parameters.
        """
        endpoint = ""
    
        if category is not None:
            endpoint += f"{category}"
        else:
            endpoint += "Any"
        
        if lang is not None:
            endpoint += f"?lang={lang}"
        
        if flags is not None:
            if "?" not in endpoint:
                endpoint += f"?blacklistFlags={flags}"
            else:
                endpoint += f"&blacklistFlags={flags}"
            
        if joke_type is not None:
            if "?" not in endpoint:
                endpoint += f"?type={joke_type}"
            else:
                endpoint += f"&type={joke_type}"
            
        if search_string is not None:
            if "?" not in endpoint:
                endpoint += f"?contains={search_string}"
            else:
                endpoint += f"&contains={search_string}"
            
        if amount is not None:
            if "?" not in endpoint:
                endpoint += f"?amount={amount}"
            else:
                endpoint += f"&amount={amount}"
        
        return mr.make_request(self.base_url+endpoint)

        
      