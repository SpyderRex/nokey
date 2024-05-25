import requests
import requests_cache
from .. helperFuncs import make_request as mr

class NagerDate:
    """
    A class to interact with the Nager.Date API.
    
    Attributes:
    - base_url: The base URL of the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="nager_date_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://date.nager.at/api/v3/"
        self.about = "The Nager.Date API provides a simple way to query the holidays of over 100 countries. It is also possible to query long weekends."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Nager.Date API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://date.nager.at/swagger/index.html"
        
    def get_country_info(self, countryCode):
        """
        Returns information about a given country.
        
        Args:
        - countryCode (str): The code representing one of over a hundred countries supported by the API.
        
        Returns:
        - dict: A dictionary containing information about the given country.
        """
        endpoint = f"CountryInfo/{countryCode}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_available_countries(self):
        """
        Returns all the countries available in the API.
        
        Args:
        - None
        
        Returns:
        - list: A list containing all the countries available in the API.
        """
        endpoint = "AvailableCountries"
        return mr.make_request(self.base_url+endpoint)
        
    def get_long_weekends_by_country(self, year, countryCode):
        """
        Returns a list of long weekends for a given country in a given year.
        
        Args:
        - year (int): The year in question.
        - countryCode (str): The code representing one of over a hundred countries supported by the API.
        
        Returns:
        - list: A list containing the long weekends for a given country in a given year.
        """
        endpoint = f"LongWeekend/{year}/{countryCode}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_public_holidays(self, year, countryCode):
        """
        Returns a list of public holidays for a given country in a given year.
        
        Args:
        - year (int): The year in question.
        - countryCode (str): The code representing one of over a hundred countries supported by the API.
        
        Returns:
        - list: A list containing the public holidays for a given country in a given year.
        """
        endpoint = f"PublicHolidays/{year}/{countryCode}"
        return mr.make_request(self.base_url+endpoint)
        
    def is_today_a_public_holiday(self, countryCode, utc_offset=0):
        """
        Returns True if today (UTC time zone) is a public holiday for a given country or False if it is not.
        
        Args:
        - countryCode (str): The code representing one of over a hundred countries supported by the API.
        - utc_offset (int): Integer offset from UTC time zone to adjust for one's own time zone.
        
        Returns:
        - bool: True if today (UTC time zone) is a public holiday for the given country or False if it is not.
        """
        endpoint = f"IsTodayPublicHoliday/{countryCode}?offset={utc_offset}"
        url = self.base_url+endpoint
        response = requests.get(url)
        if response.status_code == 200:
            return True
        elif response.status_code == 204:
            return False
        elif response.status_code == 400:
            return "Validation error"
        elif response.status_code == 404:
            return "Country code is unknown"
            
    def get_public_holdiays_for_next_365(self, countryCode):
        """
        Returns a list of the upcoming public holidays for a given country for the next 365 days.
        
        Args:
        - countryCode (str): The code representing one of over a hundred countries supported by the API.
        
        Returns:
        - list: A list containing the upcoming public holidays for a given country for the next 365 days.
        """
        endpoint = f"NextPublicHolidays/{countryCode}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_public_holidays_worldwide_for_next_7(self):
        """
        Returns a list of all the public holidays worldwide for the next 7 days.
        
        Args:
        - None
        
        Returns:
        - list: A list containing all the upcoming public holidays worldwide for the next 7 days.
        """
        endpoint = "NextPublicHolidaysWorldwide"
        return mr.make_request(self.base_url+endpoint)
     
  
            
    
           
        
    
        
        
        
        