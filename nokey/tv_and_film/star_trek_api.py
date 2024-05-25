import requests_cache
from .. helperFuncs import make_request as mr

class STAPI:
    """
    A class for interacting with the Star Trek API.
    
    Attributes:
    - base_url: The base URL of the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="stapi_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://stapi.co/api/"
        self.about = "STAPI (Star Trek API) is an API for accessing information about all things Star Trek."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Star Trek API.
        
        Args:
        - None
        
        Returns:
        - str: The URL for the API.
        """
        return "https://editor.swagger.io/?url=https://stapi.co/api/v1/rest/common/download/stapi.yaml"
        
    def get_animal_by_id(self, uid):
        """
        Returns information about a Star Trek animal matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the animal.
        
        Returns:
        - dict: A dictionary containing information about the animal.
        """
        endpoint = f"v1/rest/animal?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_animals(self, pageNumber=0, pageSize=50):
        """
        Returns a list of animals of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of animals per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of animals.
        """
        endpoint = f"v1/rest/animal/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_astronomical_object_by_id(self, uid):
        """
        Returns information about a Star Trek astronomical object matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the astronomical object.
        
        Returns:
        - dict: A dictionary containing information about the astronomical object.
        """
        endpoint = f"v2/rest/astronomicalObject?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_astronomical_objects(self, pageNumber=0, pageSize=50):
        """
        Returns a list of astronomical objects of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of objects per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of astronomical objects.
        """
        endpoint = f"v2/rest/astronomicalObject/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_book_by_id(self, uid):
        """
        Returns information about a Star Trek book matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the book.
        
        Returns:
        - dict: A dictionary containing information about the book.
        """
        endpoint = f"v2/rest/book?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_books(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek books of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of books per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of books.
        """
        endpoint = f"v2/rest/book/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_book_collection_by_id(self, uid):
        """
        Returns information about a Star Trek book collection matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the book collection.
        
        Returns:
        - dict: A dictionary containing information about the book collection.
        """
        endpoint = f"v1/rest/bookCollection?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_book_collections(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek book collections of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of book collections per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of book collections.
        """
        endpoint = f"v1/rest/bookCollection/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_book_series_by_id(self, uid):
        """
        Returns information about a Star Trek book series matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the book series.
        
        Returns:
        - dict: A dictionary containing information about the book series.
        """
        endpoint = f"v1/rest/bookSeries?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_book_series(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek book series of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of book series per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of book series.
        """
        endpoint = f"v1/rest/bookSeries/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_character_by_id(self, uid):
        """
        Returns information about a Star Trek character matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the character.
        
        Returns:
        - dict: A dictionary containing information about the character.
        """
        endpoint = f"v1/rest/character?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_characters(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek characters of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of characters per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of characters.
        """
        endpoint = f"v1/rest/character/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_comic_by_id(self, uid):
        """
        Returns information about a Star Trek comic matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the comic.
        
        Returns:
        - dict: A dictionary containing information about the comic.
        """
        endpoint = f"v1/rest/comics?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_comics(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek comics of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of comics per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of comics.
        """
        endpoint = f"v1/rest/comics/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_comic_collection_by_id(self, uid):
        """
        Returns information about a Star Trek comic collection matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the comic collection.
        
        Returns:
        - dict: A dictionary containing information about the comic collection.
        """
        endpoint = f"v1/rest/comicCollection?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_comic_collections(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek comic collections of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of comic collections per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of comic collections.
        """
        endpoint = f"v1/rest/comicCollection/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_comic_series_by_id(self, uid):
        """
        Returns information about a Star Trek comic series matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the comic series.
        
        Returns:
        - dict: A dictionary containing information about the comic series.
        """
        endpoint = f"v1/rest/comicSeries?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_comic_series(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek comic series of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of comic series per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of comic series.
        """
        endpoint = f"v1/rest/comicSeries/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_comic_strip_by_id(self, uid):
        """
        Returns information about a Star Trek comic strip matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the comic strip.
        
        Returns:
        - dict: A dictionary containing information about the comic strip.
        """
        endpoint = f"v1/rest/comicStrip?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_comic_strips(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek comic strips of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of comic strips per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of comic strips.
        """
        endpoint = f"v1/rest/comicStrip/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_company_by_id(self, uid):
        """
        Returns information about a Star Trek company matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the company.
        
        Returns:
        - dict: A dictionary containing information about the company.
        """
        endpoint = f"v2/rest/company?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_companies(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek companies of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of companies per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of companies.
        """
        endpoint = f"v2/rest/company/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_conflict_by_id(self, uid):
        """
        Returns information about a Star Trek conflict matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the conflict.
        
        Returns:
        - dict: A dictionary containing information about the conflict.
        """
        endpoint = f"v2/rest/conflict?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_conflicts(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek conflicts of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of conflicts per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of conflicts.
        """
        endpoint = f"v1/rest/conflict/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_data_version(self):
        """
        Returns the data version of the API.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing the data version of the API.
        """
        endpoint = "v1/rest/common/dataVersion"
        return mr.make_request(self.base_url+endpoint)
        
    def get_element_by_id(self, uid):
        """
        Returns information about a Star Trek element matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the element.
        
        Returns:
        - dict: A dictionary containing information about the element.
        """
        endpoint = f"v2/rest/element?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_elements(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek elements of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of elements per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of elements.
        """
        endpoint = f"v2/rest/element/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_episode_by_id(self, uid):
        """
        Returns information about a Star Trek episode matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the episode.
        
        Returns:
        - dict: A dictionary containing information about the episode.
        """
        endpoint = f"v1/rest/episode?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_episodes(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek episodes of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of eposodes per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of episodes.
        """
        endpoint = f"v1/rest/episode/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_food_by_id(self, uid):
        """
        Returns information about a Star Trek food matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the food.
        
        Returns:
        - dict: A dictionary containing information about the food.
        """
        endpoint = f"v1/rest/food?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_foods(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek foods of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of foods per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of foods.
        """
        endpoint = f"v1/rest/food/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_literature_by_id(self, uid):
        """
        Returns information about Star Trek literature matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the literature.
        
        Returns:
        - dict: A dictionary containing information about the literature.
        """
        endpoint = f"v1/rest/literature?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_literature(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek literature of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of literature per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of literature.
        """
        endpoint = f"v1/rest/literature/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_location_by_id(self, uid):
        """
        Returns information about a Star Trek location matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the location.
        
        Returns:
        - dict: A dictionary containing information about the location.
        """
        endpoint = f"v2/rest/location?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_locations(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek locations of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of locations per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of locations.
        """
        endpoint = f"v2/rest/location/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_magazine_by_id(self, uid):
        """
        Returns information about a Star Trek magazine matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the magazine.
        
        Returns:
        - dict: A dictionary containing information about the magazine.
        """
        endpoint = f"v1/rest/magazine?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_magazines(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek magazines of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of magazines per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of magazines.
        """
        endpoint = f"v1/rest/magazine/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_magazine_series_by_id(self, uid):
        """
        Returns information about a Star Trek magazine series matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the magazine series.
        
        Returns:
        - dict: A dictionary containing information about the magazine series.
        """
        endpoint = f"v1/rest/magazineSeries?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_magazine_series(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek magazine series of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of magazine series per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of magazine series.
        """
        endpoint = f"v1/rest/magazineSeries/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_material_by_id(self, uid):
        """
        Returns information about a Star Trek material matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the material.
        
        Returns:
        - dict: A dictionary containing information about the material.
        """
        endpoint = f"v1/rest/material?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_materials(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek materials of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of materials per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of materials.
        """
        endpoint = f"v1/rest/material/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_medical_condition_by_id(self, uid):
        """
        Returns information about a Star Trek medical condition matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the medical condition.
        
        Returns:
        - dict: A dictionary containing information about the medical condition.
        """
        endpoint = f"v1/rest/medicalCondition?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_medical_conditions(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek medical conditions of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of medical conditions per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of medical conditions.
        """
        endpoint = f"v1/rest/medicalCondition/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_movie_by_id(self, uid):
        """
        Returns information about a Star Trek movie matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the movie.
        
        Returns:
        - dict: A dictionary containing information about the movie.
        """
        endpoint = f"v1/rest/movie?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_movies(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek movies of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of movies per page. Defaults to 50 (although at this time there are only 14 entries).
        
        Returns:
        - dict: A dictionary containing a list of movies.
        """
        endpoint = f"v1/rest/movie/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_occupation_by_id(self, uid):
        """
        Returns information about a Star Trek occupation matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the occupation.
        
        Returns:
        - dict: A dictionary containing information about the occupation.
        """
        endpoint = f"v2/rest/occupation?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_occupations(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek occupations of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of occupations per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of occupations.
        """
        endpoint = f"v2/rest/occupation/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_organization_by_id(self, uid):
        """
        Returns information about a Star Trek organization matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the organization.
        
        Returns:
        - dict: A dictionary containing information about the organization.
        """
        endpoint = f"v1/rest/organization?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_organizations(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek organizations of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of organizations per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of organizations.
        """
        endpoint = f"v1/rest/organization/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_performer_by_id(self, uid):
        """
        Returns information about a Star Trek performer matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the performer.
        
        Returns:
        - dict: A dictionary containing information about the performer.
        """
        endpoint = f"v2/rest/performer?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_performers(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek performers of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of performers per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of performers.
        """
        endpoint = f"v2/rest/performer/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_season_by_id(self, uid):
        """
        Returns information about a Star Trek season matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the season.
        
        Returns:
        - dict: A dictionary containing information about the season.
        """
        endpoint = f"v1/rest/season?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_seasons(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek seasons of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of seasons per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of seasons.
        """
        endpoint = f"v1/rest/season/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_series_by_id(self, uid):
        """
        Returns information about a Star Trek series matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the series.
        
        Returns:
        - dict: A dictionary containing information about the series.
        """
        endpoint = f"v1/rest/series?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_series(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek series of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of series per page. Defaults to 50 (although at this time there are only 12 entries).
        
        Returns:
        - dict: A dictionary containing a list of series.
        """
        endpoint = f"v1/rest/series/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_soundtrack_by_id(self, uid):
        """
        Returns information about a Star Trek soundtrack.matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the soundtrack.
        
        Returns:
        - dict: A dictionary containing information about the soundtrack.
        """
        endpoint = f"v1/rest/soundtrack?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_soundtracks(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek soundtracks of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of soundtracks per page. Defaults to 50 (although at this time there are only 12 entries).
        
        Returns:
        - dict: A dictionary containing a list of soundtracks.
        """
        endpoint = f"v1/rest/soundtrack/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_spacecraft_by_id(self, uid):
        """
        Returns information about a Star Trek spacecraft matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the spacecraft.
        
        Returns:
        - dict: A dictionary containing information about the spacecraft.
        """
        endpoint = f"v2/rest/spacecraft?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_spacecrafts(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek spacecrafts of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of spacecrafts per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of spacecrafts.
        """
        endpoint = f"v2/rest/spacecraft/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_spacecraft_class_by_id(self, uid):
        """
        Returns information about a Star Trek spacecraft class matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the spacecraft class.
        
        Returns:
        - dict: A dictionary containing information about the spacecraft class.
        """
        endpoint = f"v2/rest/spacecraftClass?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_spacecraft_classes(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek spacecraft classes of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of spacecraft classes per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of spacecraft classes.
        """
        endpoint = f"v2/rest/spacecraftClass/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_species_by_id(self, uid):
        """
        Returns information about a Star Trek species matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the species.
        
        Returns:
        - dict: A dictionary containing information about the species.
        """
        endpoint = f"v2/rest/species?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_species(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek species of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of species per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of species.
        """
        endpoint = f"v2/rest/species/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_staff_by_id(self, uid):
        """
        Returns information about a Star Trek staff matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the staff.
        
        Returns:
        - dict: A dictionary containing information about the staff.
        """
        endpoint = f"v2/rest/staff?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_staff(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek staff of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of staff per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of staff.
        """
        endpoint = f"v2/rest/staff/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_technology_by_id(self, uid):
        """
        Returns information about a Star Trek technology matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the technology.
        
        Returns:
        - dict: A dictionary containing information about the technology.
        """
        endpoint = f"v2/rest/technology?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_technologies(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek technologies of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of technologies per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of technologies.
        """
        endpoint = f"v2/rest/technology/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_title_by_id(self, uid):
        """
        Returns information about a Star Trek titles matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the title.
        
        Returns:
        - dict: A dictionary containing information about the title.
        """
        endpoint = f"v2/rest/title?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_titles(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek titles of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of titles per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of titles.
        """
        endpoint = f"v2/rest/title/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_trading_card_by_id(self, uid):
        """
        Returns information about a Star Trek trading card matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the trading card.
        
        Returns:
        - dict: A dictionary containing information about the trading card.
        """
        endpoint = f"v1/rest/tradingCard?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_trading_cards(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek trading cards of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of trading cards per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of trading cards.
        """
        endpoint = f"v1/rest/tradingCard/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_trading_card_deck_by_id(self, uid):
        """
        Returns information about a Star Trek trading card deck matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the trading card deck.
        
        Returns:
        - dict: A dictionary containing information about the trading card deck.
        """
        endpoint = f"v1/rest/tradingCardDeck?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_trading_card_decks(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek trading card decks of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of trading card decks per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of trading card decks.
        """
        endpoint = f"v1/rest/tradingCardDeck/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_trading_card_set_by_id(self, uid):
        """
        Returns information about a Star Trek trading card set matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the trading card set.
        
        Returns:
        - dict: A dictionary containing information about the trading card set.
        """
        endpoint = f"v1/rest/tradingCardSet?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_trading_card_sets(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek trading card sets of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of trading card sets per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of trading card sets.
        """
        endpoint = f"v1/rest/tradingCardSet/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_video_game_by_id(self, uid):
        """
        Returns information about a Star Trek video game matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the video game.
        
        Returns:
        - dict: A dictionary containing information about the video game.
        """
        endpoint = f"v1/rest/videoGame?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_video_games(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek video games of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of video games per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of video games.
        """
        endpoint = f"v1/rest/videoGame/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_video_release_by_id(self, uid):
        """
        Returns information about a Star Trek video release matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the video release.
        
        Returns:
        - dict: A dictionary containing information about the video release.
        """
        endpoint = f"v2/rest/videoRelease?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_video_releases(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek video releases of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of video releases per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of video releases.
        """
        endpoint = f"v2/rest/videoRelease/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_weapon_by_id(self, uid):
        """
        Returns information about a Star Trek weapon matching the unique id.
        
        Args:
        - uid (str): The unique identifier for the weapon.
        
        Returns:
        - dict: A dictionary containing information about the weapon.
        """
        endpoint = f"v2/rest/weapon?uid={uid}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_weapons(self, pageNumber=0, pageSize=50):
        """
        Returns a list of Star Trek weapons of the specified page number and page size.
        
        Args:
        - pageNumber (int): The page number of the list. Defaults to 0, the first page.
        - pageSize (int): The number of weapons per page. Defaults to 50.
        
        Returns:
        - dict: A dictionary containing a list of weapons.
        """
        endpoint = f"v2/rest/weapon/search?pageNumber={pageNumber}&pageSize={pageSize}"
        return mr.make_request(self.base_url+endpoint)
       
        
        
    
       
       
       
       
       
       
       
       
       
       
     
     
     
        
    
    
 
 
 
   
   
   
   
   
   
     
   
   
 
 
 
   
  
   
 
  
   
   
  
    
   
  
  
   
  
   
        