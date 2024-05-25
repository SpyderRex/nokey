import requests_cache
import xmltodict
from .. helperFuncs import make_request as mr

class ITIS:
    """ 
    A class for interacting with the Integrated Taxonomic Integration System API.
    
    Attributes:
    - base_url: The base URL of the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="itis_cache", backend="sqlite", expire_after=3600):
        self.base_url = "http://www.itis.gov/ITISWebService/services/ITISService/"
        self.about = "The ITIS program is driven by a mission: communicate a comprehensive taxonomy of global species that enables biodiversity information to be discovered, indexed, and connected across all human endeavors."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the ITIS API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://www.itis.gov/ws_description.html"
        
    #SEARCH FUNCTIONS
    def search_for_any_match(self, search_key, data_format="json"):
        """
        Returns matches found by comparing the search key to the ITIS common names, scientific names, and TSNs.
        
        Args:
        - search_key (str or int): The name (common or scientific) or Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the search key.
        """
        endpoint = f"searchForAnyMatch?srchKey={search_key}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def search_for_any_match_paged(self, search_key, page_size=50, page_num=1, ascend=True, data_format="json"):
        """
        Returns matches found by comparing the search key to the ITIS common names, scientific names, and TSNs.
        
        Args:
        - search_key (str or int): The name (common or scientific) or Taxonomic Serial Number (TSN).
        - page_size (int): Number of matches returned per page. Defaults to 50.
        - page_num (int): The page number to return (pagination). Defaults to the first page.
        - ascend (boolean): Whether to sort pages in ascending or descending alphabetical order. Default is True.
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
           
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the search key.
        """
        endpoint = f"searchForAnyMatchPaged?srchKey={search_key}&pageSize={page_size}&pageNum={page_num}&ascend={ascend}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_any_match_count(self, search_key, data_format="json"):
        """
        Returns a count of the matches found by comparing the search key to the ITIS common names, scientific names, and TSNs..
        
        Args:
        - search_key (str or int): The name (common or scientific) or Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the count matching the search key.
        """
        endpoint = f"getAnyMatchCount?srchKey={search_key}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def search_by_common_name(self, search_key, data_format="json"):
        """
        Returns matches found by comparing the search key to the ITIS common names.
        
        Args:
        - search_key (str): The common name.
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the search key.
        """
        endpoint = f"searchByCommonName?srchKey={search_key}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def search_by_common_name_begins_with(self, search_key, data_format="json"):
        """
        Return matches found by comparing the search key to the beginning of the ITIS common names.
        
        Args:
        - search_key (str): The beginning of the name to be searched.
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the search key.
        """
        endpoint = f"searchByCommonNameBeginsWith?srchKey={search_key}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def search_by_common_name_ends_with(self, search_key, data_format="json"):
        """
        Return matches found by comparing the search key to the end of the ITIS common names.
        
        Args:
        - search_key (str): The end of the name to be searched.
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the search key.
        """
        endpoint = f"searchByCommonNameEndsWith?srchKey={search_key}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def search_by_scientific_name(self, search_key, data_format="json"):
        """
        Returns matches found by comparing the search key to the ITIS scientific names.
        
        Args:
        - search_key (str): The scientific name.
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the search key.
        """
        endpoint = f"searchByScientificName?srchKey={search_key}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_ITIS_terms(self, search_key, data_format="json"):
        """
        Gets a list of ITIS Terms as used by the Resource Catalog Input Tool from a common or scientific name match, or an empty result set if there is no match.
        
        Args:
        - search_key (str): The common or scientific name.
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the search key.
        """
        endpoint = f"getITISTerms?srchKey={search_key}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_ITIS_terms_from_common_name(self, search_key, data_format="json"):
        """
        Gets a list of ITIS Terms as used by the Resource Catalog Input Tool from a common name match, or an empty result set if there is no match.
        
        Args:
        - search_key (str): The common name.
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the search key.
        """
        endpoint = f"getITISTermsFromCommonName?srchKey={search_key}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_ITIS_terms_from_scientific_name(self, search_key, data_format="json"):
        """
        Gets a list of ITIS Terms as used by the Resource Catalog Input Tool from a scientific name match, or an empty result set if there is no match.
        
        Args:
        - search_key (str): The scientific name.
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the search key.
        """
        endpoint = f"getITISTermsFromScientificName?srchKey={search_key}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_TSNs_by_vernacular_language(self, language, data_format="json"):
        """
        Provide a listing of Taxonomic Serial Numbers (TSNs) with vernaculars entered in the requested language.
        
        Args:
        - language (str): The desired language. Supported values are Afrikaans, Arabic, Australian, Bengali, Chinese, Djuka, Dutch, eng, English, Fijan, French, Galibi, German, Greek, Hausa, Hawaiian, Hindi, Icelandic, Iglulik Inuit, Italian, Japanese, Javanese, Khmer, Korean, Lao, Malagasy, Manyika, Native American, Ndau, Northern Sotho, Portuguese, Romanian, Shona, Spanish, Swati, unspecified, Xhosa, Zulu.
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the language.
        """
        endpoint = f"getTsnByVernacularLanguage?language={language}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
         
    #FUNCTIONS TO RETRIEVE INFORMATION BY TSN
    def get_accepted_names_from_TSN(self, tsn, data_format="json"):
        """
        Returns a list of accepted names for the TSN. This can return more than one result if the TSN is for a synonym.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getAcceptedNamesFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_comment_detail_from_TSN(self, tsn, data_format="json"):
        """
        Returns the list of comments for the TSN. This can return more than result if multiple comments are entered.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getCommentDetailFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_common_names_from_TSN(self, tsn, data_format="json"):
        """
        Returns a list of common names for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getCommonNamesFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_core_metadata_from_TSN(self, tsn, data_format="json"):
        """
        Returns the set of core metadata for the TSN. This contains credibility rating, taxonomic usage, unacceptability reason, coverage, and currency data.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getCoreMetadataFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_coverage_from_TSN(self, tsn, data_format="json"):
        """
        Returns the taxon coverage information for the TSN. This information is  available for Genus and above (rank_id > 190) only.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getCoverageFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_credibility_rating_from_TSN(self, tsn, data_format="json"):
        """
        Returns the credibility rating for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getCredibilityRatingFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_currency_from_TSN(self, tsn, data_format="json"):
        """
        Returns the taxon currency information for the TSN. This information is  available for Genus and above (rank_id > 190) only.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getCurrencyFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_date_data_from_TSN(self, tsn, data_format="json"):
        """
        Returns the initial time stamp and last update date for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getDateDataFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_experts_from_TSN(self, tsn, data_format="json"):
        """
        Returns a list of the expert information for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getExpertsFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_full_record_from_TSN(self, tsn, data_format="json"):
        """
        Returns the full ITIS record for a TSN found by comparing the search key to the TSN field, or an empty result set if there is no match.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getFullRecordFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_geographic_divisions_from_TSN(self, tsn, data_format="json"):
        """
        Returns a list of the geographic divisions for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getGeographicDivisionsFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_global_species_completeness_from_TSN(self, tsn, data_format="json"):
        """
        Returns the taxon completenes rating for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getGlobalSpeciesCompletenessFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_jurisdictional_origin_from_TSN(self, tsn, data_format="json"):
        """
        Returns a list of the jurisdiction and origin values for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getJurisdictionalOriginFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_kingdom_name_from_TSN(self, tsn, data_format="json"):
        """
        Returns the kingdom name for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getKingdomNameFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_other_sources_from_TSN(self, tsn, data_format="json"):
        """
        Returns a list of the other sources used for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getOtherSourcesFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_parent_TSN_from_TSN(self, tsn, data_format="json"):
        """
        Returns the parent TSN for the entered TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getParentTSNFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_publications_from_TSN(self, tsn, data_format="json"):
        """
        Returns a list of the pulications used for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getPublicationsFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_review_year_from_TSN(self, tsn, data_format="json"):
        """
        Returns the review year for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getReviewYearFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_scientific_name_from_TSN(self, tsn, data_format="json"):
        """
        Returns the scientific name for the TSN. Also returns the component parts (names and indicators) of the scientific name.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getScientificNameFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_synonym_names_from_TSN(self, tsn, data_format="json"):
        """
        Returns a list of the synonyms (if any) for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getSynonymNamesFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_taxon_authorship_from_TSN(self, tsn, data_format="json"):
        """
        Returns the author information for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getTaxonAuthorshipFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_taxonomic_rank_name_from_TSN(self, tsn, data_format="json"):
        """
        Returns the kingdom and rank information for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getTaxonomicRankNameFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_taxonomic_usage_from_TSN(self, tsn, data_format="json"):
        """
        Returns the usage information for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getTaxonomicUsageFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_unacceptability_reason_from_TSN(self, tsn, data_format="json"):
        """
        Returns the unacceptability reason, if any, for the TSN.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getUnacceptabilityReasonFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
            
    # HIERARCHY FUNCTIONS
    def get_full_hierarchy_from_TSN(self, tsn, data_format="json"):
        """
        Returns the Taxonomic Hierarchy from the kingdom to the requested scientific name, and the immediate children of the scientific name.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getFullHierarchyFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_hierarchy_down_from_TSN(self, tsn, data_format="json"):
        """
        Returns a list of all the valid/accepted scientific names contained within a particular valid/accepted scientific name and their TSNs, limited to immediate children only. The result set will be found by comparing the search key to the parent TSN field.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getHierarchyDownFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_hierarchy_up_from_TSN(self, tsn, data_format="json"):
        """
        Returns the parent of the TSN (i.e. the parent of the current scientific name in the taxonomic hierarchy) found by comparing the search key to the ITIS TSN field.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getHierarchyUpFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
            
    # LIFE SCIENCE IDENTIFIER (LSID) FUNCTIONS
    def get_full_record_from_LSID(self, tsn, data_format="json"):
        """
        Returns the full ITIS record for the TSN in the LSID, found by comparing the TSN in the search key to the TSN field. Returns an empty result set if there is no match or the TSN is invalid.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getFullRecordFromLSID?lsid=urn:lsid:itis.gov:itis_tsn:{tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_LSID_from_TSN(self, tsn, data_format="json"):
        """
        Gets the unique LSID for the TSN, or an empty result if there is no match.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getLSIDFromTSN?tsn={tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_record_from_LSID(self, tsn, data_format="json"):
        """
        Gets the partial ITIS record for the TSN in the LSID, found by comparing the TSN in the search key to the TSN field. Returns an empty result set if there is no match or the TSN is invalid.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getRecordFromLSID?lsid=urn:lsid:itis.gov:itis_tsn:{tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_TSN_from_LSID(self, tsn, data_format="json"):
        """
        Gets the TSN corresponding to the LSID, or an empty result if there is no match.
        
        Args:
        - tsn (int): The Taxonomic Serial Number (TSN).
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the data matching the TSN.
        """
        endpoint = f"getTSNFromLSID?lsid=urn:lsid:itis.gov:itis_tsn:{tsn}"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
            
    # META-INFORMATION FUNCTIONS
    def get_credibility_ratings(self, data_format="json"):
        """
        Provides a list of all the unique valid credibility rating values contained in the database.
        
        Args:
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the credibility rating values.
        """
        endpoint = "getCredibilityRatings"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_description(self, data_format="json"):
        """
        Provides a description of the web service and the ITIS database.
        
        Args:
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing a description of the ITIS database.
        """
        endpoint = "getDescription"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_geographic_values(self, data_format="json"):
        """
        Provides a list of all the geographic values contained in the database.
        
        Args:
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the geographic values contained in the database.
        """
        endpoint = "getGeographicValues"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_jurisdiction_values(self, data_format="json"):
        """
        Provides a list of all the jurisdiction values contained in the database.
        
        Args:
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the jurisdiction values contained in the database.
        """
        endpoint = "getJurisdictionValues"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_jurisdictional_origin_values(self, data_format="json"):
        """
        Provides a list of all the origin values contained in the database.
        
        Args:
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the origin values contained in the database.
        """
        endpoint = "getJurisdictionalOriginValues"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_kingdom_names(self, data_format="json"):
        """
        Provides a list of all the unique kingdom names contained in the database, their kingdom IDs and their TSNs.
        
        Args:
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the kingdom names contained in the database.
        """
        endpoint = "getKingdomNames"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_last_change_date(self, data_format="json"):
        """
        Provides the date the ITIS database was last updated.
        
        Args:
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing the date the database was last updated.
        """
        endpoint = "getLastChangeDate"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_rank_names(self, data_format="json"):
        """
        Provides a list of all the unique rank names contained in the database and their kingdom and rank ID values.
        
        Args:
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing a list of all the unique rank names contained in the database.
        """
        endpoint = "getRankNames"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
            
    def get_vernacular_languages(self, data_format="json"):
        """
        Provides a list of the unique languages used in the vernacular table.
        
        Args:
        - data_format (str): The desired format for returned data. Defaults to json, but other option is xml.
        
        Returns:
        - dict or string (xml): A dictionary or XML string containing a list of all the unique languages used in the vernacular table.
        """
        endpoint = "getVernacularLanguages"
        data_format = data_format.lower()
        if data_format == "json":
            data = mr.make_request_for_content(self.base_url+endpoint)
            return xmltodict.parse(data)
        elif data_format == "xml":
            return mr.make_request_for_content(self.base_url+endpoint)
        else:
            return "Error: Format must be either json or xml."
          
          
          
          
          
          
          
          
    
          
    
            
            
            
            
            
            
    
           
            
            
       
    
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
          
          
           
            
    
       
       
          
          
          
          
          
            
    
            
    
            
    
         
         
           
         
           
          
          
        
          
          
    
    