import requests_cache
from .. helperFuncs import make_request as mr

class SpaceflightNews:
    
    """
    A class to interact with the Spaceflight News API.
    
    Attributes:
    - base_url: The base URL of the Spaceflight News API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="spaceflight_news_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://api.spaceflightnewsapi.net/v4/"
        self.about = "The Spaceflight News API (SNAPI) is a product by The Space Devs (TSD). It's the most complete and up-to-date spaceflight news API currently available."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the url for the Spaceflight News API documentation.
        
        Args:
        - None
        
        Returns:
        - string: URL for API documentation.
        """
        return "https://api.spaceflightnewsapi.net/v4/docs"
        
    def get_articles(self, limit=10, offset=10, search=None, summary_contains=None, title_contains=None):
        """
        Returns a list of spaceflight articles fitting the given parameters.
        
        Args:
        - limit (int): Number of results to return per page. Defaults to 10.
        - offset (int): The initial index from which to return the results. Defaults to 10.
        - search (str): Search for documents with a specific phrase in the title or summary. Defaults to None.
        - summary_contains (str): Search for all documents with a specific phrase in the summary. Defaults to None.
        - title_contains (str): Search for all documents with a specific phrase in the title. Defaults to None.
        
        Returns:
        - dict: List of spaceflight articles matching the given parameters.
        """
        if search is not None and summary_contains is not None and title_contains is not None:
            endpoint = f"articles?limit={limit}&offset={offset}&search={search}&summary_contains={summary_contains}&title_contains={title_contains}"
        elif search is not None and summary_contains is not None:
            endpoint = f"articles?limit={limit}&offset={offset}&search={search}&summary_contains={summary_contains}"
        elif search is not None and title_contains is not None:
            endpoint = f"articles?limit={limit}&offset={offset}&search={search}&title_contains={title_contains}"
        elif summary_contains is not None and title_contains is not None:
            endpoint = f"articles?limit={limit}&offset={offset}&summary_contains={summary_contains}&title_contains={title_contains}"
        elif search is not None:
            endpoint = f"articles?limit={limit}&offset={offset}&search={search}"
        elif summary_contains is not None:
            endpoint = f"articles?limit={limit}&offset={offset}&summary_contains={summary_contains}"
        elif title_contains is not None:
            endpoint = f"articles?limit={limit}&offset={offset}&title_contains={title_contains}"
        else:
            endpoint = "articles"
        
        return mr.make_request(self.base_url + endpoint)
        
    def get_article_by_id(self, ID):
        """
        Returns a specific article.
        
        Args:
        - ID (int): A unique integer value identifying this article.
        
        Returns:
        - dict: A dictionary containing the article.
        """
        endpoint = f"articles/{ID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_blogs(self, limit=10, offset=10, search=None, summary_contains=None, title_contains=None):
        """
        Returns a list of spaceflight blogs fitting the given parameters.
        
        Args:
        - limit (int): Number of results to return per page. Defaults to 10.
        - offset (int): The initial index from which to return the results. Defaults to 10.
        - search (str): Search for documents with a specific phrase in the title or summary. Defaults to None.
        - summary_contains (str): Search for all documents with a specific phrase in the summary. Defaults to None.
        - title_contains (str): Search for all documents with a specific phrase in the title. Defaults to None.
        
        Returns:
        - dict: List of spaceflight blogs matching the given parameters.
        """
        if search is not None and summary_contains is not None and title_contains is not None:
            endpoint = f"blogs?limit={limit}&offset={offset}&search={search}&summary_contains={summary_contains}&title_contains={title_contains}"
        elif search is not None and summary_contains is not None:
            endpoint = f"blogs?limit={limit}&offset={offset}&search={search}&summary_contains={summary_contains}"
        elif search is not None and title_contains is not None:
            endpoint = f"blogs?limit={limit}&offset={offset}&search={search}&title_contains={title_contains}"
        elif summary_contains is not None and title_contains is not None:
            endpoint = f"blogs?limit={limit}&offset={offset}&summary_contains={summary_contains}&title_contains={title_contains}"
        elif search is not None:
            endpoint = f"blogs?limit={limit}&offset={offset}&search={search}"
        elif summary_contains is not None:
            endpoint = f"blogs?limit={limit}&offset={offset}&summary_contains={summary_contains}"
        elif title_contains is not None:
            endpoint = f"blogs?limit={limit}&offset={offset}&title_contains={title_contains}"
        else:
            endpoint = "blogs"
        
        return mr.make_request(self.base_url + endpoint)
        
    def get_blog_by_id(self, ID):
        """
        Returns a specific blog.
        
        Args:
        - ID (int): A unique integer value identifying this blog.
        
        Returns:
        - dict: A dictionary containing the blog.
        """
        endpoint = f"blogs/{ID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_info(self):
        """
        Returns information containing API version and news sites featured.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing the version number and a list of features news sites.
        """
        endpoint = "info"
        return mr.make_request(self.base_url+endpoint)
        
    def get_reports(self, limit=10, offset=10, search=None, summary_contains=None, title_contains=None):
        """
        Returns a list of spaceflight reports fitting the given parameters.
        
        Args:
        - limit (int): Number of results to return per page. Defaults to 10.
        - offset (int): The initial index from which to return the results. Defaults to 10.
        - search (str): Search for documents with a specific phrase in the title or summary. Defaults to None.
        - summary_contains (str): Search for all documents with a specific phrase in the summary. Defaults to None.
        - title_contains (str): Search for all documents with a specific phrase in the title. Defaults to None.
        
        Returns:
        - dict: List of spaceflight reports matching the given parameters.
        """
        if search is not None and summary_contains is not None and title_contains is not None:
            endpoint = f"reports?limit={limit}&offset={offset}&search={search}&summary_contains={summary_contains}&title_contains={title_contains}"
        elif search is not None and summary_contains is not None:
            endpoint = f"reports?limit={limit}&offset={offset}&search={search}&summary_contains={summary_contains}"
        elif search is not None and title_contains is not None:
            endpoint = f"reports?limit={limit}&offset={offset}&search={search}&title_contains={title_contains}"
        elif summary_contains is not None and title_contains is not None:
            endpoint = f"reports?limit={limit}&offset={offset}&summary_contains={summary_contains}&title_contains={title_contains}"
        elif search is not None:
            endpoint = f"reports?limit={limit}&offset={offset}&search={search}"
        elif summary_contains is not None:
            endpoint = f"reports?limit={limit}&offset={offset}&summary_contains={summary_contains}"
        elif title_contains is not None:
            endpoint = f"reports?limit={limit}&offset={offset}&title_contains={title_contains}"
        else:
            endpoint = "reports"
        
        return mr.make_request(self.base_url + endpoint)
        
    def get_report_by_id(self, ID):
        """
        Returns a specific report.
        
        Args:
        - ID (int): A unique integer value identifying this report.
        
        Returns:
        - dict: A dictionary containing the report.
        """
        endpoint = f"reports/{ID}"
        return mr.make_request(self.base_url+endpoint)
     
    
   
      
        
