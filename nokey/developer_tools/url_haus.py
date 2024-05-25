import os
import requests
import requests_cache
from .. helperFuncs import make_request as mr


class URLHaus:
    """
    A class to interact with the URLHaus API.
    
    Attributes:
    - base_url: The base URL of the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="urlhaus_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://urlhaus-api.abuse.ch/v1/"
        self.about = "URLhaus is a project operated by abuse.ch. The purpose of the project is to collect, track and share malware URLs, helping network administrators and security analysts to protect their network and customers from cyber threats."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the URLHaus API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://urlhaus-api.abuse.ch/"
        
    def get_recent_urls(self, limit=None):
        """
        Returns a list of recent URLs added to URLHaus.
        
        Args:
        - limit (int): Optional limit of URLs returned. Defaults to None.
        
        Returns:
        - dict: A dictionary containing a list of recent URLs added to URLHaus.
        """
        if limit is not None:
            endpoint = f"urls/recent/limit/{limit}"
        else:
            endpoint = "urls/recent"
        return mr.make_request(self.base_url+endpoint)
        
    def get_recent_payloads(self, limit=None):
        """
        Returns a list of recent payloads seen by URLHaus.
        
        Args:
        - limit (int): Optional limit of payloads returned. Defaults to None.
        
        Returns:
        - dict: A dictionary containing a list of recent payloads seen by URLHaus.
        """
        if limit is not None:
            endpoint = f"payloads/recent/limit/{limit}"
        else:
            endpoint = "payloads/recent"
        return mr.make_request(self.base_url+endpoint)
        
    def get_info_about_url(self, url):
        """
        Returns any information URLHaus may have about a specific URL.
        
        Args:
        - url (str): The URL in question.
        
        Returns:
        - dict: A dictionary containing information about a specific URL.
        """
        payload = {"url": f"{url}"}
        endpoint = "url/"
        response = requests.post(self.base_url+endpoint, payload)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
            
    def get_info_about_url_by_id(self, urlID):
        """
        Returns any information URLHaus may have about a specific URL.
        
        Args:
        - urlID (int): The id of the URL in question.
        
        Returns:
        - dict: A dictionary containing information about a specific URL.
        """
        payload = {"urlid": f"{urlID}"}
        endpoint = "urlid/"
        response = requests.post(self.base_url+endpoint, payload)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
            
    def get_info_about_host(self, host):
        """
        Returns any information URLHaus may have about a specific host.
        
        Args:
        - host (str): The IPv4 address, domain name, or hostname in question.
        
        Returns:
        - dict: A dictionary containing information about a specific host.
        """
        payload = {"host": f"{host}"}
        endpoint = "host/"
        response = requests.post(self.base_url+endpoint, payload)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
            
    def get_info_about_payload(self, p_load):
        """
        Returns any information URLHaus has about a specific payload (malware sample).
        
        Args:
        - p_load (str): The MD5 hash or SHA256 hash of the payload (malware sample).
        
        Returns:
        - dict: A dictionary containing information about a specific payload.
        """
        payload = {"payload": f"{p_load}"}
        endpoint = "payload/"
        response = requests.post(self.base_url+endpoint, payload)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
            
    def get_info_about_tag(self, tag):
        """
        Returns any information URLHaus has about a specific tag.
        
        Args:
        - tag (str): The tag to query.
        
        Returns:
        - dict: A dictionary containing information about a specific tag.
        """
        payload = {"tag": f"{tag}"}
        endpoint = "tag/"
        response = requests.post(self.base_url+endpoint, payload)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
            
    def get_info_about_signature(self, signature):
        """
        Returns any information URLHaus has about a specific signature.
        
        Args:
        - signature (str): The signature to query.
        
        Returns:
        - dict: A dictionary containing information about a specific signature.
        """
        payload = {"signature": f"{signature}"}
        endpoint = "signature/"
        response = requests.post(self.base_url+endpoint, payload)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
            
    def download_malware_sample(self, sha256):
        """
        Downloads a zip file containing the malware sample (payload).
    
        Args:
        - base_url (str): The base URL of the API.
        - sha256 (str): The SHA256 hash identifying the malware sample (payload) to be downloaded.
    
        Returns:
        - str: Path to the downloaded ZIP file if successful, error message otherwise.
        """
        # Define the endpoint and construct the URL
        endpoint = f"download/{sha256}"
        url = self.base_url + endpoint

        # Send the GET request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Check if the response contains a ZIP file
            if response.headers.get('content-disposition'):
                # Extract the filename from the content-disposition header
                filename = response.headers['content-disposition'].split('=')[1]
                # Get the current directory
                current_directory = os.getcwd()
                # Define the path to save the ZIP file
                zip_path = os.path.join(current_directory, filename)
                # Save the content to the ZIP file
                with open(zip_path, 'wb') as f:
                    f.write(response.content)
                return zip_path
            else:
                return "Error: Response does not contain a ZIP file."
        elif response.status_code == 404:
            return "Error: Malware sample not found."
        else:
            return f"Error: {response.status_code}"      
     
     
     
     
       
        
    
    