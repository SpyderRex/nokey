from .. helperFuncs import make_request as mr

class FreeDictionary:
    """
    A class to interact with the Free Dictionary API.
    
    Attributes:
    - base_url: The base URL of the Free Dictionary API.
    - about: A short description of the API.
    """
    def __init__(self):
        self.base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        self.about = "The Free Dictionary API is a powerful tool that allows you to access the vast array of dictionary data."
        
    def get_docs_url(self):
        """
        Returns the URL for the Free Dictionary API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for thre API documentation.
        """
        return "https://dictionaryapi.dev/"
        
    def look_up_word(self, word):
        """
        Returns the definition and other information of a word.
        
        Args:
        - word (str): The word to be looked up.
        
        Returns:
        - dict: A dictionary containing the definition of a word and other related information.
        """
        endpoint = f"{word}"
        return mr.make_request(self.base_url+endpoint)