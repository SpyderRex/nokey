import requests_cache
from .. helperFuncs import make_request as mr

class OpenTriviaDB:
    """
    A class for interacting with the Open Trivia Database API.
    
    Attributes:
    - base_url: The base URL of the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="open_trivia_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://opentdb.com/api.php?"
        self.about = "The Open Trivia Database provides a completely free JSON API to retrieve trivia questions for use in programming projects."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Open Trivia Database API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://opentdb.com/api_config.php"
        
    def get_random_trivia_questions(self, amount):
        """
        Returns the specified amount of random trivia questions of various difficulties and subjects, and the answers to those questions.
        
        Args:
        - amount (int): The number of trivia desired.
        
        Returns:
        - dict: A dictionary containing the specified amount of trivia questions along with relevant data and the answers.
        """
        endpoint = f"amount={amount}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_specified_trivia_questions(self, amount, category=None, difficulty=None, q_type=None):
        """
        Returns the specified amount of trivial questions matching the given parameters, along with relevant data and answers to the questions.
        
        Args:
        - amount (int): The number of trivia questions to return.
        - category (int): The category of trivia questions desired. Defaults to None, in which case any categories will be returned.
        - difficulty (str): The difficulty level of the trivia questions. Defaults to None, in which case each question can be any difficulty level. Supported values are easy, medium, and hard.
        - q_type (str): The type of questions. Defaults to None, in which case the types are random. Supported values are boolean (True or False) and multiple (Multiple Choice).
        """
        category_dict = {"general knowledge": 9, 
                         "books": 10,
                         "film": 11,
                         "music": 12,
                         "musicals and theatres": 13,
                         "television": 14,
                         "video games": 15,
                         "board games": 16,
                         "science and nature": 17,
                         "computers": 18,
                         "mathematics": 19,
                         "mythology": 20,
                         "sports": 21,
                         "geography": 22,
                         "history": 23,
                         "politics": 24,
                         "art": 25,
                         "celebrities": 26,
                         "animals": 27,
                         "vehicles": 28,
                         "comics": 29,
                         "gadgets": 30,
                         "japanese anime and manga": 31,
                         "cartoon and animations": 32
        }
        # returns any difficulty of any type of a specific amount and category
        if category is not None and difficulty is None and q_type is None:
            endpoint = f"amount={amount}&category={category_dict[category.lower()]}"
            return mr.make_request(self.base_url+endpoint)
            
        # returns any category and any type of a specific amount and difficulty 
        elif difficulty is not None and category is None and q_type is None:
            endpoint = f"amount={amount}&difficulty={difficulty.lower()}"
            return mr.make_request(self.base_url+endpoint)
            
        # returns any category and any difficulty of a specific amount and question type
        elif q_type is not None and category is None and difficulty is None:
            endpoint = f"amount={amount}&type={q_type.lower()}"
            return mr.make_request(self.base_url+endpoint)
            
        # returns any question type of a specific amount, category, and difficulty.
        elif category is not None and difficulty is not None and q_type is None:
            endpoint = f"amount={amount}&category={category_dict[category.lower()]}&difficulty={difficulty.lower()}"
            return mr.make_request(self.base_url+endpoint)
            
        # returns any category of a specific amount, difficulty, and question type.
        elif difficulty is not None and q_type is not None and category is None:
            endpoint = f"amount={amount}&difficulty={difficulty.lower()}&type={q_type.lower()}"
            return mr.make_request(self.base_url+endpoint)
            
        # returns any difficulty of a specific amount, category, and question type
        elif category is not None and q_type is not None and difficulty is None:
            endpoint = f"amount={amount}&category={category_dict[category.lower()]}&type={q_type.lower()}"
            return mr.make_request(self.base_url+endpoint)
            
        # returns random questions of a given amount (same as get_random_trivia_questions).
        else:
            return self.get_random_trivia_questions(amount=amount)       
                       