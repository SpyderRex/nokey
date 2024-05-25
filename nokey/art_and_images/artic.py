import requests_cache
from .. helperFuncs import make_request as mr
from .. helperFuncs.throttler import throttle_class

@throttle_class(rate_limit=1, period=1)
class Artic:
    """
    A class for interacting with the Art Institute of Chicago API.
    
    Attributes:
    - base_url: The base URL of the API.
    - image_api_url: The base URL for accessing the images in this API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="artic_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://api.artic.edu/api/v1/"
        self.image_api_url ="https://www.artic.edu/iiif/2/"
        self.about = "The Art Institute of Chicago's API provides JSON-formatted data as a REST-style service that allows developers to explore and integrate the museum’s public data into their projects. This API is the same tool that powers our website, our mobile app, and many other technologies in the museum."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Art Institute of Chicago API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://api.artic.edu/docs/"
    
    # Artworks    
    def get_all_artworks(self, page=1, limit=10):
        """
        Returns data about all the artwork at Art Institute of Chicago.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing artwork data.
        """
        endpoint = f"artworks?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artwork_by_id(self, artwork_id):
        """
        Returns data about a specific artwork in the Art Institute of Chicago's database.
        
        Args:
        - artwork_id (int): A unique number identifying the artwork.
        
        Returns:
        - dict: A dictionary containing data about a specific artwork.
        """
        endpoint = f"artworks/{artwork_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artworks_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the artwork contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_artworks_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing artwork data.
        """
        endpoint = f"artworks/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artworks_data_fields(self):
        """
        Returns the list of artwork fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_artworks()["data"][0].keys()
        
    def search_artworks(self, query, page=1, limit=10):
        """
        Returns data about a artwork in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about artwork.
        """
        endpoint = f"artworks/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
    
    # Places    
    def get_all_artists(self, page=1, limit=10):
        """
        Returns data about all the artists in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing artist data.
        """
        endpoint = f"artists?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artist_by_id(self, artist_id):
        """
        Returns data about a specific artist in the Art Institute of Chicago's database.
        
        Args:
        - artist_id (int): A unique number identifying the artist
        
        Returns:
        - dict: A dictionary containing data about a specific artist.
        """
        endpoint = f"artists/{artist_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artists_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the artists contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_artists_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing artist data.
        """
        endpoint = f"artists/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artists_data_fields(self):
        """
        Returns the list of artist fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_artists()["data"][0].keys()
        
    def search_artists(self, query, page=1, limit=10):
        """
        Returns data about artists in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about artists
        """
        endpoint = f"artists/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)        
    
    # Places    
    def get_all_places(self, page=1, limit=10):
        """
        Returns data about all the places in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing places data.
        """
        endpoint = f"places?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_place_by_id(self, place_id):
        """
        Returns data about a specific place in the Art Institute of Chicago's database.
        
        Args:
        - place_id (negative int): A unique (negative) number identifying the place.
        
        Returns:
        - dict: A dictionary containing data about a specific place.
        """
        endpoint = f"places/{place_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_places_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the places contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_places_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing places data.
        """
        endpoint = f"places/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_places_data_fields(self):
        """
        Returns the list of places fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_places()["data"][0].keys()
        
    def search_places(self, query, page=1, limit=10):
        """
        Returns data about places in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about places.
        """
        endpoint = f"places/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Agents
    def get_all_agents(self, page=1, limit=10):
        """
        Returns data about all the agents in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing agents data.
        """
        endpoint = f"agents?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agent_by_id(self, agent_id):
        """
        Returns data about a specific agent in the Art Institute of Chicago's database.
        
        Args:
        - agent_id (int): A unique number identifying the agent.
        
        Returns:
        - dict: A dictionary containing data about a specific agent.
        """
        endpoint = f"agents/{agent_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agents_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the agents contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_agents_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing agents data.
        """
        endpoint = f"agents/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agents_data_fields(self):
        """
        Returns the list of agents fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_agents()["data"][0].keys()
        
    def search_agents(self, query, page=1, limit=10):
        """
        Returns data about agents in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about agents.
        """
        endpoint = f"agents/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Galleries
    def get_all_galleries(self, page=1, limit=10):
        """
        Returns data about all the galleries in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing galleries data.
        """
        endpoint = f"galleries?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_gallery_by_id(self, gallery_id):
        """
        Returns data about a specific gallery in the Art Institute of Chicago's database.
        
        Args:
        - agent_id (int): A unique number identifying the gallery.
        
        Returns:
        - dict: A dictionary containing data about a specific gallery.
        """
        endpoint = f"galleries/{gallery_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_galleries_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the galleries contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_galleries_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing galleries data.
        """
        endpoint = f"galleries/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_galleries_data_fields(self):
        """
        Returns the list of galleries fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_galleries()["data"][0].keys()
        
    def search_galleries(self, query, page=1, limit=10):
        """
        Returns data about galleries in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about galleries.
        """
        endpoint = f"galleries/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Exhibitions
    def get_all_exhibitions(self, page=1, limit=10):
        """
        Returns data about all the exhibitions in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing exhibitions data.
        """
        endpoint = f"exhibitions?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_exhibition_by_id(self, exhibition_id):
        """
        Returns data about a specific exhibition in the Art Institute of Chicago's database.
        
        Args:
        - exhibition_id (int): A unique number identifying the exhibition.
        
        Returns:
        - dict: A dictionary containing data about a specific exhibition.
        """
        endpoint = f"exhibitions/{exhibition_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_exhibitions_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the exhibitions contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_exhibitions_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing exhibitions data.
        """
        endpoint = f"exhibitions/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_exhibitions_data_fields(self):
        """
        Returns the list of exhibitions fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_exhibitions()["data"][0].keys()
        
    def search_exhibitions(self, query, page=1, limit=10):
        """
        Returns data about exhibitions in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about exhibitions.
        """
        endpoint = f"exhibitions/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Agent Types
    def get_all_agent_types(self, page=1, limit=10):
        """
        Returns data about all the agent types in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing agent types data.
        """
        endpoint = f"agent-types?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agent_type_by_id(self, agent_type_id):
        """
        Returns data about a specific agent type in the Art Institute of Chicago's database.
        
        Args:
        - agent_type_id (int): A unique number identifying the agent type.
        
        Returns:
        - dict: A dictionary containing data about a specific agent type.
        """
        endpoint = f"agent-types/{agent_type_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agent_types_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the agent types contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_agent_types_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing agent types data.
        """
        endpoint = f"agent-types/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agent_types_data_fields(self):
        """
        Returns the list of agent types fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_agent_types()["data"][0].keys()
        
    def search_agent_types(self, query, page=1, limit=10):
        """
        Returns data about agent types in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about agent types.
        """
        endpoint = f"agent-types/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Agent Roles
    def get_all_agent_roles(self, page=1, limit=10):
        """
        Returns data about all the agent roles in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing agent roles data.
        """
        endpoint = f"agent-roles?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agent_role_by_id(self, agent_role_id):
        """
        Returns data about a specific agent role in the Art Institute of Chicago's database.
        
        Args:
        - agent_role_id (int): A unique number identifying the agent role.
        
        Returns:
        - dict: A dictionary containing data about a specific agent role.
        """
        endpoint = f"agent-role/{agent_role_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agent_roles_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the agent roles contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_agent_roles_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing agent roles data.
        """
        endpoint = f"agent-roles/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agent_roles_data_fields(self):
        """
        Returns the list of agent roles fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_agent_roles()["data"][0].keys()
        
    def search_agent_roles(self, query, page=1, limit=10):
        """
        Returns data about agent roles in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about agent roles.
        """
        endpoint = f"agent-roles/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Artwork place qualifiers
    def get_all_artwork_place_qualifiers(self, page=1, limit=10):
        """
        Returns data about all the artwork place qualifiers in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing artwork place qualifiers data.
        """
        endpoint = f"artwork-place-qualifiers?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artwork_place_qualifier_by_id(self, artwork_place_qualifier_id):
        """
        Returns data about a specific artwork place qualifier in the Art Institute of Chicago's database.
        
        Args:
        - artwork_place_qualifier_id (int): A unique number identifying the artwork place qualifier.
        
        Returns:
        - dict: A dictionary containing data about a specific artwork place qualifier.
        """
        endpoint = f"artwork-place-qualifier/{artwork_place_qualifier_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artwork_place_qualifiers_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the artwork place qualifiers contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_artwork_place_qualifiers_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing artwork place qualifiers data.
        """
        endpoint = f"artwork-place-qualifiers/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artwork_place_qualifiers_data_fields(self):
        """
        Returns the list of artwork place qualifiers fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_artwork_place_qualifiers()["data"][0].keys()
        
    def search_artwork_place_qualifiers(self, query, page=1, limit=10):
        """
        Returns data about artwork place qualifiers in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about artwork place qualifiers.
        """
        endpoint = f"artwork-place-qualifiers/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Artwork date qualifiers
    def get_all_artwork_date_qualifiers(self, page=1, limit=10):
        """
        Returns data about all the artwork date qualifiers in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing artwork date qualifiers data.
        """
        endpoint = f"artwork-date-qualifiers?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artwork_date_qualifier_by_id(self, artwork_date_qualifier_id):
        """
        Returns data about a specific artwork date qualifier in the Art Institute of Chicago's database.
        
        Args:
        - artwork_date_qualifier_id (int): A unique number identifying the artwork date qualifier.
        
        Returns:
        - dict: A dictionary containing data about a specific artwork date qualifier.
        """
        endpoint = f"artwork-date-qualifier/{artwork_date_qualifier_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artwork_date_qualifiers_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the artwork date qualifiers contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_artwork_date_qualifiers_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing artwork date qualifiers data.
        """
        endpoint = f"artwork-date-qualifiers/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artwork_date_qualifiers_data_fields(self):
        """
        Returns the list of artwork date qualifiers fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_artwork_date_qualifiers()["data"][0].keys()
        
    def search_artwork_date_qualifiers(self, query, page=1, limit=10):
        """
        Returns data about artwork date qualifiers in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about artwork date qualifiers.
        """
        endpoint = f"artwork-date-qualifiers/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Artwork types
    def get_all_artwork_types(self, page=1, limit=10):
        """
        Returns data about all the artwork types in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing artwork type data.
        """
        endpoint = f"artwork-types?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artwork_type_by_id(self, artwork_type_id):
        """
        Returns data about a specific artwork type in the Art Institute of Chicago's database.
        
        Args:
        - artwork_type_id (int): A unique number identifying the artwork type.
        
        Returns:
        - dict: A dictionary containing data about a specific artwork type.
        """
        endpoint = f"artwork-types/{artwork_type_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artwork_types_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the artwork types contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_artwork_types_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing artwork types data.
        """
        endpoint = f"artwork-types/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_artwork_types_data_fields(self):
        """
        Returns the list of artwork types fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_artwork_types()["data"][0].keys()
        
    def search_artwork_types(self, query, page=1, limit=10):
        """
        Returns data about artwork types in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about artwork types.
        """
        endpoint = f"artwork-types/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Category Terms
    def get_all_category_terms(self, page=1, limit=10):
        """
        Returns data about all the category terms in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing category terms.
        """
        endpoint = f"category-terms?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_category_term_by_id(self, category_term_id):
        """
        Returns data about a specific category term in the Art Institute of Chicago's database.
        
        Args:
        - category_term_id (str): A unique id identifying the category term.
        
        Returns:
        - dict: A dictionary containing data about a specific category term.
        """
        endpoint = f"category-terms/{category_term_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_category_terms_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the category terms contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_category_terms_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing category terms data.
        """
        endpoint = f"category-terms/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_category_terms_data_fields(self):
        """
        Returns the list of category terms fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_category_terms()["data"][0].keys()
        
    def search_category_terms(self, query, page=1, limit=10):
        """
        Returns data about category terms in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about category terms.
        """
        endpoint = f"category-terms/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Images
    def get_all_images(self, page=1, limit=10):
        """
        Returns data about all the images in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing image data.
        """
        endpoint = f"images?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_image_by_id(self, image_id):
        """
        Returns data about a specific image in the Art Institute of Chicago's database.
        
        Args:
        - image_id (str): A unique id identifying the image.
        
        Returns:
        - dict: A dictionary containing data about a specific image.
        """
        endpoint = f"images/{image_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_images_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the images contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_images_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing images data.
        """
        endpoint = f"images/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_images_data_fields(self):
        """
        Returns the list of images fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_images()["data"][0].keys()
        
    def search_images(self, query, page=1, limit=10):
        """
        Returns data about images in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about images.
        """
        endpoint = f"images/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Videos
    def get_all_videos(self, page=1, limit=10):
        """
        Returns data about all the videos in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing videos data.
        """
        endpoint = f"videos?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_video_by_id(self, video_id):
        """
        Returns data about a specific video in the Art Institute of Chicago's database.
        
        Args:
        - video_id (str): A unique id identifying the video.
        
        Returns:
        - dict: A dictionary containing data about a specific video.
        """
        endpoint = f"videos/{video_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_videos_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the videos contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_videos_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing videos data.
        """
        endpoint = f"videos/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_videos_data_fields(self):
        """
        Returns the list of videos fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_videos()["data"][0].keys()
        
    def search_videos(self, query, page=1, limit=10):
        """
        Returns data about videos in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about videos.
        """
        endpoint = f"videos/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Sounds
    def get_all_sounds(self, page=1, limit=10):
        """
        Returns data about all the sounds in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing sounds data.
        """
        endpoint = f"sounds?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_sound_by_id(self, sound_id):
        """
        Returns data about a specific sound in the Art Institute of Chicago's database.
        
        Args:
        - sound_id (str): A unique id identifying the sound.
        
        Returns:
        - dict: A dictionary containing data about a specific sound.
        """
        endpoint = f"sounds/{sound_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_sounds_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the sounds contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_sounds_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing sounds data.
        """
        endpoint = f"sounds/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_sounds_data_fields(self):
        """
        Returns the list of sounds fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_sounds()["data"][0].keys()
        
    def search_sounds(self, query, page=1, limit=10):
        """
        Returns data about sounds in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about sounds.
        """
        endpoint = f"sounds/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Texts
    def get_all_texts(self, page=1, limit=10):
        """
        Returns data about all the texts in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing texts data.
        """
        endpoint = f"texts?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_text_by_id(self, text_id):
        """
        Returns data about a specific text in the Art Institute of Chicago's database.
        
        Args:
        - text_id (str): A unique id identifying the text.
        
        Returns:
        - dict: A dictionary containing data about a specific text.
        """
        endpoint = f"texts/{text_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_texts_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the texts contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_texts_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing texts data.
        """
        endpoint = f"texts/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_texts_data_fields(self):
        """
        Returns the list of texts fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_texts()["data"][0].keys()
        
    def search_texts(self, query, page=1, limit=10):
        """
        Returns data about texts in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about texts.
        """
        endpoint = f"texts/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Products
    def get_all_products(self, page=1, limit=10):
        """
        Returns data about all the products in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing products data.
        """
        endpoint = f"products?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_product_by_id(self, product_id):
        """
        Returns data about a specific product in the Art Institute of Chicago's database.
        
        Args:
        - product_id (int): A unique number identifying the product.
        
        Returns:
        - dict: A dictionary containing data about a specific product.
        """
        endpoint = f"products/{product_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_products_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the products contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_products_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing products data.
        """
        endpoint = f"products/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_products_data_fields(self):
        """
        Returns the list of products fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_products()["data"][0].keys()
        
    def search_products(self, query, page=1, limit=10):
        """
        Returns data about products in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about products.
        """
        endpoint = f"products/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Tours
    def get_all_tours(self, page=1, limit=10):
        """
        Returns data about all the tours in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing tours data.
        """
        endpoint = f"tours?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_tour_by_id(self, tour_id):
        """
        Returns data about a specific tour in the Art Institute of Chicago's database.
        
        Args:
        - tour_id (int): A unique number identifying the tour.
        
        Returns:
        - dict: A dictionary containing data about a specific tour.
        """
        endpoint = f"tours/{tour_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_tours_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the tours contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_tours_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing tours data.
        """
        endpoint = f"tours/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_tours_data_fields(self):
        """
        Returns the list of tours fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_tours()["data"][0].keys()
        
    def search_tours(self, query, page=1, limit=10):
        """
        Returns data about tours in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about tours.
        """
        endpoint = f"tours/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Mobile Sounds
    def get_all_mobile_sounds(self, page=1, limit=10):
        """
        Returns data about all the mobile sounds in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing mobile sounds data.
        """
        endpoint = f"mobile-sounds?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_mobile_sound_by_id(self, mobile_sound_id):
        """
        Returns data about a specific mobile sound in the Art Institute of Chicago's database.
        
        Args:
        - mobile_sound_id (int): A unique number identifying the mobile sound.
        
        Returns:
        - dict: A dictionary containing data about a specific mobile sound.
        """
        endpoint = f"mobile-sounds/{mobile_sound_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_mobile_sounds_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the mobile sounds contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_mobile_sounds_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing mobile sounds data.
        """
        endpoint = f"mobile-sounds/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_mobile_sounds_data_fields(self):
        """
        Returns the list of mobile sounds fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields
        """
        return self.get_all_mobile_sounds()["data"][0].keys()
        
    def search_mobile_sounds(self, query, page=1, limit=10):
        """
        Returns data about mobile sounds in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about mobile sounds.
        """
        endpoint = f"mobile-sounds/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Publications 
    def get_all_publications(self, page=1, limit=10):
        """
        Returns data about all the publications in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing publications data.
        """
        endpoint = f"publications?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_publication_by_id(self, publication_id):
        """
        Returns data about a specific publication in the Art Institute of Chicago's database.
        
        Args:
        - publication_id (int): A unique number identifying the publication.
        
        Returns:
        - dict: A dictionary containing data about a specific publication.
        """
        endpoint = f"publications/{publication_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_publications_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the publications contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_publications_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing publications data.
        """
        endpoint = f"publications/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_publications_data_fields(self):
        """
        Returns the list of publications fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields
        """
        return self.get_all_publications()["data"][0].keys()
        
    def search_publications(self, query, page=1, limit=10):
        """
        Returns data about publications in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about publications.
        """
        endpoint = f"publications/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Sections 
    def get_all_sections(self, page=1, limit=10):
        """
        Returns data about all the sections in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing sections data.
        """
        endpoint = f"sections?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_section_by_id(self, section_id):
        """
        Returns data about a specific section in the Art Institute of Chicago's database.
        
        Args:
        - section_id (int): A unique number identifying the publication.
        
        Returns:
        - dict: A dictionary containing data about a specific section.
        """
        endpoint = f"sections/{section_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_sections_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the sections contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_sections_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing sections data.
        """
        endpoint = f"sections/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_sections_data_fields(self):
        """
        Returns the list of sections fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields
        """
        return self.get_all_sections()["data"][0].keys()
        
    def search_sections(self, query, page=1, limit=10):
        """
        Returns data about sections in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about sections.
        """
        endpoint = f"sections/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Sites
    def get_all_sites(self, page=1, limit=10):
        """
        Returns data about all the sites in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing sites data.
        """
        endpoint = f"sites?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_site_by_id(self, site_id):
        """
        Returns data about a specific site in the Art Institute of Chicago's database.
        
        Args:
        - site_id (int): A unique number identifying the site.
        
        Returns:
        - dict: A dictionary containing data about a specific site.
        """
        endpoint = f"sites/{site_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_sites_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the sites contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_sites_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing sites data.
        """
        endpoint = f"sites/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_sites_data_fields(self):
        """
        Returns the list of sites fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields
        """
        return self.get_all_sites()["data"][0].keys()
        
    def search_sites(self, query, page=1, limit=10):
        """
        Returns data about sites in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about sites.
        """
        endpoint = f"sites/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Events
    def get_all_events(self, page=1, limit=10):
        """
        Returns data about all the events in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing events data.
        """
        endpoint = f"events?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_event_by_id(self, event_id):
        """
        Returns data about a specific event in the Art Institute of Chicago's database.
        
        Args:
        - event_id (int): A unique number identifying the event.
        
        Returns:
        - dict: A dictionary containing data about a specific event.
        """
        endpoint = f"event/{event_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_events_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the events contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_events_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing events data.
        """
        endpoint = f"events/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_events_data_fields(self):
        """
        Returns the list of events fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields
        """
        return self.get_all_events()["data"][0].keys()
        
    def search_events(self, query, page=1, limit=10):
        """
        Returns data about events in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about events.
        """
        endpoint = f"events/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Event Occurrences 
    def get_all_event_occurrences(self, page=1, limit=10):
        """
        Returns data about all the event occurrences in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing event occurrences data.
        """
        endpoint = f"event-occurrences?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_event_occurrence_by_id(self, event_occurrence_id):
        """
        Returns data about a specific event occurrence in the Art Institute of Chicago's database.
        
        Args:
        - event_occurrence_id (str): A unique id identifying the event occurrence.
        
        Returns:
        - dict: A dictionary containing data about a specific event occurrence.
        """
        endpoint = f"event-occurrences/{event_occurrence_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_event_occurrences_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the event occurrences contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_events_occurrences_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing event occurrences data.
        """
        endpoint = f"event-occurrences/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_event_occurrences_data_fields(self):
        """
        Returns the list of event occurrences fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields
        """
        return self.get_all_event_occurrences()["data"][0].keys()
        
    def search_event_occurrences(self, query, page=1, limit=10):
        """
        Returns data about event occurrences in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about event occurrences.
        """
        endpoint = f"event-occurrences/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Event Programs
    def get_all_event_programs(self, page=1, limit=10):
        """
        Returns data about all the event programs in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing event programs data.
        """
        endpoint = f"event-programs?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_event_program_by_id(self, event_program_id):
        """
        Returns data about a specific event program in the Art Institute of Chicago's database.
        
        Args:
        - event_program_id (int): A unique number identifying the event program.
        
        Returns:
        - dict: A dictionary containing data about a specific event program.
        """
        endpoint = f"event-programs/{event_program_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_event_programs_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the event programs contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_events_programs_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing event programs data.
        """
        endpoint = f"event-programs/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_event_programs_data_fields(self):
        """
        Returns the list of event programs fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_event_programs()["data"][0].keys()
        
    def search_event_programs(self, query, page=1, limit=10):
        """
        Returns data about event programs in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about event programs.
        """
        endpoint = f"event-programs/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Articles
    def get_all_articles(self, page=1, limit=10):
        """
        Returns data about all the articles in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing articles data.
        """
        endpoint = f"articles?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_article_by_id(self, article_id):
        """
        Returns data about a specific article in the Art Institute of Chicago's database.
        
        Args:
        - article_id (int): A unique number identifying the article.
        
        Returns:
        - dict: A dictionary containing data about a specific article.
        """
        endpoint = f"articles/{article_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_articles_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the articles contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_articles_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing articles data.
        """
        endpoint = f"articles/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_articles_data_fields(self):
        """
        Returns the list of articles fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_articles()["data"][0].keys()
        
    def search_articles(self, query, page=1, limit=10):
        """
        Returns data about articles in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about articles.
        """
        endpoint = f"articles/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Highlights
    def get_all_highlights(self, page=1, limit=10):
        """
        Returns data about all the highlights in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing highlights data.
        """
        endpoint = f"highlights?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_highlight_by_id(self, highlight_id):
        """
        Returns data about a specific highlight in the Art Institute of Chicago's database.
        
        Args:
        - highlight_id (int): A unique number identifying the highlight.
        
        Returns:
        - dict: A dictionary containing data about a specific highlight.
        """
        endpoint = f"highlights/{highlight_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_highlights_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the highlights contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_highlights_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing highlights data.
        """
        endpoint = f"highlights/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_highlights_data_fields(self):
        """
        Returns the list of highlights fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_highlights()["data"][0].keys()
        
    def search_highlights(self, query, page=1, limit=10):
        """
        Returns data about highlights in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about highlights.
        """
        endpoint = f"highlights/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Static Pages
    def get_all_static_pages(self, page=1, limit=10):
        """
        Returns data about all the static pages in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing static pages data.
        """
        endpoint = f"static-pages?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_static_page_by_id(self, static_page_id):
        """
        Returns data about a specific static page in the Art Institute of Chicago's database.
        
        Args:
        - static_page_id (int): A unique number identifying the static page.
        
        Returns:
        - dict: A dictionary containing data about a specific static page.
        """
        endpoint = f"static-pages/{static_page_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_static_pages_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the static pages contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_static_pages_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing static pages data.
        """
        endpoint = f"static-pages/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_static_pages_data_fields(self):
        """
        Returns the list of static pages fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_static_pages()["data"][0].keys()
        
    def search_static_pages(self, query, page=1, limit=10):
        """
        Returns data about static pages in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about static pages.
        """
        endpoint = f"static-pages/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Generic Pages
    def get_all_generic_pages(self, page=1, limit=10):
        """
        Returns data about all the generic pages in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing generic pages data.
        """
        endpoint = f"generic-pages?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_generic_page_by_id(self, generic_page_id):
        """
        Returns data about a specific generic page in the Art Institute of Chicago's database.
        
        Args:
        - generic_page_id (int): A unique number identifying the generic page.
        
        Returns:
        - dict: A dictionary containing data about a specific generic page.
        """
        endpoint = f"generic-pages/{generic_page_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_generic_pages_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the generic pages contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_generic_pages_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing generic pages data.
        """
        endpoint = f"generic-pages/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_generic_pages_data_fields(self):
        """
        Returns the list of generic pages fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_generic_pages()["data"][0].keys()
        
    def search_generic_pages(self, query, page=1, limit=10):
        """
        Returns data about generic pages in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about generic pages.
        """
        endpoint = f"generic-pages/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Press Releases
    def get_all_press_releases(self, page=1, limit=10):
        """
        Returns data about all the press releases in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing press releases data.
        """
        endpoint = f"press-releases?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_press_release_by_id(self, press_release_id):
        """
        Returns data about a specific press release in the Art Institute of Chicago's database.
        
        Args:
        - press_release_id (int): A unique number identifying the press release.
        
        Returns:
        - dict: A dictionary containing data about a specific press release.
        """
        endpoint = f"press-releases/{press_release_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_press_releases_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the press releases contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_press_releases_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing press releases data.
        """
        endpoint = f"press-releases/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_press_releases_data_fields(self):
        """
        Returns the list of press releases fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_press_releases()["data"][0].keys()
        
    def search_press_releases(self, query, page=1, limit=10):
        """
        Returns data about press releases in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about press releases.
        """
        endpoint = f"press-releases/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Educator Resources
    def get_all_educator_resources(self, page=1, limit=10):
        """
        Returns data about all the educator resources in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing educator resources data.
        """
        endpoint = f"educator-resources?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_educator_resource_by_id(self, educator_resource_id):
        """
        Returns data about a specific educator resource in the Art Institute of Chicago's database.
        
        Args:
        - educator_resource_id (int): A unique number identifying the educator resource.
        
        Returns:
        - dict: A dictionary containing data about a specific educator resource.
        """
        endpoint = f"educator-resources/{educator_resource_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_educator_resources_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the educator resources contained in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_educator_resources_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing educator resources data.
        """
        endpoint = f"educator-resources/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_educator_resources_data_fields(self):
        """
        Returns the list of educator resources fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_educator_resources()["data"][0].keys()
        
    def search_educator_resources(self, query, page=1, limit=10):
        """
        Returns data about educator resources in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about educator resources.
        """
        endpoint = f"educator-resources/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Digital Catalogs
    def get_all_digital_catalogs(self, page=1, limit=10):
        """
        Returns data about all the digital catalogs in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing digital catalogs data.
        """
        endpoint = f"digital-catalogs?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_digital_catalog_by_id(self, digital_catalog_id):
        """
        Returns data about a specific digital catalog in the Art Institute of Chicago's database.
        
        Args:
        - digital_catalog_id (int): A unique number identifying the digital catalog.
        
        Returns:
        - dict: A dictionary containing data about a specific digital catalog.
        """
        endpoint = f"digital-catalogs/{digital_catalog_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_digital_catalogs_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the digital catalogs in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_digital_catalogs_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing digital catalogs data.
        """
        endpoint = f"digital-catalogs/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_digital_catalogs_data_fields(self):
        """
        Returns the list of digital catalogs fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_digital_catalogs()["data"][0].keys()
        
    def search_digital_catalogs(self, query, page=1, limit=10):
        """
        Returns data about digital catalogs in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about digital catalogs.
        """
        endpoint = f"digital-catalogs/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Digital Publication Sections
    def get_all_digital_publication_sections(self, page=1, limit=10):
        """
        Returns data about all the digital publication sections in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing digital publication sections data.
        """
        endpoint = f"digital-publication-sections?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_digital_publication_section_by_id(self, digital_publication_section_id):
        """
        Returns data about a specific digital publication section in the Art Institute of Chicago's database.
        
        Args:
        - digital_publication_section_id (int): A unique number identifying the digital publication section.
        
        Returns:
        - dict: A dictionary containing data about a specific digital publication section.
        """
        endpoint = f"digital-publication-sections/{digital_publication_section_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_digital_publication_sections_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the digital publication sections in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_digital_publication_sections_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing digital publication sections data.
        """
        endpoint = f"digital-publication-sections/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_digital_publication_sections_data_fields(self):
        """
        Returns the list of digital publication sections fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_digital_publication_sections()["data"][0].keys()
        
    def search_digital_publication_sections(self, query, page=1, limit=10):
        """
        Returns data about digital publication sections in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about digital publication sections.
        """
        endpoint = f"digital-publication-sections/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    # Printed Catalogs
    def get_all_printed_catalogs(self, page=1, limit=10):
        """
        Returns data about all the printed catalogs in Art Institute of Chicago database.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing printed catalogs data.
        """
        endpoint = f"printed-catalogs?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_printed_catalog_by_id(self, printed_catalog_id):
        """
        Returns data about a specific printed catalog in the Art Institute of Chicago's database.
        
        Args:
        - printed_catalog_id (int): A unique number identifying the printed catalog.
        
        Returns:
        - dict: A dictionary containing data about a specific printed catalog.
        """
        endpoint = f"printed-catalogs/{printed_catalog_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_printed_catalogs_by_fields(self, fields, page=1, limit=10):
        """
        Returns data about all the printed catalogs in the ARTIC database, but only by the specified fields.
        
        Args:
        - field (str): A comma separated, no spaced string of field names. For retrieving only certain fields. Call get_printed_catalogs_data_fields function to get the available fields.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Default is 10.
        
        Returns:
        - dict: A dictionary containing printed catalogs data.
        """
        endpoint = f"printed-catalogs/?fields={fields}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_printed_catalogs_data_fields(self):
        """
        Returns the list of printed catalogs fields (dictionary keys) used in the ARTIC database.
        
        Args:
        - None
        
        Returns:
        - object: A dict_keys object containing a list of the fields.
        """
        return self.get_all_printed_catalogs()["data"][0].keys()
        
    def search_printed_catalogs(self, query, page=1, limit=10):
        """
        Returns data about printed catalogs in the Art Institute of Chicago's database matching the specified query term and field values.
        
        Args:
        - query (str): A search term.
        
        Returns:
        - dict: A dictionary containing data about printed catalogs.
        """
        endpoint = f"printed-catalogs/search?q={query}&page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    #Download Images
    def download_image(self, image_id):
        """
        Downloads a jpg of the image matching the id.
        
        Args:
        - image_id (str): The unique identifier for the image. These can be obtained from both the images and exhibitions endpoints of the Artic API.
        
        Returns:
        - image, str: Downloads an image and returns a string confirming the download.
        """
        endpoint = f"{image_id}/full/843,/0/default.jpg"
        image_bin = mr.make_request_for_content(self.image_api_url+endpoint)
        with open(image_id+".jpg", "wb") as f:
            f.write(image_bin)
        return f"Image with id {image_id} downloaded"
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
  
    
  
    
  
    
      
  
      
  
    
 
     
  
  
  
   
   
   
        
    
 
        
   
        
    