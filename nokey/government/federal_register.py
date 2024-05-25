import requests_cache
from .. helperFuncs import make_request as mr

class FederalRegister:
    """
    A class for interacting with the Federal Register API.
    
    Attributes:
    base_url: The base URL of the API.
    about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="federal_register_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://www.federalregister.gov/api/v1/"
        self.about = "FederalRegister.gov provides multiple public API endpoints. These can be used to access information in the Federal Register, the daily journal of the US government."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Federal Register API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://www.federalregister.gov/developers/documentation/api/v1"
        
    def get_fed_reg_document(self, document_num):
        """
        Returns a Federal Register document of the given number.
        
        Args:
        - document_num (str): The unique number for the document.
        
        Returns:
        - dict: A dictionary containing the document matching the given number.
        """
        endpoint = f"documents/{document_num}.json"
        return mr.make_request(self.base_url+endpoint)
        
    def get_multiple_fed_reg_documents(self, document_nums):
        """
        Returns multiple Federal Register documents of the given numbers.
        
        Args:
        - document_nums (str): A string of unspaced, comma-separated document numbers.
        
        Returns:
        - dict: A dictionary containing the documents matching the given numbers.
        """
        endpoint = f"documents/{document_nums}.json"
        return mr.make_request(self.base_url+endpoint)
        
    def search_all_documents(self, search_term, per_page=20, doc_type=None):
        """
        Returns the Federal Register documents published since 1994 matching the given parameters.
        
        Args:
        - search_term (str): The term by which to search the documents.
        - per_page (int): The number of documents to return at once; default is 20; 1000 maximum.
        - doc_type (str): Additional optional search by document type. Supported values are rule (final rule), prorule (proposed rule), notice (notice), and presdocu (presidential document)
        
        Returns:
        - dict: A dictionary containing the documents published since 1994 matching the given values.
        """
        if doc_type is not None:
            endpoint = f"documents.json?per_page={per_page}&conditions[term]={search_term}&conditions[type][]={doc_type.upper()}"
            return mr.make_request(self.base_url+endpoint)
        else:            
            endpoint = f"documents.json?per_page={per_page}&conditions[term]={search_term}"
            return mr.make_request(self.base_url+endpoint)
        
    def get_document_counts_by_facet(self, facet, search_term=None, doc_type=None):
        """
        Returns counts of matching Federal Register documents grouped by a facet.
        
        Args:
        - facet (str): The facet by which to group the documents. Supported values are daily, weekly, monthly, quarterly, yearly, agency, topic, section, type, and subtype.
        - search_term (str): Option search query term. Defaults to None.
        - doc_type (str): Additional optional search by document type. Supported values are rule (final rule), prorule (proposed rule), notice (notice), and presdocu (presidential document)
        
        Returns:
        - dict: Returns a dictionary of document counts for the given parameters.
        """
        if search_term is not None and doc_type is None:
            endpoint = f"documents/facets/{facet}?conditions[term]={search_term}"
            return mr.make_request(self.base_url+endpoint)
        elif doc_type is not None and search_term is None:
            endpoint = f"documents/facets/{facet}?conditions[type][]={doc_type.upper()}"
            return mr.make_request(self.base_url+endpoint)
        else:
            endpoint = f"documents/facets/{facet}"
            return mr.make_request(self.base_url+endpoint)
            
    def get_document_toc_by_date(self, pub_date):
        """
        Returns the document table of contents based on print edition.
        
        Args:
        - pub_date (str): The exact publication date (YYYY-MM-DD).
        
        Returns:
        - dict: A dictionary containing the document table of contents that matches the given date.
        """
        endpoint = f"issues/{pub_date}.json"
        return mr.make_request(self.base_url+endpoint)
        
    def get_public_inspection_document(self, document_num):
        """
        Returns a single public inspection document matching the given number.
        
        Args:
        - document_num (str): The number matching the public inspection document.
        
        Returns:
        - dict: A dictionary containing a single public inspection document matching the given number.
        """
        endpoint = f"public-inspection-documents/{document_num}.json"
        return mr.make_request(self.base_url+endpoint)
        
    def get_multiple_public_inspection_documents(self, document_nums):
        """
        Returns the public inspection documents matching the given numbers.
        
        Args:
        - document_nums (str): The numbers matching the public inspection documents, separated by commas, no spaces.
        
        Returns:
        - dict: A dictionary containing the public inspection documents matching the given numbers.
        """
        endpoint = f"public-inspection-documents/{document_nums}.json"
        return mr.make_request(self.base_url+endpoint)
        
    def get_current_public_inspection_documents(self):
        """
        Returns all the public inspection documents that are currently on public inspection.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing all the public inspection documents that are currently on public inspection.
        """
        endpoint = "public-inspection-documents/current.json"
        return mr.make_request(self.base_url+endpoint)
        
    def search_all_public_inspection_documents(self, pub_date, per_page=20, search_term=None, doc_type=None):
        """
        Returns the Federal Register documents published since 1994 matching the given parameters.
        
        Args:
        - pub_date (str): Public inspection issue date (YYYY-MM-DD).
        - per_page (int): The number of documents to return at once; default is 20; 1000 maximum.
        - search_term (str): The term by which to search the documents.
        - doc_type (str): Additional optional search by document type. Supported values are rule (final rule), prorule (proposed rule), notice (notice), and presdocu (presidential document)
        
        Returns:
        - dict: A dictionary containing the documents published since 1994 matching the given values.
        """
        if search_term is not None and doc_type is None:
            endpoint = f"public-inspection-documents.json?per_page={per_page}&conditions[available_on]={pub_date}&conditions[term]={search_term}"
            return mr.make_request(self.base_url+endpoint)
        elif doc_type is not None and search_term is None:
            endpoint = f"public-inspection-documents.json?per_page={per_page}&conditions[available_on]={pub_date}&conditions[type][]={doc_type.upper()}"
            return mr.make_request(self.base_url+endpoint)
        elif search_term is not None and doc_type is not None:
            endpoint = f"public-inspection-documents.json?per_page={per_page}&conditions[available_on]={pub_date}&conditions[term]={search_term}&conditions[type][]={doc_type.upper()}"
            print(self.base_url+endpoint)
            return mr.make_request(self.base_url+endpoint)
        else:            
            endpoint = f"public-inspection-documents.json?per_page={per_page}&conditions[available_on]={pub_date}"
            return mr.make_request(self.base_url+endpoint)
            
    def get_agencies_details(self):
        """
        Returns all agency details.
        
        Args:
        - None
        
        Returns:
        - dict: A dictionary containing all agency details.
        """
        endpoint = "agencies"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agency_by_slug(self, slug):
        """
        Returns a particular agency's details.
        
        Args:
        - slug (str): The Federal Register slug for the agency. See Federal Register API docs for extensive list of possible values.
        
        Returns:
        - dict: A dictionary containing a particular agency's details.
        """
        endpoint = f"agencies/{slug}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_image_variants_by_id(self, image_id):
        """
        Returns the available image variants and their metadata for a single image identifier.
        
        Args:
        - image_id (str): The Federal Register image identifier.
        
        Returns:
        - dict: A dictionary containing the available image variants and their metadata for a single image identifier.
        """
        endpoint = f"images/{image_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_suggested_searches_by_section(self, section):
        """
        Returns all suggested searches or limit by FederalRegister.gov section.
        
        Args:
        - section (str): The Federal Register slug for the section. Supported values are business-and-industry, environment, health-and-public-welfare, money, science-and-technology, and world.
        
        Returns:
        - dict: A dictionary containing all the suggested searches or limit by Federal.Register.gov section.
        """
        endpoint = f"suggested_searches?conditions[sections]={section}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_suggested_search_by_slug(self, slug):
        """
        Returns a particular suggested search.
        
        Args:
        - slug (str): The Federal Register slug for the suggested search. See Federal Register API docs for extensive list of possible values.
        
        Returns:
        - dict: A dictionary containing a particular suggested search.
        """
        endpoint = f"suggested_searches/{slug}"
        return mr.make_request(self.base_url+endpoint)
 
  
   
   
        
        
 
 
 
 
        
    
 
       