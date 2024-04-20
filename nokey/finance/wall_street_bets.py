from .. helperFuncs import make_request as mr


class WallstreetBets:
    """
    A class to interact with the Wallstreet Bets API.
    
    Attributes:
    - base_url: The base URL of the Wallstreet Bets API.
    - about: A short description of the API.
    """
    def __init__(self):
        self.base_url = "https://tradestie.com/api/v1/apps/reddit"
        self.about = "This API gets the top 50 stocks discussed on the Reddit subreddit, Wallstreetbets"

    def get_docs_url(self):
        """
        Returns the URL for the Wallstreet Bets API documentation.
        
        Args:
        - None
        
        Returns:
        -string: The URL for the API docs.
        """
        return "https://tradestie.com/apps/reddit/api/"       
    
    def get_stock_sentiment_from_reddit(self):
        """
        Returns top 50 stocks discussed on Reddit subeddit - Wallstreetbets.

        Args:
        - None

        Returns:
        - list: List of dictionaries containing information about subreddit comments of top 50 stocks.
        """
        endpoint = None
        return mr.make_request(self.base_url)
    