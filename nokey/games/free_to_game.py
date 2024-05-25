import requests_cache
from .. helperFuncs import make_request as mr

class FreeToGame:
    """
    Class to interact with the Free To Game API.
    
    Attributes:
    - base_url: The base URL of the Free To Game API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="freetogame_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://www.freetogame.com/api/"
        self.about = "The Free To Game API is a way to access programmatically the best free-to-play games and free MMO games."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Free To Game API documentation.
        
        Args:
        - None
        
        Returns:
        -string: The URL for the API docs.
        """
        return "https://www.freetogame.com/api-doc"
        
    def get_all_live_games(self, sort_by=None):
        """
        Returns the live games listed in the API.
        
        Args:
        - sort_by (str): Optional parameter by which to sort games if desired. Defaults to None, but supported values are release-date, popularity, alphabetical or relevance.
        
        Returns:
        - dict: A dictionary containing all the live games listed in the API.
        """
        if sort_by is not None:
            endpoint = f"games?sort-by={sort_by}"
        else:
            endpoint = "games"
        return mr.make_request(self.base_url+endpoint)
        
    def get_games_by_platform(self, platform, sort_by=None):
        """
        Returns a list of free games by platform.
        
        Args:
        - platform (str): The platform on which the game is played. Supported values are pc, browser, or all.
        - sort_by (str): Optional parameter by which to sort games if desired. Defaults to None, but supported values are release-date, popularity, alphabetical or relevance.
        
        Returns:
        - dict: A dictionary containing the free games played on the given platform.
        """
        if sort_by is not None:
            endpoint = f"games?platform={platform}&sort-by={sort_by}"
        else:
            endpoint = f"games?platform={platform}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_games_by_category(self, category, sort_by=None):
        """
        Returns a list of free games by category.
        
        Args:
        - category (str): The category of the game. Supported values are mmorpg, shooter, strategy, moba, racing, sports, social, sandbox, open-world, survival, pvp, pve, pixel, voxel, zombie, turn-based, first-person, third-Person, top-down, tank, space, sailing, side-scroller, superhero, permadeath, card, battle-royale, mmo, mmofps, mmotps, 3d, 2d, anime, fantasy, sci-fi, fighting, action-rpg, action, military, martial-arts, flight, low-spec, tower-defense, horror, mmorts.
        - sort_by (str): Optional parameter by which to sort games if desired. Defaults to None, but supported values are release-date, popularity, alphabetical or relevance.
        
        Returns:
        - dict: A dictionary containing the free games matching the given category.
        """
        if sort_by is not None:
            endpoint = f"games?category={category}&sort-by={sort_by}"
        else:
            endpoint = f"games?category={category}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_games_by_platform_and_category(self, platform, category, sort_by=None):
        """
        Returns a list of free games by category.
        
        Args:
        - platform (str): The platform on which the game is played. Supported values are pc, browser, or all.
        - category (str): The category of the game. Supported values are mmorpg, shooter, strategy, moba, racing, sports, social, sandbox, open-world, survival, pvp, pve, pixel, voxel, zombie, turn-based, first-person, third-Person, top-down, tank, space, sailing, side-scroller, superhero, permadeath, card, battle-royale, mmo, mmofps, mmotps, 3d, 2d, anime, fantasy, sci-fi, fighting, action-rpg, action, military, martial-arts, flight, low-spec, tower-defense, horror, mmorts.
        - sort_by (str): Optional parameter by which to sort games if desired. Defaults to None, but supported values are release-date, popularity, alphabetical or relevance.
        
        Returns:
        - dict: A dictionary containing the free games matching the given category.
        """
        if sort_by is not None:
            endpoint = f"games?platform={platform}&category={category}&sort-by={sort_by}"
        else:
            endpoint = f"games?platform={platform}&category={category}"
        return mr.make_request(self.base_url+endpoint)
        
    def filter_games(self, tag, platform="all", sort_by=None):
        """
        Returns a list of free games by category.
        
        Args:
        - tag (str): The filter tags, representing the categories of the filtered games, period delimited, no spaces. Supported values are mmorpg, shooter, strategy, moba, racing, sports, social, sandbox, open-world, survival, pvp, pve, pixel, voxel, zombie, turn-based, first-person, third-Person, top-down, tank, space, sailing, side-scroller, superhero, permadeath, card, battle-royale, mmo, mmofps, mmotps, 3d, 2d, anime, fantasy, sci-fi, fighting, action-rpg, action, military, martial-arts, flight, low-spec, tower-defense, horror, mmorts.
        - platform (str): Optional parameter representing the platform on which the games are played. Default is all, but other supported values are browser and pc.
        - sort_by (str): Optional parameter by which to sort games if desired. Defaults to None, but supported values are release-date, popularity, alphabetical or relevance.
        
        Returns:
        - dict: A dictionary containing the free games matching the given category.
        """
        if sort_by is not None:
            endpoint = f"filter?tag={tag}&platform={platform}&sort-by={sort_by}"
        else:
            endpoint = f"filter?tag={tag}&platform={platform}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_game_by_id(self, gameID):
        """
        Returns information for a single game matching the id.
        
        Args:
        - gameID (int): A number representing the unique id of the game as listed in the API.
        
        Returns:
        - dict: A dictionary containing information for the game matching the given id.
        """
        endpoint = f"game?id={gameID}"
        return mr.make_request(self.base_url+endpoint)
     
     
       
       
        
        