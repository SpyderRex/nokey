import requests_cache
from .. helperFuncs import make_request as mr

class Gutendex:
    """
    A class for interacting with the Gutendex API.
    
    Attributes:
    base_url: The base URL for the API.
    about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="gutendex_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://gutendex.com/books/"
        self.about = "Gutendex is a JSON web API for Project Gutenberg ebook metadata."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Gutendex API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://gutendex.com/"
        
    def get_books(self, page=1, sort="popular", language="en"):
        """
        Returns a list of book metadata contained in the API.
        
        Args:
        - page (int): The page of the book list. Defaults to the first page.
        - sort (str): Sort option for the book metadata. The default is popular, based on number of downloads. Other supported values are ascending and descending.
        - language (str): The language in which the books are written. Defaults to en (English). Can take multiple comma separated (non-spaced) values.
       
        Returns:
        - dict: A dictionary containing the book metadata for the given page.
        """
        endpoint = f"?page={page}&sort={sort}&languages={language}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_book_by_id(self, book_id):
        """
        Returns metadata for a single book matching the given id.
        
        Args:
        - book_id (int): A unique integer identifying the book in the API database.
        
        Returns:
        - dict: A dictionary containing metadata for a single book.
        """
        endpoint = f"{book_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_books_by_ids(self, book_ids):
        """
        Returns metadata for a single book matching the given id.
        
        Args:
        - book_ids (str): Comma separated (no spaces) integers, written as a string, identifying the book in the API database.
        
        Returns:
        - dict: A dictionary containing metadata for a single book.
        """
        endpoint = f"?ids={book_ids}"
        return mr.make_request(self.base_url+endpoint)
        
    def search_books_by_author_and_title(self, author, title, sort="popular", language="en"):
        """
        Returns metadata on books from the given author and/or a give title.
        
        Args:
        - author (str): Any part of the author's name.
        - title (str): Any part of the book's title.
        - sort (str): Parameter by which to sort the data. Default is popular, and other supported values are ascending and descending.
        - language (str): The language in which the books are written. Defaults to en (English). Can take multiple comma separated (non-spaced) values.
        
        Returns:
        - dict: A dictionary containing metadata on books from the given author and/or given title. 
        """
        endpoint = f"?search={author}%20{title}&sort={sort}&languages={language}"
        print(self.base_url+endpoint)
        return mr.make_request(self.base_url+endpoint)
        
    def search_books_by_topic(self, topic, sort="popular", language="en"):
        """
        Returns metadata on books matching the given topic.
        
        Args:
        - topic (str): The topic to search.
        - sort (str): Parameter by which to sort the data. Default is popular, and other supported values are ascending and descending.
        - language (str): The language in which the books are written. Defaults to en (English). Can take multiple comma separated (non-spaced) values.
        
        Returns:
        - dict: A dictionary containing metadata for books matching the given topic.
        """
        endpoint = f"?topic={topic}&sort={sort}&languages={language}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_authors_within_date_range(self, author_year_start, author_year_end, sort="popular", language="en"):
        """
        Returns authors and metadata for their books within the specified year range.
        
        Args:
        - author_year_start (int): The year marking the beginning of range. Can be negative (for BC era) or positive.
        - author_year_end (int): The year marking the end of range. Can be negative (for BC era) or positive.
        - sort (str): Parameter by which to sort the data. Default is popular, and other supported values are ascending and descending.
        - language (str): The language in which the books are written. Defaults to en (English). Can take multiple comma separated (non-spaced) values.
        
        Returns:
        - dict: A dictionary containing a list of books whose authors lived within the specified range.
        """
        endpoint = f"?author_year_start={author_year_start}&author_year_end={author_year_end}&sort={sort}&languages={language}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_authors_before_specified_year(self, author_year_end, sort="popular", language="en"):
        """
        Returns authors and metadata for their books existing before the specified year.
        
        Args:
        - author_year_end (int): The year before which the author was alive. Can be negative (for BC era) or positive.
        - sort (str): Parameter by which to sort the data. Default is popular, and other supported values are ascending and descending.
        - language (str): The language in which the books are written. Defaults to en (English). Can take multiple comma separated (non-spaced) values.
        
        Returns:
        - dict: Returns a dictionary containing metadata for books by authors who were alive before the specified year.
        """
        endpoint = f"?author_year_end={author_year_end}&sort={sort}&languages={language}"
        return mr.make_request(self.base_url+endpoint)