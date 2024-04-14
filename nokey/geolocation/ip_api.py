from .. helperFuncs import make_request as mr


class IP_API:
    """
    A class to interact with the IP API.
    
    Attributes:
    - base_url: The base URL of IP API.
    """
    def __init__(self):
        self.base_url = "http://ip-api.com/json/" 
        
    def get_docs_url(self):
        """
        Returns URL for API docs.
        
        Args:
        - None
        
        Returns:
        - string: URL for API documentation.
        """
        return "https://ip-api.com/docs"
    
    def get_location_info_by_ip_address(self, ip):
        """
        Returns geolocation info (country, state, coordinates, etc.) by IP address.

        Args:
        - ip (str): IPv4/IPv6 address or domain name.

        Returns:
        - dict: Location information based on given IP address or domain name.
        """
        endpoint = f"{ip}"
        return mr.make_request(self.base_url+endpoint)
    