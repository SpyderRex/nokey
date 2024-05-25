import requests_cache
import datetime as dt
from .. helperFuncs import make_request as mr 

current = dt.datetime.now().year

class USAspending:
    """
    A class for interacting with the USA Spending API.
    
    Attributes:
    - base_url: The base URL for the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="usa_spending_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://api.usaspending.gov/api/v2/"
        self.about = "USAspending is the official open data source of federal spending information, including information about federal awards such as contracts, grants, and loans."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the USAspending API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://api.usaspending.gov/docs/"
        
    def get_agency_overview_info(self, toptier_agency_code, fiscal_year=current):
        """
        Returns agency overview information for USAspending.gov's Agency Details page for agencies that have ever awarded.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        
        Returns:
        - dict: A dictionary containing the agency overview information.
        """
        endpoint = f"agency/{toptier_agency_code}?fiscal_year={fiscal_year}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agency_summary_info(self, toptier_agency_code, fiscal_year=current, agency_type="awarding"):
        """
        Returns agency summary information, specifically the number of transactions and award obligations for the sub agency section of USAspending.gov's Agency Details page.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - agency_type (str): Optional. Determines if the data being returned is derived from the awarding agency or the funding agency. Defaults to awarding, but other option is funding.
        
        Returns:
        - dict: A dictionary containing the agency summary information.
        """
        endpoint = f"agency/{toptier_agency_code}/awards?fiscal_year={fiscal_year}&agency_type={agency_type}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_new_awards_count_for_agency(self, toptier_agency_code, fiscal_year=current, agency_type="awarding"):
        """
        Returns a count of New Awards for the agency in a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - agency_type (str): Optional. Determines if the data being returned is derived from the awarding agency or the funding agency. Defaults to awarding, but other option is funding.
        
        Returns:
        - dict: A dictionary containing the count.
        """
        endpoint = f"agency/{toptier_agency_code}/awards/new/count?fiscal_year={fiscal_year}&agency_type={agency_type}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_awards_type_count(self, group="all", fiscal_year=current, order="desc", limit=1, page=1):
        """
        Returns a count of Awards types for agencies in a single fiscal year.
        
        Args:
        - group (str): Optional parameter. Use cfo to get results where CFO designated agencies are returned. Otherwise the default is all.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - order (str): Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order (default).
        - limit (int): The number of items to return. Default is 1.
        - page (int): Pagination parameter. Default is 1.
        
        Returns:
        - dict: A dictionary containing the count.
        """
        endpoint = f"agency/awards/count?group={group}&fiscal_year={fiscal_year}&order={order}&limit={limit}&page={page}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_budget_functions_for_agency(self, toptier_agency_code, fiscal_year=current, Filter=None, order="desc", limit=10, page=1):
        """
        Returns a list of Budget Functions and Budget Subfunctions for the agency in a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - Filter (str): Optional. This will filter the Budget Function by their name to those matching the text.
        - order (str): Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order (default).
        - limit (int): Optional parameter to limit number of items. Default is 10.
        - page (int): Pagination parameter. Default is 1.
        
        Returns:
        - dict: A dictionary containing a list of Budget Functions and Subfunctions.
        """
        if Filter is not None:
            endpoint = f"agency/{toptier_agency_code}/budget_function?fiscal_year={fiscal_year}&filter={Filter}&order={order}&limit={limit}&page={page}"
            return mr.make_request(self.base_url+endpoint)
        else:
            endpoint = f"agency/{toptier_agency_code}/budget_function?fiscal_year={fiscal_year}&order={order}&limit={limit}&page={page}"
            return mr.make_request(self.base_url+endpoint)
        
    def get_budget_function_count_for_agency(self, toptier_agency_code, fiscal_year=current):
        """
        Returns the count of Budget Functions for the agency in a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        
        Returns:
        - dict: A dictionary containing the count.
        """
        endpoint = f"agency/{toptier_agency_code}/budget_function/count?fiscal_year={fiscal_year}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_budgetary_resources_for_agency(self, toptier_agency_code):
        """
        Returns budgetary resources and obligations for the agency and fiscal year requested.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        
        Returns:
        - dict: A dictionary containing a list of budgetary resources and obligations.
        """
        endpoint = f"agency/{toptier_agency_code}/budgetary_resources"
        return mr.make_request(self.base_url+endpoint)
        
    def get_federal_accounts_for_agency(self, toptier_agency_code, fiscal_year=current, Filter=None, order="desc", limit=10, page=1):
        """
        Returns a list of Federal Accounts and Treasury Accounts for the agency in a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - Filter (str): Optional. This will filter the Budget Function by their name to those matching the text.
        - order (str): Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order (default).
        - limit (int): Optional parameter to limit number of items. Default is 10.
        - page (int): Optional pagination parameter. Default is 1.
        
        Returns:
        - dict: A dictionary containing a list of Federal Accounts and Treasury Accounts.
        """
        if Filter is not None:
            endpoint = f"agency/{toptier_agency_code}/federal_account?fiscal_year={fiscal_year}&filter={Filter}&order={order}&limit={limit}&page={page}"
            return mr.make_request(self.base_url+endpoint)
        else:
            endpoint = f"agency/{toptier_agency_code}/federal_account?fiscal_year={fiscal_year}&order={order}&limit={limit}&page={page}"
            return mr.make_request(self.base_url+endpoint)
             
    def get_federal_accounts_count_for_agency(self, toptier_agency_code, fiscal_year=current):
        """
        Returns the count of Federal Accounts and Treasury Accounts for the agency in a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        
        Returns:
        - dict: A dictionary containing the count of Federal Accounts and Treasury Accounts.
        """
        endpoint = f"agency/{toptier_agency_code}/federal_account/count?fiscal_year={fiscal_year}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_object_classes_for_agency(self, toptier_agency_code, fiscal_year=current, Filter=None, order="desc", limit=10, page=1):
        """
        Returns a list of Object Classes for the agency in a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - Filter (str): Optional. This will filter the Budget Function by their name to those matching the text.
        - order (str): Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order (default).
        - limit (int): Optional parameter to limit number of items. Default is 10.
        - page (int): Optional pagination parameter. Default is 1.
        
        Returns:
        - dict: A dictionary containing a list of Objects Classes.
        """
        if Filter is not None:
            endpoint = f"agency/{toptier_agency_code}/object_class?fiscal_year={fiscal_year}&filter={Filter}&order={order}&limit={limit}&page={page}"
            return mr.make_request(self.base_url+endpoint)
        else:
            endpoint = f"agency/{toptier_agency_code}/object_class?fiscal_year={fiscal_year}&order={order}&limit={limit}&page={page}"
            return mr.make_request(self.base_url+endpoint)
               
    def get_object_classes_count_for_agency(self, toptier_agency_code, fiscal_year=current):
        """
        Returns the count of Object Classes for the agency in a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        
        Returns:
        - dict: A dictionary containing the count of Object Classes.
        """
        endpoint = f"agency/{toptier_agency_code}/object_class/count?fiscal_year={fiscal_year}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_obligations_by_award_category_for_agency(self, toptier_agency_code, fiscal_year=current):
        """
        Returns a breakdown of obligations by award category within a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        
        Returns:
        - dict: A dictionary containing a breakdown of obligations by award category.
        """
        endpoint = f"agency/{toptier_agency_code}/obligations_by_award_category?fiscal_year={fiscal_year}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_program_activity_for_agency(self, toptier_agency_code, fiscal_year=current, Filter=None, order="desc", limit=10, page=1):
        """
        Returns a list of Program Activity categories for the agency in a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - Filter (str): Optional. This will filter the Budget Function by their name to those matching the text.
        - order (str): Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order (default).
        - limit (int): Optional parameter to limit number of items. Default is 10.
        - page (int): Optional pagination parameter. Default is 1.
        
        Returns:
        - dict: A dictionary containing a list of Program Activity categories.
        """
        if Filter is not None:
            endpoint = f"agency/{toptier_agency_code}/program_activity?fiscal_year={fiscal_year}&filter={Filter}&order={order}&limit={limit}&page={page}"
            return mr.make_request(self.base_url+endpoint)
        else:
            endpoint = f"agency/{toptier_agency_code}/program_activity?fiscal_year={fiscal_year}&order={order}&limit={limit}&page={page}"
            return mr.make_request(self.base_url+endpoint)
              
    def get_program_activity_count_for_agency(self, toptier_agency_code, fiscal_year=current):
        """
        Returns the count of Program Activity categories for the agency in a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        
        Returns:
        - dict: A dictionary containing the count of Program Activity categories.
        """
        endpoint = f"agency/{toptier_agency_code}/program_activity/count?fiscal_year={fiscal_year}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_sub_agencies_for_agency(self, toptier_agency_code, fiscal_year=current, agency_type="awarding", order="desc", limit=10, page=1):
        """
        Returns a list of sub-agencies and offices with obligated amounts, transaction counts and new award counts for the agency in a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - agency_type (str): Optional. Determines if the data being returned is derived from the awarding agency or the funding agency. Defaults to awarding, but other option is funding.
        - order (str): Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order (default).
        - limit (int): Optional parameter to limit number of items. Default is 10.
        - page (int): Optional pagination parameter. Default is 1.
        
        Returns:
        - dict: A dictionary containing a list of sub-agencies and offices.
        """
        endpoint = f"agency/{toptier_agency_code}/sub_agency?fiscal_year={fiscal_year}&agency_type={agency_type}&order={order}&limit={limit}&page={page}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_sub_agency_count_for_agency(self, toptier_agency_code, fiscal_year=current, agency_type="awarding"):
        """
        Returns the number of sub-agencies and offices for the agency in a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - agency_type (str): Optional. Determines if the data being returned is derived from the awarding agency or the funding agency. Defaults to awarding, but other option is funding.
        
        Returns:
        - dict: A dictionary containing a number of sub-agencies and offices.
        """
        endpoint = f"agency/{toptier_agency_code}/sub_agency/count?fiscal_year={fiscal_year}&agency_type={agency_type}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_federal_accounts_by_bureau_for_agency(self, toptier_agency_code, bureau_slug, fiscal_year=current, agency_type="awarding", order="desc", limit=10, page=1):
        """
        Returns a list of federal_accounts by bureau for the agency in a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - bureau_slug (str): The slug for the bureau.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - agency_type (str): Optional. Determines if the data being returned is derived from the awarding agency or the funding agency. Defaults to awarding, but other option is funding.
        - order (str): Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order (default).
        - limit (int): Optional parameter to limit number of items. Default is 10.
        - page (int): Optional pagination parameter. Default is 1.
        
        Returns:
        - dict: A dictionary containing a list of federal accounts by bureau.
        """
        endpoint = f"agency/{toptier_agency_code}/sub_components/{bureau_slug}?fiscal_year={fiscal_year}&agency_type={agency_type}&order={order}&limit={limit}&page={page}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_subcomponents_for_agency(self, toptier_agency_code, fiscal_year=current, agency_type="awarding", order="desc", limit=10, page=1):
        """
        Returns a list of Sub-Components in the Agency's appropriations for a single fiscal year.
        
        Args:
        - toptier_agency_code (str): A numerical code (in string form, due to the use of leading zeros) identifying the agency.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - agency_type (str): Optional. Determines if the data being returned is derived from the awarding agency or the funding agency. Defaults to awarding, but other option is funding.
        - order (str): Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order (default).
        - limit (int): Optional parameter to limit number of items. Default is 10.
        - page (int): Optional pagination parameter. Default is 1.
        
        Returns:
        - dict: A dictionary containing a list of Sub-Components.
        """
        endpoint = f"agency/{toptier_agency_code}/sub_components?fiscal_year={fiscal_year}&agency_type={agency_type}&order={order}&limit={limit}&page={page}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_object_classes_for_tas(self, tas, fiscal_year=current, Filter=None, order="desc", limit=10, page=1):
        """
        Returns a list of Object Classes for the specified Treasury Account Symbol (tas).
        
        Args:
        - tas (str): The treasury account symbol (tas) of a treasury account. This endpoint supports TAS codes with 0 or 1 slashes in the code.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - Filter (str): Optional. This will filter the Budget Function by their name to those matching the text.
        - order (str): Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order (default).
        - limit (int): Optional parameter to limit number of items. Default is 10.
        - page (int): Optional pagination parameter. Default is 1.
        
        Returns:
        - dict: A dictionary containing a list of Object Classes.
        """
        if Filter is not None:
            endpoint = f"agency/treasury_account/{tas}/object_class?fiscal_year={fiscal_year}&filter={Filter}&order={order}&limit={limit}&page={page}"
            return mr.make_request(self.base_url+endpoint)
        else:
            endpoint = f"agency/treasury_account/{tas}/object_class?fiscal_year={fiscal_year}&order={order}&limit={limit}&page={page}"
            return mr.make_request(self.base_url+endpoint)
    
        
    def get_program_activities_for_tas(self, tas, fiscal_year=current, Filter=None, order="desc", limit=10, page=1):
        """
        Returns a list of Program Activities for the specified Treasury Account Symbol (tas).
        
        Args:
        - tas (str): The treasury account symbol (tas) of a treasury account. This endpoint supports TAS codes with 0 or 1 slashes in the code.
        - fiscal_year (int): The fiscal year. Optional parameter, defaults to the current year.
        - Filter (str): Optional. This will filter the Budget Function by their name to those matching the text.
        - order (str): Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order (default).
        - limit (int): Optional parameter to limit number of items. Default is 10.
        - page (int): Optional pagination parameter. Default is 1.
        
        Returns:
        - dict: A dictionary containing a list of Program Activities.
        """
        if Filter is not None:
            endpoint = f"agency/treasury_account/{tas}/program_activity?fiscal_year={fiscal_year}&filter={Filter}&order={order}&limit={limit}&page={page}"
            return mr.make_request(self.base_url+endpoint)
        else:
            endpoint = f"agency/treasury_account/{tas}/program_activity?fiscal_year={fiscal_year}&order={order}&limit={limit}&page={page}"
            return mr.make_request(self.base_url+endpoint)
            
       
    ### Autocomplete functions       
    def tas_autocomplete_a(self, Filter, limit=10):
        """
        Returns the list of potential Availability Type Codes narrowed by other components supplied in the Treasury Account filter.
        
        Args:
        - Filter (dict): The component filters to be used in the data. Each component listed may be omitted, null, or a string value. If omitted, no filtering will be performed on that component. If null, the filter will include account numbers missing that component. If a string, the filter will perform an exact match on account numbers where that component matches the string provided. Possible values are ata (optional, string, nullable) Allocation Transfer Agency Identifier (3 characters). TAS only; aid (optional, string, nullable) Agency Identifier (3 characters); bpoa (optional, string, nullable) Beginning Period of Availability (4 characters). TAS only; epoa (optional, string, nullable) Ending Period of Availability (4 characters). TAS only; a (optional, string, nullable) Availability Type Code (1 character). Will either be 'X' or null. TAS only; main (optional, string, nullable) Main Account Code (4 characters); and sub (optional, string, nullable) Sub Account Code (3 characters). TAS only.
        - limit (int): Optional. Maximum number of results to return. Default is 10.
        
        Returns:
        - dict: A dictionary containing list of potential Availability Type Codes.
        """
        data = {"filters": Filter, "limit": limit}
        endpoint = "autocomplete/accounts/a"
        return mr.make_request_with_post_and_data(self.base_url+endpoint, data=data)
        
    def tas_autocomplete_aid(self, Filter, limit=10):
        """
        Returns the list of potential Agency Identifiers narrowed by other components supplied in the Treasury Account or Federal Account filter.
        
        Args:
        - Filter (dict): The component filters to be used in the data. Each component listed may be omitted, null, or a string value. If omitted, no filtering will be performed on that component. If null, the filter will include account numbers missing that component. If a string, the filter will perform an exact match on account numbers where that component matches the string provided. Possible values are ata (optional, string, nullable) Allocation Transfer Agency Identifier (3 characters). TAS only; aid (optional, string, nullable) Agency Identifier (3 characters); bpoa (optional, string, nullable) Beginning Period of Availability (4 characters). TAS only; epoa (optional, string, nullable) Ending Period of Availability (4 characters). TAS only; a (optional, string, nullable) Availability Type Code (1 character). Will either be 'X' or null. TAS only; main (optional, string, nullable) Main Account Code (4 characters); and sub (optional, string, nullable) Sub Account Code (3 characters). TAS only.
        - limit (int): Optional. Maximum number of results to return. Default is 10.
        
        Returns:
        - dict: A dictionary containing list of potential Agency Identifiers.
        """
        data = {"filters": Filter, "limit": limit}
        endpoint = "autocomplete/accounts/aid"
        return mr.make_request_with_post_and_data(self.base_url+endpoint, data=data)
        
    def tas_autocomplete_ata(self, Filter, limit=10):
        """
        Returns the list of potential Allocation Transfer Agency Identifiers narrowed by other components supplied in the Treasury Account filter.
        
        Args:
        - Filter (dict): The component filters to be used in the data. Each component listed may be omitted, null, or a string value. If omitted, no filtering will be performed on that component. If null, the filter will include account numbers missing that component. If a string, the filter will perform an exact match on account numbers where that component matches the string provided. Possible values are ata (optional, string, nullable) Allocation Transfer Agency Identifier (3 characters). TAS only; aid (optional, string, nullable) Agency Identifier (3 characters); bpoa (optional, string, nullable) Beginning Period of Availability (4 characters). TAS only; epoa (optional, string, nullable) Ending Period of Availability (4 characters). TAS only; a (optional, string, nullable) Availability Type Code (1 character). Will either be 'X' or null. TAS only; main (optional, string, nullable) Main Account Code (4 characters); and sub (optional, string, nullable) Sub Account Code (3 characters). TAS only.
        - limit (int): Optional. Maximum number of results to return. Default is 10.
        
        Returns:
        - dict: A dictionary containing list of potential Transfer Agency Identifiers.
        """
        data = {"filters": Filter, "limit": limit}
        endpoint = "autocomplete/accounts/ata"
        return mr.make_request_with_post_and_data(self.base_url+endpoint, data=data)
        
    def tas_autocomplete_bpoa(self, Filter, limit=10):
        """
        Returns the list of potential Beginning Period of Availabilities narrowed by other components supplied in the Treasury Account filter.
        
        Args:
        - Filter (dict): The component filters to be used in the data. Each component listed may be omitted, null, or a string value. If omitted, no filtering will be performed on that component. If null, the filter will include account numbers missing that component. If a string, the filter will perform an exact match on account numbers where that component matches the string provided. Possible values are ata (optional, string, nullable) Allocation Transfer Agency Identifier (3 characters). TAS only; aid (optional, string, nullable) Agency Identifier (3 characters); bpoa (optional, string, nullable) Beginning Period of Availability (4 characters). TAS only; epoa (optional, string, nullable) Ending Period of Availability (4 characters). TAS only; a (optional, string, nullable) Availability Type Code (1 character). Will either be 'X' or null. TAS only; main (optional, string, nullable) Main Account Code (4 characters); and sub (optional, string, nullable) Sub Account Code (3 characters). TAS only.
        - limit (int): Optional. Maximum number of results to return. Default is 10.
        
        Returns:
        - dict: A dictionary containing list of potential Beginning Period of Availabilities.
        """
        data = {"filters": Filter, "limit": limit}
        endpoint = "autocomplete/accounts/bpoa"
        return mr.make_request_with_post_and_data(self.base_url+endpoint, data=data)
        
    def tas_autocomplete_epoa(self, Filter, limit=10):
        """
        Returns the list of potential Ending Period of Availabilities narrowed by other components supplied in the Treasury Account filter.
        
        Args:
        - Filter (dict): The component filters to be used in the data. Each component listed may be omitted, null, or a string value. If omitted, no filtering will be performed on that component. If null, the filter will include account numbers missing that component. If a string, the filter will perform an exact match on account numbers where that component matches the string provided. Possible values are ata (optional, string, nullable) Allocation Transfer Agency Identifier (3 characters). TAS only; aid (optional, string, nullable) Agency Identifier (3 characters); bpoa (optional, string, nullable) Beginning Period of Availability (4 characters). TAS only; epoa (optional, string, nullable) Ending Period of Availability (4 characters). TAS only; a (optional, string, nullable) Availability Type Code (1 character). Will either be 'X' or null. TAS only; main (optional, string, nullable) Main Account Code (4 characters); and sub (optional, string, nullable) Sub Account Code (3 characters). TAS only.
        - limit (int): Optional. Maximum number of results to return. Default is 10.
        
        Returns:
        - dict: A dictionary containing list of potential Ending Period of Availabilities.
        """
        data = {"filters": Filter, "limit": limit}
        endpoint = "autocomplete/accounts/epoa"
        return mr.make_request_with_post_and_data(self.base_url+endpoint, data=data)
        
    def tas_autocomplete_main(self, Filter, limit=10):
        """
        Returns the list of potential Main Account Codes narrowed by other components supplied in the Treasury Account or Federal Account filter.
        
        Args:
        - Filter (dict): The component filters to be used in the data. Each component listed may be omitted, null, or a string value. If omitted, no filtering will be performed on that component. If null, the filter will include account numbers missing that component. If a string, the filter will perform an exact match on account numbers where that component matches the string provided. Possible values are ata (optional, string, nullable) Allocation Transfer Agency Identifier (3 characters). TAS only; aid (optional, string, nullable) Agency Identifier (3 characters); bpoa (optional, string, nullable) Beginning Period of Availability (4 characters). TAS only; epoa (optional, string, nullable) Ending Period of Availability (4 characters). TAS only; a (optional, string, nullable) Availability Type Code (1 character). Will either be 'X' or null. TAS only; main (optional, string, nullable) Main Account Code (4 characters); and sub (optional, string, nullable) Sub Account Code (3 characters). TAS only.
        - limit (int): Optional. Maximum number of results to return. Default is 10.
        
        Returns:
        - dict: A dictionary containing list of potential Main Account Codes.
        """
        data = {"filters": Filter, "limit": limit}
        endpoint = "autocomplete/accounts/main"
        return mr.make_request_with_post_and_data(self.base_url+endpoint, data=data)
        
    def tas_autocomplete_sub(self, Filter, limit=10):
        """
        Returns the list of potential Sub Account Codes narrowed by other components supplied in the Treasury Account filter.
        
        Args:
        - Filter (dict): The component filters to be used in the data. Each component listed may be omitted, null, or a string value. If omitted, no filtering will be performed on that component. If null, the filter will include account numbers missing that component. If a string, the filter will perform an exact match on account numbers where that component matches the string provided. Possible values are ata (optional, string, nullable) Allocation Transfer Agency Identifier (3 characters). TAS only; aid (optional, string, nullable) Agency Identifier (3 characters); bpoa (optional, string, nullable) Beginning Period of Availability (4 characters). TAS only; epoa (optional, string, nullable) Ending Period of Availability (4 characters). TAS only; a (optional, string, nullable) Availability Type Code (1 character). Will either be 'X' or null. TAS only; main (optional, string, nullable) Main Account Code (4 characters); and sub (optional, string, nullable) Sub Account Code (3 characters). TAS only.
        - limit (int): Optional. Maximum number of results to return. Default is 10.
        
        Returns:
        - dict: A dictionary containing list of potential Sub Account Codes.
        """
        data = {"filters": Filter, "limit": limit}
        endpoint = "autocomplete/accounts/sub"
        return mr.make_request_with_post_and_data(self.base_url+endpoint, data=data)
        
    def awarding_agency_and_office_autocomplete(self, search_text, limit=None):
        """
        Returns a list of rewarding agencies matching the specified search text.
        
        Args:
        - search_text (str): Text for search query.
        - limit (int): Optional. Maximum number of results to return. Default is None.
        
        Returns:
        - dict: A dictionary containing list of rewarding agencies.
        """
        data = {"search_text": search_text}
        if limit is not None:
            data["limit"] = limit
        endpoint = "autocomplete/awarding_agency_office/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def funding_agency_autocomplete(self, search_text, limit=None):
        """
        Returns a list of funding agencies matching the specified search text.
        
        Args:
        - search_text (str): Text for search query.
        - limit (int): Optional. Maximum number of results to return. Default is None.
        
        Returns:
        - dict: A dictionary containing list of funding agencies.
        """
        data = {"search_text": search_text}
        if limit is not None:
            data["limit"] = limit
        endpoint = "autocomplete/funding_agency_office/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def cfda_autocomplete(self, search_text, limit=None):
        """
        Returns a list of cfda programs matching the specified search text.
        
        Args:
        - search_text (str): Text for search query.
        - limit (int): Optional. Maximum number of results to return. Default is None.
        
        Returns:
        - dict: A dictionary containing list of cfda programs.
        """
        data = {"search_text": search_text}
        if limit is not None:
            data["limit"] = limit
        endpoint = "autocomplete/cfda/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def city_autocomplete(self, search_text, limit, country_code, scope, state_code=None):
        """
        Returns a list of city names matching the specified search text.
        
        Args:
        - search_text (str): Text for search query.
        - limit (int): Maximum number of results to return. Required.
        - country_code (str): Country code part of a filter object. 
        - scope (str): Scope of the search, part of a filter object. Possible values are primary_place_of_performance and recipient_location.
        - state_code (str): Optional state code part of a filter object. 
        
        Returns:
        - dict: A dictionary containing list of city names.
        """
        if state_code is not None:
            data = {"search_text": search_text, "limit": limit, "filter": {"country_code": country_code, "scope": scope, "state_code": state_code}}
        else:
            data = {"search_text": search_text, "limit": limit, "filter": {"country_code": country_code, "scope": scope}}
        endpoint = "autocomplete/city/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def recipient_autocomplete(self, search_text, limit=10, recipient_levels=None):
        """
        Returns a list of recipients matching the specified search text.
        
        Args:
        - search_text (str): Text for search query.
        - limit (int): Maximum number of results to return. Default is 10, and maximum is 500.
        - recipient_levels (array): Optional. Array of strings identifying the recipient levels. Default is None.
        
        Returns:
        - dict: A dictionary containing list of recipients.
        """
        data = {"search_text": search_text, "limit": limit}
        if recipient_levels is not None:
            data["recipient_levels"] = recipient_levels
        endpoint = "autocomplete/recipient/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def glossary_autocomplete(self, search_text, limit=None):
        """
        Returns glossary autocomplete data for submitted text snippet.
        
        Args:
        - search_text (str): Text for search query.
        - limit (int): Optional. Maximum number of results to return. Default is None.
        
        Returns:
        - dict: A dictionary containing glossary autocomplete data.
        """
        data = {"search_text": search_text}
        if limit is not None:
            data["limit"] = limit
        endpoint = "autocomplete/glossary/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def naics_autocomplete(self, search_text, limit=10):
        """
        Returns a list of naics objects matching the specified search text.
        
        Args:
        - search_text (str): Text for search query.
        - limit (int): Maximum number of results to return. Default is 10.
        
        Returns:
        - dict: A dictionary containing list of naics objects.
        """
        data = {"search_text": search_text, "limit": limit}
        endpoint = "autocomplete/naics/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def psc_autocomplete(self, search_text, limit=None):
        """
        Returns a list of product or service (psc) codes matching the specified search text.
        
        Args:
        - search_text (str): Text for search query.
        - limit (int): Optional. Maximum number of results to return. Default is None.
        
        Returns:
        - dict: A dictionary containing list of product or service (psc) codes.
        """
        data = {"search_text": search_text}
        if limit is not None:
            data["limit"] = limit
        endpoint = "autocomplete/psc/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def location_autocomplete(self, search_text, limit=10):
        """
        Returns a list of locations matching the specified search text.
        
        Args:
        - search_text (str): Text for search query.
        - limit (int): Maximum number of results to return. Default is 10.
        
        Returns:
        - dict: A dictionary containing list of locations.
        """
        data = {"search_text": search_text, "limit": limit}
        endpoint = "autocomplete/location/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    ### Award-related functions
    def get_recipient_award_spending(self, awarding_agency_id, fiscal_year, limit=10, page=1):
        """
        Returns all award spending by recipient for a given agency id and fiscal year.
        
        Args:
        - awarding_agency_id (int): Internal award id of the recipient.
        - fiscal_year (int): The fiscal year for the search.
        - limit (int): Number of items to return. Defaults to 10.
        - page (int): Pagination parameter. Defaults to first page.
        
        Returns:
        - dict: Dictionary containing all award spending by recipient.
        """
        enpoint = f"award_spending/recipient/?fiscal_year={fiscal_year}&awarding_agency_id={awarding_agency_id}&limit={limit}&page={page}"
        return mr.make_request(self.base_url+enpoint)
        
    def get_award_data(self, award_id):
        """
        Returns a list of data that is associated with the award profile page.
        
        Args:
        - award_id (str): Unique identifier matching the award.
        
        Returns:
        - dict: Dictionary containing a list of data associated with an award.
        """
        enpoint = f"awards/{award_id}"
        return mr.make_request(self.base_url+enpoint)
        
    def get_award_accounts(self, award_id, page=1, limit=None, order="desc", sort="federal_account"):
        """
        Returns a list of federal accounts under a given award.
        
        Args:
        - award_id (str): Unique matching the award.
        - page (int): Optional pagination parameter. Defaults to first page.
        - limit (int): Number of items to return. Defaults to None.
        - order (str): Ordering of the data. Defaults to desc (descending), and other option is asc (ascending).
        - sort (str): The field to sort on. Default is federal_account, but other options are account_title, agency, and total_transaction_obligated_amount.
        
        Returns:
        - dict: Dictionary containing a list of federal accounts under a given award.
        """
        data = {"sort": sort, "order": order, "award_id": award_id, "page": page}
        if limit is not None:
            data["limit"] = limit
        enpoint = "awards/accounts/"
        return mr.make_request_with_post_and_json(self.base_url+enpoint, json=data)
        
    def get_federal_accounts_count_by_award(self, award_id):
        """
        Returns the number of federal accounts associated with the given award.
        
        Args:
        - award_id (str): Unique identifier matching the award.
        
        Returns:
        - dict: Dictionary containing the number of federal accounts associated with the given award.
        """
        enpoint = f"awards/count/federal_account/{award_id}"
        return mr.make_request(self.base_url+enpoint)
        
    def get_subawards_for_award(self, award_id):
        """
        Returns the number of subawards associated with the given award.
        
        Args:
        - award_id (str): Unique identifier matching the award.
        
        Returns:
        - dict: Dictionary containing the number of subawards associated with the given award.
        """
        enpoint = f"awards/count/subaward/{award_id}"
        return mr.make_request(self.base_url+enpoint)
        
    def get_award_transactions_count(self, award_id):
        """
        Returns the number of transactions associated with the given award.
        
        Args:
        - award_id (str): Unique identifier matching the award.
        
        Returns:
        - dict: Dictionary containing the number of transactions associated with the given award.
        """
        enpoint = f"awards/count/transaction/{award_id}"
        return mr.make_request(self.base_url+enpoint)
        
    def get_award_funding_data(self, award_id, page=1, limit=10, order="desc", sort="reporting_fiscal_date"):
        """
        Returns federal account, awarding agencies, funding agencies, and transaction obligated amount information for a requested award.
        
        Args:
        - award_id (str): Unique identifier matching the award.
        - page (int): Optional pagination parameter. Defaults to first page.
        - limit (int): Number of items to return. Defaults to 10.
        - order (str): Ordering of the data. Defaults to desc (descending), and other option is asc (ascending).
        - sort (str): The field to sort on. Default is reporting_fiscal_date, but other options are account_title, awarding_agency_name, disaster_emergency_fund_code, federal_account, funding_agency_name, gross_outlay_amount, object_class, program_activity, and transaction_obligated_amount.
        
        Returns:
        - dict: Dictionary containing a list of data for a given award.
        """
        data = {"sort": sort, "order": order, "award_id": award_id, "page": page, "limit": limit}
        enpoint = "awards/funding/"
        return mr.make_request_with_post_and_json(self.base_url+enpoint, json=data)
        
    def get_award_funding_obligations_and_count(self, award_id):
        """
        Returns the total transaction obligations and count of awarding agencies, funding agencies, and federal accounts for an award.
        
        Args:
        - award_id (str): Unique identifier matching the award.
       
        Returns:
        - dict: Dictionary containing a list of total transaction obligations and count of awarding agencies, funding agencies, and federal accounts for an award.
        """
        data = {"award_id": award_id}
        enpoint = "awards/funding_rollup/"
        return mr.make_request_with_post_and_json(self.base_url+enpoint, json=data)
        
    def get_award_last_updated(self):
        """
        Returns the last updated date for the award data.
        
        Args:
        - None
        
        Returns:
        - dict: Dictionary containing the last updated date for the award data.
        """
        enpoint = "awards/last_updated"
        return mr.make_request(self.base_url+enpoint)
    
    ### Budget functions    
    def get_budget_functions(self):
        """
        Returns a list of all Budget Functions ordered by their title.
        
        Args:
        - None
        
        Returns:
        - dict: Dictionary containing a list of all Budget Functions ordered by their title.
        """
        enpoint = "budget_functions/list_budget_functions"
        return mr.make_request(self.base_url+enpoint)
        
    def get_budget_subfunctions(self, budget_function=None):
        """
        Returns a list of all Budget Subfunctions that can be filtered by Budget Function, ordered by their title.
        
        Args:
        - budget_function (int): Number matching the budget function.
       
        Returns:
        - dict: Dictionary containing a list of Budget Subfunctions.
        """
        if budget_function is not None:
            data = {"budget_function": budget_function}
        else:
            data = {}
        enpoint = "budget_functions/list_budget_subfunctions/"
        return mr.make_request_with_post_and_json(self.base_url+enpoint, json=data)
        
    ### Download functions
    def bulk_award_download(self, filters, file_format="csv"):
        """
        Returns a ZIP file of award data for download.
        
        Args:
        - filters (dict): A dictionary of filter options for the downloaded data. See the endpoint docs for the format of this filter object.
        - file_format (str): Format of the file to be downloaded. Default is csv, but other options are tsv and pstxt.
       
        Returns:
        - dict: Dictionary containing the data regarding ZIP file for download.
        """
        data = {"filters": filters, "file_format": file_format}
        enpoint = "bulk_download/awards/"
        return mr.make_request_with_post_and_json(self.base_url+enpoint, json=data)
        
    def list_agencies(self, agencies_type, agency=None):
        """
        Returns one of three result set flavors. For "account_agencies" requests it returns a list of all toptier agencies with at least one DABS submission. For "award_agencies" requests it returns a list of all user selectable flagged toptier agencies with at least one subtier agency. For specific agency requests it returns a list of all user selectable flagged subtier agencies.
        
        Args:
        - agencies_type (str): Type of agency desired. Possible options are account_agencies and award_agencies.
        - agency (int): Agency identifier number.
       
        Returns:
        - dict: Dictionary containing a list of selected agency information.
        """
        data = {"type": agencies_type}
        if agency is not None:
            data["agency"] = agency
        enpoint = "bulk_download/list_agencies/"
        return mr.make_request_with_post_and_json(self.base_url+enpoint, json=data)
        
    def list_monthly_files(self, agency, fiscal_year, file_type):
        """
        Returns a list of the current versions of generated archive files for a given fiscal year and agency.
        
        Args:
        - agency (str or int): Agency database ID or all.
        - fiscal_year (int): Fiscal year.
        - file_type (str): Optional parameter for archive file type. Possible values are assistance and contracts. Defaults to None.
       
        Returns:
        - dict: Dictionary containing a list of current versions of generated archive files.
        """
        data = {"agency": agency, "fiscal_year": fiscal_year, "type": file_type}
        enpoint = "bulk_download/list_monthly_files/"
        return mr.make_request_with_post_and_json(self.base_url+enpoint, json=data)
        
    def get_download_status(self, file_name):
        """
        Returns the current status of a download job.
        
        Args:
        - file_name (str): The full name of the file downloaded. Taken from the file_name field of a download endpoint response.
        
        Returns:
        - dict: Dictionary containing the current status of a download job.
        """
        enpoint = f"bulk_download/status?file_name={file_name}"
        return mr.make_request(self.base_url+enpoint)
        
    ### Emergency and disaster related functions
    def get_count_agencies_receiving_def(self, def_codes):
        """
        Returns a count for agencies which received disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        
        Returns:
        - dict: A dictionary containing a count of agencies which received disaster/emergency funding.
        """
        data = {"filter": {"def_codes": def_codes}}
        endpoint = "disaster/agency/count/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_agencies_awarding_def_loans(self, def_codes, award_type_codes=None, limit=10, page=1, sort="id", order="desc"):
        """
        Returns insights on the Agencies awarding loans from disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - award_type_codes (list): Optional. Only accepts loan award type 07 or 08 in the array, since this endpoint is specific to loans. Defaults to None.
        - limit (int): Page size of results. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - order (str): Order of returned data. Defaults to desc (descending), with asc (ascending) as other option.
        - sort (str): Optional parameter indicating what returns values should be sorted by. Default is id, but other options are code, description, award_count, face_value_of_loan, obligation, and outlay.
        
        Returns:
        - dict: A dictionary containing insights on the Agencies awarding loans from disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes},
                "pagination": {"limit": limit, "page": page, "sort": sort, "order": order}
                }
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        endpoint = "disaster/agency/loans/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_agencies_receiving_def_funding(self, def_codes, spending_type="total", award_type_codes=None, limit=10, page=1, sort="id", order="desc"):
        """
        Returns insights on the Agencies receiving funding from disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - spending_type (str): Spending type. Defaults to total, but other option is award.
        - award_type_codes (list): Optional. Only to be used if spending type is award. Possible values are 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, A, B, C, D, IDV_A, IDV_B_A, IDV_B_B, IDV_B_C, IDV_B, IDV_C, IDV_D, IDV_E, and -1.
        - limit (int): Page size of results. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - order (str): Order of returned data. Defaults to desc (descending), with asc (ascending) as other option.
        - sort (str): Optional parameter indicating what returns values should be sorted by. Default is id, but other options are code, description, award_count, face_value_of_loan, obligation, and outlay.
        
        Returns:
        - dict: A dictionary containing insights on the Agencies receiving funding from disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes},
                "pagination": {"limit": limit, "page": page, "sort": sort, "order": order},
                "spending_type": spending_type
                }
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        endpoint = "disaster/agency/spending/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_aggregated_def_spending(self, def_codes, spending_type="total", award_type_codes=None, award_type=None, limit=10, page=1, sort="id", order="desc"):
        """
        Returns account data obligation and outlay spending aggregations of all (File D) Awards which received disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - spending_type (str): Spending type. Defaults to total, but other option is award.
        - award_type_codes (list): Optional. Only to be used if spending type is award. Possible values are 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, A, B, C, D, IDV_A, IDV_B_A, IDV_B_B, IDV_B_C, IDV_B, IDV_C, IDV_D, IDV_E, and -1.
        - award_type (str): When provided, it will return results limiting to the award type (Assistance or Procurment) based on Financial Account data. This is mutually exclusive from award_type_codes. Possible values are procurement and assistance.
        - limit (int): Page size of results. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - order (str): Order of returned data. Defaults to desc (descending), with asc (ascending) as other option.
        - sort (str): Optional parameter indicating what returns values should be sorted by. Default is id, but other options are code, description, award_count, face_value_of_loan, obligation, and outlay.
        
        Returns:
        - dict: A dictionary containing account data obligation and outlay spending aggregations of all (File D) Awards which received disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes},
                "pagination": {"limit": limit, "page": page, "sort": sort, "order": order},
                "spending_type": spending_type
                }
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        if award_type is not None:
            data["filter"]["award_type"] = award_type
        endpoint = "disaster/award/amount/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_aggregated_def_spending_count(self, def_codes, spending_type="total", award_type_codes=None, award_type=None, limit=10, page=1, sort="id", order="desc"):
        """
        Returns the count of account data obligation and outlay spending aggregations of all (File D) Awards which received disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - spending_type (str): Spending type. Defaults to total, but other option is award.
        - award_type_codes (list): Optional. Only to be used if spending type is award. Possible values are 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, A, B, C, D, IDV_A, IDV_B_A, IDV_B_B, IDV_B_C, IDV_B, IDV_C, IDV_D, IDV_E, and -1.
        - award_type (str): When provided, it will return results limiting to the award type (Assistance or Procurment) based on Financial Account data. This is mutually exclusive from award_type_codes. Possible values are procurement and assistance.
        - limit (int): Page size of results. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - order (str): Order of returned data. Defaults to desc (descending), with asc (ascending) as other option.
        - sort (str): Optional parameter indicating what returns values should be sorted by. Default is id, but other options are code, description, award_count, face_value_of_loan, obligation, and outlay.
        
        Returns:
        - dict: A dictionary containing the count of account data obligation and outlay spending aggregations of all (File D) Awards which received disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes},
                "pagination": {"limit": limit, "page": page, "sort": sort, "order": order},
                "spending_type": spending_type
                }
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        if award_type is not None:
            data["filter"]["award_type"] = award_type
        endpoint = "disaster/award/count/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_cfda_receiving_def_count(self, def_codes, award_type_codes=None):
        """
        Returns the count of CFDA programs which received disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - award_type_codes (list): Optional. Possible values are 02, 03, 04, 05, 06, 07, 08, 09, 10, 11. Defaults to None here, but in the API it defaults to all the codes.
        
        Returns:
        - dict: A dictionary containing the count of CFDA programs which received disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes}}
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        endpoint = "disaster/cfda/count/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_def_loans_for_cfda(self, def_codes, award_type_codes=None, limit=10, page=1, sort="id", order="desc"):
        """
        Returns insights on the CFDA Programs' loans from disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - award_type_codes (list): Optional. Only accepts loan award type 07 or 08 in the array, since this endpoint is specific to loans. Defaults to None.
        - limit (int): Page size of results. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - order (str): Order of returned data. Defaults to desc (descending), with asc (ascending) as other option.
        - sort (str): Optional parameter indicating what returns values should be sorted by. Default is id, but other options are code, description, award_count, face_value_of_loan, obligation, and outlay.
        
        Returns:
        - dict: A dictionary containing insights on the CFDA Programs' loans from disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes},
                "pagination": {"limit": limit, "page": page, "sort": sort, "order": order}
                }
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        endpoint = "disaster/cfda/loans/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_cfda_programs_receiving_def_funding(self, def_codes, spending_type="total", award_type_codes=None, limit=10, page=1, sort="id", order="desc"):
        """
        Returns insights on the cfda programs receiving funding from disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - spending_type (str): Spending type. Defaults to total, but other option is award.
        - award_type_codes (list): Optional. Only to be used if spending type is award. Possible values are 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, A, B, C, D, IDV_A, IDV_B_A, IDV_B_B, IDV_B_C, IDV_B, IDV_C, IDV_D, IDV_E, and -1.
        - limit (int): Page size of results. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - order (str): Order of returned data. Defaults to desc (descending), with asc (ascending) as other option.
        - sort (str): Optional parameter indicating what returns values should be sorted by. Default is id, but other options are code, description, award_count, face_value_of_loan, obligation, and outlay.
        
        Returns:
        - dict: A dictionary containing insights on the cfda programs receiving funding from disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes},
                "pagination": {"limit": limit, "page": page, "sort": sort, "order": order},
                "spending_type": spending_type
                }
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        endpoint = "disaster/cfda/spending/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_defc_receiving_def_count(self, def_codes):
        """
        Returns the count of DEFC which received disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
         
        Returns:
        - dict: A dictionary containing the count of DEFC which received disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes}}
        endpoint = "disaster/def_code/count/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_federal_accounts_receiving_def_count(self, def_codes):
        """
        Returns the count of Federal Accounts and TAS which received disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
         
        Returns:
        - dict: A dictionary containing the count of Federal Accounts and TAS which received disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes}}
        endpoint = "disaster/federal_account/count/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_def_loans_for_federal_accounts(self, def_codes, award_type_codes=None, limit=10, page=1, sort="id", order="desc"):
        """
        Returns insights on the Federal Accounts awarding loans from disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - award_type_codes (list): Optional. Only accepts loan award type 07 or 08 in the array, since this endpoint is specific to loans. Defaults to None.
        - limit (int): Page size of results. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - order (str): Order of returned data. Defaults to desc (descending), with asc (ascending) as other option.
        - sort (str): Optional parameter indicating what returns values should be sorted by. Default is id, but other options are code, description, award_count, face_value_of_loan, obligation, and outlay.
        
        Returns:
        - dict: A dictionary containing insights on the Federal Accounts awarding loans from disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes},
                "pagination": {"limit": limit, "page": page, "sort": sort, "order": order}
                }
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        endpoint = "disaster/federal_account/loans/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_federal_accounts_receiving_def_funding(self, def_codes, spending_type="total", award_type_codes=None, limit=10, page=1, sort="id", order="desc"):
        """
        Returns insights on the Federal Accounts and TAS receiving funding from disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - spending_type (str): Spending type. Defaults to total, but other option is award.
        - award_type_codes (list): Optional. Only to be used if spending type is award. Possible values are 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, A, B, C, D, IDV_A, IDV_B_A, IDV_B_B, IDV_B_C, IDV_B, IDV_C, IDV_D, IDV_E, and -1.
        - limit (int): Page size of results. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - order (str): Order of returned data. Defaults to desc (descending), with asc (ascending) as other option.
        - sort (str): Optional parameter indicating what returns values should be sorted by. Default is id, but other options are code, description, award_count, face_value_of_loan, obligation, and outlay.
        
        Returns:
        - dict: A dictionary containing insights on the Federal Accounts and TAS receiving funding from disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes},
                "pagination": {"limit": limit, "page": page, "sort": sort, "order": order},
                "spending_type": spending_type
                }
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        endpoint = "disaster/federal_account/spending/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_object_classes_receiving_def_count(self, def_codes):
        """
        Returns the count of Object Classes which received disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
         
        Returns:
        - dict: A dictionary containing the count of Object Classes which received disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes}}
        endpoint = "disaster/object_class/count/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_def_loans_for_object_classes(self, def_codes, award_type_codes=None, limit=10, page=1, sort="id", order="desc"):
        """
        Returns insights on the Object Classes' loans from disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - award_type_codes (list): Optional. Only accepts loan award type 07 or 08 in the array, since this endpoint is specific to loans. Defaults to None.
        - limit (int): Page size of results. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - order (str): Order of returned data. Defaults to desc (descending), with asc (ascending) as other option.
        - sort (str): Optional parameter indicating what returns values should be sorted by. Default is id, but other options are code, description, award_count, face_value_of_loan, obligation, and outlay.
        
        Returns:
        - dict: A dictionary containing insights on the Object Classes' loans from disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes},
                "pagination": {"limit": limit, "page": page, "sort": sort, "order": order}
                }
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        endpoint = "disaster/object_class/loans/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_object_classes_receiving_def_funding(self, def_codes, spending_type="total", award_type_codes=None, limit=10, page=1, sort="id", order="desc"):
        """
        Returns insights on the Object Classes receiving funding from disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - spending_type (str): Spending type. Defaults to total, but other option is award.
        - award_type_codes (list): Optional. Only to be used if spending type is award. Possible values are 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, A, B, C, D, IDV_A, IDV_B_A, IDV_B_B, IDV_B_C, IDV_B, IDV_C, IDV_D, IDV_E, and -1.
        - limit (int): Page size of results. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - order (str): Order of returned data. Defaults to desc (descending), with asc (ascending) as other option.
        - sort (str): Optional parameter indicating what returns values should be sorted by. Default is id, but other options are code, description, award_count, face_value_of_loan, obligation, and outlay.
        
        Returns:
        - dict: A dictionary containing insights on the Object Classes receiving funding from disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes},
                "pagination": {"limit": limit, "page": page, "sort": sort, "order": order},
                "spending_type": spending_type
                }
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        endpoint = "disaster/object_class/spending/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_recipients_receiving_def_count(self, def_codes, award_type_codes=None):
        """
        Returns the count of Recipients which received disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - award_type_codes (list): Optional. Only to be used if spending type is award. Possible values are 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, A, B, C, D, IDV_A, IDV_B_A, IDV_B_B, IDV_B_C, IDV_B, IDV_C, IDV_D, IDV_E, and -1.
        
        Returns:
        - dict: A dictionary containing the count of Recipients which received disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes}}
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        endpoint = "disaster/recipient/count/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_def_loans_for_recipients(self, def_codes, award_type_codes=None, limit=10, page=1, sort="id", order="desc"):
        """
        Returns insights on the recipient loans from disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - award_type_codes (list): Optional. Only accepts loan award type 07 or 08 in the array, since this endpoint is specific to loans. Defaults to None.
        - limit (int): Page size of results. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - order (str): Order of returned data. Defaults to desc (descending), with asc (ascending) as other option.
        - sort (str): Optional parameter indicating what returns values should be sorted by. Default is id, but other options are code, description, award_count, face_value_of_loan, obligation, and outlay.
        
        Returns:
        - dict: A dictionary containing insights on the recipient loans from disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes},
                "pagination": {"limit": limit, "page": page, "sort": sort, "order": order}
                }
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        endpoint = "disaster/recipient/loans/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_recipients_receiving_def_funding(self, def_codes, spending_type="total", award_type_codes=None, limit=10, page=1, sort="id", order="desc"):
        """
        Returns insights on the recipients receiving funding from disaster/emergency funding per the requested filters.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - spending_type (str): Spending type. Defaults to total, but other option is award.
        - award_type_codes (list): Optional. Only to be used if spending type is award. Possible values are 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, A, B, C, D, IDV_A, IDV_B_A, IDV_B_B, IDV_B_C, IDV_B, IDV_C, IDV_D, IDV_E, and -1.
        - limit (int): Page size of results. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - order (str): Order of returned data. Defaults to desc (descending), with asc (ascending) as other option.
        - sort (str): Optional parameter indicating what returns values should be sorted by. Default is id, but other options are code, description, award_count, face_value_of_loan, obligation, and outlay.
        
        Returns:
        - dict: A dictionary containing insights on the recipients receiving funding from disaster/emergency funding per the requested filters.
        """
        data = {"filter": {"def_codes": def_codes},
                "pagination": {"limit": limit, "page": page, "sort": sort, "order": order},
                "spending_type": spending_type
                }
        if award_type_codes is not None:
            data["filter"]["award_type_codes"] = award_type_codes
        endpoint = "disaster/recipient/spending/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_def_spending_by_geography(self, def_codes, geo_layer, spendng_type, geo_layer_filters=None, scope="recipient_location"):
        """
        Returns geographical spending information from emergency/disaster funding based on recipient location.
        
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V.
        - geo_layer (str): Sets the type of shape codes in the response. Possible values are state, county, and district.
        - spending_type (str): Possible values are obligation, outlay, and face_value_of_loan.
        - geo_layer_filters (list): Optional. Allows the API to only request data for what is currently in view in the map.. Defaults to None.
        - scope (str): Optional. When fetching awards, use the primary place of performance or recipient location. Defaults to recipient_location, but other values is place_of_performance.
        
        Returns:
        - dict: A dictionary containing geographical spending information from emergency/disaster funding based on recipient location.
        """
        data = {"filter": {"def_codes": def_codes},
                "geo_layer": geo_layer,
                "scope": scope,
                "spending_type": spendng_type
        }
        if geo_layer_filters is not None:
            data["geo_layer_filters"] = geo_layer_filters
        endpoint = "disaster/spending_by_geography/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    ### More download functions
    def download_account(self, account_level, submission_types, fiscal_year, agency=None, federal_account=None, quarter=None, period=None, def_codes=None, file_format="csv"):
        """
        Generate files and return metadata using filters on custom account.
            
        Args:
        - account_level (str): Used to filter for a specific type of file. Specific values are treasury_account and federal_account.
        - submission_types (list): Possible values are account_balances, object_class_program_activity, and award_financial.
        - fiscal_year (int): Fiscal year.
        - agency (str): Optional. The agency on which to filter. This field expects an internal toptier agency identifier also known as the toptier_agency_id. Defaults to None.
        - federal_account (str): Optional. An internal id. Defaults to None.
        - quarter (int): Either quarter or period is required. Do not supply both. Note that both monthly and quarterly submissions will be included in the resulting download file even if only quarter is provided. Possible values are 1, 2, 3, and 4.
        - period (int): Either quarter or period is required. Do not supply both. Agencies cannot submit data for period 1 so it is disallowed as a query filter. Note that both monthly and quarterly submissions will be included in the resulting download file even if only period is provided. Possible values are 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, and 12.
        - def_codes (list): Option search parameter by def codes.
        - file_format (str): Optional. Defaults to csv, but other values are tsv and pstxt.
            
        Returns:
        - dict: A dictionary containing information on the download job.
        """
        data = {"account_level": account_level,
                "file_format": file_format,
                "filters": {
                    "fy": fiscal_year,
                    "submission_types": submission_types
                    }
        }
        if quarter is not None and period is not None:
            print("Either quarter or period must be supplied, not both.")
            exit()
        elif quarter is None and period is None:
            print("Either quarter or period must be supplied.")
            exit()
        elif quarter is not None and period is None:
            data["filters"]["quarter"] = quarter
        elif period is not None and quarter is None:
            data["filters"]["period"] = period
        if agency is not None:
            data["filters"]["agency"] = agency
        if federal_account is not None:
            data["filters"]["federal_account"] = federal_account
        if def_codes is not None:
            data["filters"]["def_codes"] = def_codes
        endpoint = "download/accounts/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
            
    def download_assistance_data(self, award_id, file_format="csv"):
        """
        Creates a new download job for the requested award and returns a link to a zipped file containing contract award data.
            
        Args:
        - award_id (str): Unique identifier for the award.
        - file_format (str): Optional. Defaults to csv, but other values are tsv and pstxt.
            
        Returns:
        - dict: A dictionary containing information about the download job.
        """
        data = {"award_id": award_id, "file_format": file_format}
        endpoint = "download/assistance/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
            
    def download_award_data_advanced(self, filters, columns=None, file_format="csv", limit=None):
        """
        Creates a download job for the award data matching the search filters.
        
        Args:
        - filters (dict): An advanced json object for filtering results. Must contain ar least one filter entry. See this endpoint's docs for information on format of this filtering object.
        - columns (list): A list of the column names desired. Default is None.
        - file_format (str): Default is csv, but other options are tsv and pstxt.
        - limit (int): Optional. Number of items in file. Default is None.
        
        Returns:
        - dict: A dictionary containing information about the download job.
        """
        data = {"filters": filters,
                "file_format": file_format
        }
        if columns is not None:
            data["columns"] = columns
        if limit is not None:
            data["limit"] = limit
        endpoint = "download/awards/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def download_contract_data(self, award_id, file_format="csv"):
        """
        Creates a new download job for the requested award and returns a link to a zipped file containing award contract data.
            
        Args:
        - award_id (str): Unique identifier for the award.
        - file_format (str): Optional. Defaults to csv, but other values are tsv and pstxt.
            
        Returns:
        - dict: A dictionary containing information about the download job.
        """
        data = {"award_id": award_id, "file_format": file_format}
        endpoint = "download/contract/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def download_transaction_count(self, filters):
        """
        Returns the number of transactions that would be included in a download request for the given filter set.
            
        Args:
        - filters (dict): Advanced json filter object. See this endpoint's docs for information on the format of this json object.
            
        Returns:
        - dict: A dictionary containing a number of transactions.
        """
        data = filters
        endpoint = "download/count/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
       
    def download_def_data(self, def_codes, file_format="csv"):
        """
        Creates a new download job for the requested COVID-19 related account and award. Returns a link to a zipped file containing the generated data files.
            
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V, but it must be either one of these or all of them.
        - file_format (str): Optional. Defaults to csv, but other values are tsv and pstxt.
            
        Returns:
        - dict: A dictionary containing information about the download job.
        """
        data = {"filters": {"def_codes": def_codes}, "file_format": file_format}
        endpoint = "download/disaster/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def download_def_recipient_data(self, def_codes, award_type_codes=None, query=None):
        """
        Returns information to download a zip file of recipient disaster data. Specifically, only COVID-19 at the moment
            
        Args:
        - def_codes (list): A list of Disaster Emergency Fund (def) codes (strings). Possible values are L, M, N, O, P, U, and V, but it must be either one of these or all of them.
        - award_type_codes (list): Optional. Possible values are 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, A, B, C, D, IDV_A, IDV_B_A, IDV_B_B, IDV_B_C, IDV_B, IDV_C, IDV_D, IDV_E, and -1.
        - query (str): Search query term.
            
        Returns:
        - dict: A dictionary containing information about the download job.
        """
        data = {"filters": {"def_codes": def_codes}}
        if award_type_codes is not None:
            data["filters"]["award_type_codes"] = award_type_codes
        if query is not None:
            data["filters"]["query"] = query
        endpoint = "download/disaster/recipients/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def download_idv_data(self, award_id, file_format="csv"):
        """
        Creates a new download job for the requested award and returns a link to a zipped file containing IDV data.
            
        Args:
        - award_id (str): Unique identifier for the award.
        - file_format (str): Optional. Defaults to csv, but other values are tsv and pstxt.
            
        Returns:
        - dict: A dictionary containing information about the download job.
        """
        data = {"award_id": award_id, "file_format": file_format}
        endpoint = "download/idv/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def download_transactions_data_advanced(self, filters, columns=None, file_format="csv", limit=None):
        """
        Creates a download job for the transaction data matching the search filters.
        
        Args:
        - filters (dict): An advanced json object for filtering results. Must contain ar least one filter entry. See this endpoint's docs for information on format of this filtering object.
        - columns (list): A list of the column names desired. Default is None.
        - file_format (str): Default is csv, but other options are tsv and pstxt.
        - limit (int): Optional. Number of items in file. Default is None.
        
        Returns:
        - dict: A dictionary containing information about the download job.
        """
        data = {"filters": filters,
                "file_format": file_format
        }
        if columns is not None:
            data["columns"] = columns
        if limit is not None:
            data["limit"] = limit
        endpoint = "download/transactions/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    ### Other functions 
    def get_federal_account(self, account_number, fiscal_year=current):
        """
        Returns the agency identifier, account code, title, and database id for the given federal account.
        
        Args:
        - account_number (str): The Federal Account symbol comprised of Agency Code and Main Account Code. A unique identifier for federal accounts.
        - fiscal_year (str): Desired fiscal year. Defaults to current year.
        
        Returns:
        - dict: A dictionary containing the agency identifier, account code, title, and database id for the given federal account.
        """
        endpoint = f"federal_accounts/{account_number}/?fiscal_year={fiscal_year}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_spending_data_by_object_class(self, federal_account_id):
        """
        Returns object classes that the specified federal account has allotted money toward.
        
        Args:
        - federal_account_id (int): Database id for a federal account.
        
        Returns:
        - dict: A dictionary containing the data matching the parameter.
        """
        endpoint = f"federal_accounts/{federal_account_id}/available_object_classes"
        return mr.make_request(self.base_url+endpoint)
        
    def get_fiscal_year_snapshot_for_federal_account(self, federal_account_id, fiscal_year=current):
        """
        Returns budget information for a federal account for the year provided based on account's internal ID.
        
        Args:
        - federal_account_id (int): Database id for a federal account.
        - fiscal_year (int): The fiscal year. Defaults to the current year.
        
        Returns:
        - dict: A dictionary containing budget information for a federal account for the year provided based on account's internal ID
        """
        endpoint = f"federal_accounts/{federal_account_id}/fiscal_year_snapshot/{fiscal_year}"
        return mr.make_request(self.base_url+endpoint)
        
    def search_federal_accounts(self, fiscal_year=str(current), agency_identifier=None, sort_direction="desc", sort_field="budgetary_resources", limit=50, page=1, keyword=None):
        """
        Returns a list of federal accounts, their number, name, managing agency, and budgetary resources matching the search parameters.
        
        Args:
        - fiscal_year (str): The desired fiscal year, entered as a string. If none is given, default is previous year.
        - agency_identifier (str): Agency id. Optional. Defaults to None.
        - sort_direction (str): The direction in which to sort. Defaults to desc, but other option is asc.
        - sort_field (str): The field on which to sort. Default is budgetary_resources, but other options are account_number, account_name, and managing_agency.
        - limit (int): Number of results to include per page. Defaults to 50.
        - page (int): The page to return. Defaults to first page.
        - keyword (str): Optional search term. Default is None.
        
        Returns:
        - dict: A dictionary containing a list of federal accounts, their number, name, managing agency, and budgetary resources matching the search parameters.
        """
        data = {"filters": {"fy": fiscal_year},
                "sort": {
                    "direction": sort_direction,
                    "field": sort_field
                    },
                "limit": limit,
                "page": page,
        }
        if agency_identifier is not None:
            data["filters"]["agency_identifier"] = agency_identifier
        if keyword is not None:
            data["keyword"] = keyword
        endpoint = "federal_accounts/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_federal_account_by_obligation(self, fiscal_year, funding_agency_id, limit=10, page=1):
        """
        Returns the amount that the specific agency has obligated to various federal accounts in a given fiscal year.
        
        Args:
        - fiscal_year (int): The desired fiscal year.
        - funding_agency_id (int): The unique USAspending.gov agency identifier. This ID is the agency_id value returned in the /api/v2/references/toptier_agencies/ endpoint.
        - limit (int): Maximum number of results to return.
        - page (int): Optional pagination parameter. Defaults to first page.
        
        Returns:
        - dict: A dictionary containing the amount that the specific agency has obligated to various federal accounts in a given fiscal year.
        """
        endpoint = f"federal_obligations/?fiscal_year={fiscal_year}&funding_agency_id={funding_agency_id}&limit={limit}&page={page}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_financial_balances(self, fiscal_year, funding_agency_id):
        """
        Returns aggregated balances for a specific government agency in a given fiscal year.
        
        Args:
        - fiscal_year (int): The desired fiscal year.
        - funding_agency_id (int): The unique USAspending.gov agency identifier. This ID is the agency_id value returned in the /api/v2/references/toptier_agencies/ endpoint.
          
        Returns:
        - dict: A dictionary containing financial balance data.
        """
        endpoint = f"financial_balances/agencies/?fiscal_year={fiscal_year}&funding_agency_id={funding_agency_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_financial_spending_by_object_class(self, fiscal_year, funding_agency_id):
        """
        Returns the total amount that a specific agency has obligated to major object classes in a given fiscal year.
        
        Args:
        - fiscal_year (int): The desired fiscal year.
        - funding_agency_id (int): The unique USAspending.gov agency identifier. This ID is the agency_id value returned in the /api/v2/references/toptier_agencies/ endpoint.
          
        Returns:
        - dict: A dictionary containing financial spending data.
        """
        endpoint = f"financial_spending/major_object_class/?fiscal_year={fiscal_year}&funding_agency_id={funding_agency_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_financial_spending_for_minor_object_class(self, fiscal_year, funding_agency_id, major_object_class_code):
        """
        Returns the total amount that a specific agency has obligated to minor object classes within a specific major object class in a given fiscal year.
        
        Args:
        - fiscal_year (int): The desired fiscal year.
        - funding_agency_id (int): The unique USAspending.gov agency identifier. This ID is the agency_id value returned in the /api/v2/references/toptier_agencies/ endpoint.
        - major_object_class_code (int): The major object class code returned in /api/v2/financial_spending/major_object_class/.
          
        Returns:
        - dict: A dictionary containing financial spending data.
        """
        endpoint = f"financial_spending/major_object_class/?fiscal_year={fiscal_year}&funding_agency_id={funding_agency_id}&major_object_class_code={major_object_class_code}"
        return mr.make_request(self.base_url+endpoint)
        
    ### IDV functions  
    def get_federal_accounts_under_idv(self, award_id, page=1, limit=10, order="desc", sort="total_transaction_obligated_amount"):
        """
        Returns a list of federal accounts under a given IDV.
        
        Args:
        - award_id (str): IDV (Indefinite Delivery Vehicle) to return accounts for.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Optional. Number of items to return. Default is 10.
        - order (str): Order in which to return data. Default is desc, and other option is asc.
        - sort (str): Sorting parameter. Default is total_transaction_obligated_amount, but other options are federal_account, agency, and account_title.
        
        Returns:
        - dict: A dictionary containing a list of federal accounts.
        """
        data = {"limit": limit,
                "sort": sort,
                "order": order,
                "award_id": award_id,
                "page": page
        }
        endpoint = "idvs/accounts/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_idv_activity(self, award_id, page=1, limit=10, hide_edge_cases="false"):
        """
        Returns a list of child and grandchild awards for a given IDV.
        
        Args:
        - award_id (str): IDV (Indefinite Delivery Vehicle) to return accounts for.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Optional. Number of items to return. Default is 10.
        - hide_edge_cases (str): Choose whether or not to hide awards that have no/negative obligated amounts and/or no/negative awarded amounts and/or no end date. Default is false and true is other option.
        
        Returns:
        - dict: A dictionary containing a list of awards.
        """
        data = {"award_id": award_id,
                "page": page,
                "hide_edge_cases": hide_edge_cases,
                "limit": limit
        }
        endpoint = "idvs/activity/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_idv_amounts(self, award_id):
        """
        Returns aggregated award counts and funding amounts for IDV contracts.
        
        Args:
        - award_id (str): Either a "generated" natural award id (string) or a database surrogate award id (number). Generated award identifiers are preferred as they are effectively permanent. Surrogate award ids are retained for backward compatibility but are deprecated.
           
        Returns:
        - dict: A dictionary containing a list of award coints and funding amounts.
        """
        endpoint = f"idvs/amounts/{award_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_idv_awards(self, award_id, Type="child_idvs", page=1, limit=10, order="desc", sort="period_of_performance_start_date"):
        """
        Returns a list of child IDVs, child awards, or grandchild awards for IDV.
        
        Args:
        - award_id (str): Either a "generated" natural award id (string) or a database surrogate award id (number). Generated award identifiers are preferred as they are effectively permanent. Surrogate award ids are retained for backward compatibility but are deprecated.
        - type (str): The type of related awards to return. Default is child_idvs, but other options are child_awards and grandchild_awards.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Optional. Number of items to return. Default is 10.
        - order (str): Order in which to return data. Default is desc, and other option is asc.
        - sort (str): Sorting parameter. Default is period_of_performance_start_date, but other options are piid, description, period_of_performance_current_end_date, last_date_to_order, funding_agency, awarding_agency, award_type, and obligated_amount.
        
        Returns:
        - dict: A dictionary containing a list of idv award data.
        """
        data = {"award_id": award_id,
                "type": Type,
                "limit": limit,
                "page": page,
                "sort": sort,
                "order": order,        
        }
        endpoint = "idvs/awards/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_idv_federal_account_count(self, award_id, piid=None):
        """
        Returns the number of federal accounts associated with the given IDV and it's children and grandchildren.
        
        Args:
        - award_id (str): Either a "generated" natural award id (string) or a database surrogate award id (number). Generated award identifiers are preferred as they are effectively permanent. Surrogate award ids are retained for backward compatibility but are deprecated.
        - piid (str): Optional. Award ID to further refine results. All File C financial data for this award is returned if omitted. Defaults to None.
          
        Returns:
        - dict: A dictionary containing a federal account count.
        """
        if piid is not None:
            endpoint = f"idvs/count/federal_account/{award_id}/?piid={piid}"
        else:
            endpoint = f"idvs/count/federal_account/{award_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_idv_funding(self, award_id, piid=None, page=1, limit=10, order="desc", sort="reporting_fiscal_date"):
        """
        Returns a list of File C financial data for an IDV award's descendant contracts.
        
        Args:
        - award_id (str): Either a "generated" natural award id (string) or a database surrogate award id (number). Generated award identifiers are preferred as they are effectively permanent. Surrogate award ids are retained for backward compatibility but are deprecated.
        - piid (str): Optional. Award ID to further refine results. All File C financial data for this award is returned if omitted. Defaults to None.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Optional. Number of items to return. Default is 10.
        - order (str): Order in which to return data. Default is desc, and other option is asc.
        - sort (str): Sorting parameter. Default is reporting_fiscal_date, but other options are account_title, disaster_emergency_fund_code, gross_outlay_amount, object_class, piid, program_activity, reporting_agency_name, and transaction_obligated_amount.
        
        Returns:
        - dict: A dictionary containing a list of financial data.
        """
        data = {"award_id": award_id,
                "page": page,
                "sort": sort,
                "order": order,
                "limit": limit        
        }
        if piid is not None:
            data["piid"] = piid
        endpoint = "idvs/funding/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_idv_funding_totals(self, award_id):
        """
        Returns award metadata summing the total transaction obligations and counting awarding agencies, funding agencies, and federal accounts for an IDV's children and grandchildren.
        
        Args:
        - award_id (str): Either a "generated" natural award id (string) or a database surrogate award id (number). Generated award identifiers are preferred as they are effectively permanent. Surrogate award ids are retained for backward compatibility but are deprecated.
          
        Returns:
        - dict: A dictionary containing award metadata.
        """
        data = {"award_id": award_id}
        endpoint = "idvs/funding_rollup/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    ### Recipient functions
    def search_recipients(self, order="desc", sort="amount", limit=50, page=1, keyword=None, award_type="all"):
        """
        Returns a list of recipients, their level, DUNS, UEI, and amount.
        
        Args:
        - order (str): The direction results are sorted by. asc for ascending, desc for descending. Default is desc.
        - sort (str): The field results are sorted by. Default is amount, but other values are name and duns.
        - limit (int): Number of results per page. Default is 50. Max is 1000.
        - page (int): Pagination parameter. Defaults to first page.
        - keyword (str): The keyword results are filtered by. Searches on name, UEI, or DUNS.        
        - award_type (str): The award type results are filtered by. Default is all, but other options are contracts, grants, loans, direct_payments, and other_financial_assistance.
        
        Returns:
        - dict: A dictionary containing a list of recipient data.
        """
        data = {"order": order,
                "sort": sort,
                "limit": limit if limit <= 1000 else 1000,
                "page": page,
                "award_type": award_type       
        }
        if keyword is not None:
            data["keyword"] = keyword
        endpoint = "recipient/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_child_recipients_by_duns_or_uei(self, duns_or_uei, year="latest"):
        """
        Returns a list of child recipients belonging to the given parent recipient DUNS or UEI.
        
        Args:
        - duns_or_uei (str): Parent recipient's DUNS or UEI.
        - year (str): The fiscal year you would like data for. Use all to view all time or latest to view the latest 12 months. Default is latest.   
        
        Returns:
        - dict: A dictionary containing a list of child recipients.
        """
        endpoint = f"recipient/children/{duns_or_uei}/?year={year}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_recipient_count(self, keyword=None, award_type="all"):
        """
        Returns the count of recipients given an award_type and keyword string.
        
        Args:
        - keyword (str): The keyword results are filtered by. Searches on name, UEI, or DUNS.        
        - award_type (str): The award type results are filtered by. Default is all, but other options are contracts, grants, loans, direct_payments, and other_financial_assistance.
        
        Returns:
        - dict: A dictionary containing a count of recipients.
        """
        data= {"award_type": award_type}
        if keyword is not None:
            data["keyword"] = keyword
        endpoint = "recipient/count/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_recipient_overview(self, recipient_id, year="latest"):
        """
        Returns a high-level overview of a specific recipient, given its id.
        
        Args:
        - recipient_id (str): A unique identifier for the recipient at a specific level (parent, child, or neither).
        - year (str): The fiscal year you would like data for. Use all to view all time or latest to view the latest 12 months. Default is latest.   
        
        Returns:
        - dict: A dictionary containing an overview of recipient.
        """
        endpoint = f"recipient/{recipient_id}/?year={year}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_state_metadata(self, fips, year="latest"):
        """
        Returns a high-level overview of a specific state or territory, given its USAspending.gov id.
        
        Args:
        - fips (str): The FIPS code for the state you want to view. You must include leading zeros.
        - year (str): The fiscal year you would like data for. Use all to view all time or latest to view the latest 12 months. Default is latest.   
        
        Returns:
        - dict: A dictionary containing state metadata.
        """
        endpoint = f"recipient/state/{fips}?year={year}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_states(self):
        """
        Returns a list of states and their amounts.
        
        Args:
        - None
          
        Returns:
        - dict: A dictionary containing a list of states.
        """
        endpoint = "recipient/state"
        return mr.make_request(self.base_url+endpoint)
        
    def get_state_award_breakdown(self, fips, year="latest"):
        """
        Returns the award amounts and totals, based on award type, of a specific state or territory, given its USAspending.gov id.
        
        Args:
        - fips (str): The FIPS code for the state you want to view. You must include leading zeros.
        - year (str): The fiscal year you would like data for. Use all to view all time or latest to view the latest 12 months. Default is latest.   
        
        Returns:
        - dict: A dictionary containing amounts and totals of a state.
        """
        endpoint = f"recipient/state/awards/{fips}/?year={year}"
        return mr.make_request(self.base_url+endpoint)
        
    ### Differences and discrepancies functions 
    def get_obligation_difference_data(self, toptier_code, fiscal_year, fiscal_period, page=1, limit=10, order="desc", sort="tas"):
        """
        Returns an overview of government agency obligation differences data.
        
        Args:
        - toptier_code (str): The specific agency code.
        - fiscal_year (int): The fiscal year.
        - fiscal_period (int): The fiscal period. Valid values: 2-12 (2 = November ... 12 = September) For retriving quarterly data, provide the period which equals 'quarter * 3' (e.g. Q2 = P6).
        - page (int): Optional pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Defaults to 10.
        - order (str): The direction (asc or desc) that the sort field will be sorted in. Default is desc.
        - sort (str):  A data field that will be used to sort the response array. Default is tas, but other options are difference, file_a_obligation, and file_b_obligation.
        Returns:
        - dict: A dictionary containing an overview of government agency obligation differences data.
        """
        endpoint = f"reporting/agencies/{toptier_code}/differences/?fiscal_year={fiscal_year}&fiscal_period={fiscal_period}&page={page}&limit={limit}&order={order}&sort={sort}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_tas_discrepancies_data(self, toptier_code, fiscal_year, fiscal_period, page=1, limit=10, order="desc", sort="amount"):
        """
        Returns an overview of government agency TAS discrepancies data.
        
        Args:
        - toptier_code (str): The specific agency code.
        - fiscal_year (int): The fiscal year.
        - fiscal_period (int): The fiscal period. Valid values: 2-12 (2 = November ... 12 = September) For retriving quarterly data, provide the period which equals 'quarter * 3' (e.g. Q2 = P6).
        - page (int): Optional pagination parameter. Defaults to first page.
        - limit (int): Number of results per page. Defaults to 10.
        - order (str): The direction (asc or desc) that the sort field will be sorted in. Default is desc.
        - sort (str):  A data field that will be used to sort the response array. Default is amount, but other option is tas.
        Returns:
        - dict: A dictionary containing an overview of government agency TAS discrepancies data.
        """
        endpoint = f"reporting/agencies/{toptier_code}/discrepancies/?fiscal_year={fiscal_year}&fiscal_period={fiscal_period}&page={page}&limit={limit}&order={order}&sort={sort}"
        return mr.make_request(self.base_url+endpoint)
        
    ### References functions
    def get_agency_overview_by_agency_id(self, agency_id):
        """
        Returns a high-level overview of a specific government agency, given its USAspending.gov id.
        
        Args:
        - agency_id (int): The unique USAspending.gov agency identifier. This ID is the agency_id value returned in the /api/v2/references/toptier_agencies/ endpoint.
          
        Returns:
        - dict: A dictionary containing an agency overview.
        """
        endpoint = f"references/agency/{agency_id}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_award_types(self):
        """
        Returns a grouping of award types.
        
        Args:
        - None
          
        Returns:
        - dict: A dictionary containing a grouping of award types.
        """
        endpoint = "references/award_types"
        return mr.make_request(self.base_url+endpoint)
    
    # This doesn't seem to be working.  
#    def get_opportunity_totals_for_all_cfdas(self):
#        """
#        Returns opportunity totals for a CFDA or all opportunity totals.
#        
#        Args:
#        - None
#          
#        Returns:
#        - dict: A dictionary containing opportunity totals for a CFDA or all opportunity totals.
#        """
#        endpoint = "references/cfda/totals"
#        return mr.make_request(self.base_url+endpoint)

    def get_data_dictionary(self):
        """
        Returns data corresponding to the latest data dictionary csv file.
        
        Args:
        - None
          
        Returns:
        - dict: A dictionary containing data corresponding to the latest data dictionary csv file.
        """
        endpoint = "references/data_dictionary"
        return mr.make_request(self.base_url+endpoint)
        
    def get_def_codes(self):
        """
        Returns a JSON object describing all Disaster and Emergency Funding (DEF) Codes.
        
        Args:
        - None
          
        Returns:
        - dict: A dictionary containing all Disaster and Emergency Funding (DEF) Codes
        """
        endpoint = "references/def_codes"
        return mr.make_request(self.base_url+endpoint)
        
    def get_filter_hash_for_url(self, filters):
        """
        Returns a hash for URL, based on selected filter criteria.
        
        Args:
        - filters (dict): Advanced JSON filtering object. See this endpoint's docs for information on the format of this filtering object.
        
        Returns:
        - dict: A dictionary containing a hash.
        """
        data= {"filters": filters}
        endpoint = "references/filter/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_psc_search_tree_nodes(self, depth=0, Filter=None):
        """
        Returns the basic groupings of Product Service Codes.
        
        Args:
        - depth (int): Defines how many levels of descendants to return under each node. For example, depth=0 will return a flat array, while depth=2 will populate the children array of each top level node with that node's children and grandchildren. The actual depth of each tree may be less than the value of depth if returned nodes have no children. Negative values are treated as infinite, returning all descendants. Default is 0.
        - Filter (str):  Restricts results to nodes with a id or description matching the filter string. If depth is greater than zero, nodes will also appear the response if at least one child within depth matches the filter. Default is None.  
        
        Returns:
        - dict: A dictionary containing the basic groupings of the psc codes.
        """
        if Filter is not None:
            endpoint = f"references/filter_tree/psc/?depth={depth}&filter={Filter}"
        else:
            endpoint = f"references/filter_tree/psc/?depth={depth}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_tas_search_tree_nodes(self, depth=0, Filter=None):
        """
        Returns a list of toptier agencies that have at least one TAS affiliated with them.
        
        Args:
        - depth (int): Defines how many levels of descendants to return under each node. For example, depth=0 will return a flat array, while depth=2 will populate the children array of each top level node with that node's children and grandchildren. The actual depth of each tree may be less than the value of depth if returned nodes have no children. Negative values are treated as infinite, returning all descendants. Default is 0.
        - Filter (str):  Restricts results to nodes with a id or description matching the filter string. If depth is greater than zero, nodes will also appear the response if at least one child within depth matches the filter. Default is None.  
        
        Returns:
        - dict: A dictionary containing a list of toptier agencies.
        """
        if Filter is not None:
            endpoint = f"references/filter_tree/tas/?depth={depth}&filter={Filter}"
        else:
            endpoint = f"references/filter_tree/tas/?depth={depth}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_glossary(self, page=1, limit=10):
        """
        Returns a list of glossary data.
        
        Args:
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of items per page. Defaults to 10.
          
        Returns:
        - dict: A dictionary containing a list of glossary data.
        """
        endpoint = f"references/glossary/?page={page}&limit={limit}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_filter_object_from_hash(self, Hash):
        """
        Accepts a hash generated by /api/v2/references/filter/ and returns an Advanced Search filter object.
        
        Args:
        - hash (str): A hash.
        
        Returns:
        - dict: A dictionary containing a filter object.
        """
        data= {"hash": Hash}
        endpoint = "references/hash/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_naics_codes(self, Filter=None):
        """
        Returns a list of Tier 1 NAICS codes, their descriptions, and a count of their Tier 3 grandchildren. If filter is provided then return parents/grandparents that match the search text.
        
        Args:
        - Filter (str): Optional. This will filter the NAICS by their descriptions to those matching the text. Default is None.
        
        Returns:
        - dict: A dictionary containing a list of naics codes.
        """
        if Filter is not None:
            endpoint = f"references/naics/?filter={Filter}"
        else:
            endpoint = "references/naics"
        return mr.make_request(self.base_url+endpoint)
    
    def get_submission_periods(self, use_cache=False):
        """
        Returns a list of all fields in the "dabs_submission_window_schedule" table except 'id'.
        
        Args:
        - use_cache (bool): Optional. Whether or not to use a cache when retrieving values. Defaults to false.
        
        Returns:
        - dict: A dictionary containing a list of all fields in the "dabs_submission_window_schedule" table except 'id'.
        """
        if use_cache:
            endpoint = f"references/submission_periods/?use_cache={use_cache}"
        else:
            endpoint = "references/submission_periods"
        return mr.make_request(self.base_url+endpoint)
        
    def get_toptier_agencies(self, sort="percentage_of_total_budget_authority", order="desc"):
        """
        Returns a list of toptier agencies, their budgetary resources, and and the percent of the total government budget authority this agency accounts for.
        
        Args:
        - sort (str): A data field that will be used to sort the response array. Defaults to percentage_of_total_budget_authority.
        - order (str): The direction (asc or desc) that the sort field will be sorted in. Defaults to desc.
        
        Returns:
        - dict: A dictionary containing a list of toptier agencies.
        """
        endpoint = f"references/toptier_agencies/?sort={sort}&order={order}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_total_budgetary_resources(self, fiscal_year=None, fiscal_period=None):
        """
        Returns federal budgetary resources by fiscal year and fiscal period.
        
        Args:
        - fiscal_year (int): Optional. The fiscal year to retrieve, 2017 or later. Defaults to None.
        - fiscal_period (int): Optional. The fiscal period. If this optional parameter is provided then fiscal_year is a required parameter. If fiscal_period is provided without fiscal_year, a 400 error is returned. Valid values: 2-12 (2 = November ... 12 = September). For retrieving quarterly data, provide the period which equals 'quarter * 3' (e.g. Q2 = P6). If neither paramater is provided, the entire available history will be returned.
        
        Returns:
        - dict: A dictionary containing federal budgetary resources by fiscal year and fiscal period.
        """
        if fiscal_year is not None and fiscal_period is None:
            endpoint = f"references/total_budgetary_resources/?fiscal_year={fiscal_year}"
        if fiscal_year is not None and fiscal_period is not None:
            endpoint = f"references/total_budgetary_resources/?fiscal_year={fiscal_year}&fiscal_period={fiscal_period}"
        if fiscal_year is None and fiscal_period is not None:
            print("If fiscal_period parameter is passed, fiscal_year must be passed as well.")
            exit()
        if fiscal_year is None and fiscal_period is None:
            endpoint = "references/total_budgetary_resources"
        return mr.make_request(self.base_url+endpoint)
        
    ### Reporting functions   
    def get_agency_overview_by_toptier_code(self, toptier_code, page=1, limit=10, order="desc", sort="current_total_budget_authority_amount"):
        """
        Returns an overview of government agency submission data. 
        
        Args:
        - toptier_code (str): The specific agency's toptier code.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of items per page. Defaults to 10.
        - order (str): The direction (asc or desc) that the sort field will be sorted in. Defaults to desc.
        - sort (str): A data field that will be used to sort the response array. Default is current_total_budget_authority_amount, but other options are fiscal_period, fiscal_year, missing_tas_accounts_count, tas_accounts_total, obligation_difference, percent_of_total_budgetary_resources, recent_publication_date, recent_publication_date_certified, tas_obligation_not_in_gtas_total, unlinked_contract_award_count, and unlinked_assistance_award_count.
          
        Returns:
        - dict: A dictionary containing an overview of government agency submission data.
        """
        endpoint = f"reporting/agencies/{toptier_code}/overview/?page={page}&limit={limit}&order={order}&sort={sort}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agency_overview_by_year(self, fiscal_year, fiscal_period, Filter=None, page=1, limit=10, order="desc", sort="current_total_budget_authority_amount"):
        """
        Returns an overview of government agency submission data. 
        
        Args:
        - fiscal_year (int): The fiscal year.
        - fiscal_period (int): The fiscal period. Valid values: 2-12 (2 = November ... 12 = September) For retriving quarterly data, provide the period which equals 'quarter * 3' (e.g. Q2 = P6).
        - Filter (str): The agency name or abbreviation to filter on (partial match, case insesitive). Defaults to None.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of items per page. Defaults to 10.
        - order (str): The direction (asc or desc) that the sort field will be sorted in. Defaults to desc.
        - sort (str): A data field that will be used to sort the response array. Default is current_total_budget_authority_amount, but other options are fiscal_period, fiscal_year, missing_tas_accounts_count, tas_accounts_total, obligation_difference, percent_of_total_budgetary_resources, recent_publication_date, recent_publication_date_certified, tas_obligation_not_in_gtas_total, unlinked_contract_award_count, and unlinked_assistance_award_count.
          
        Returns:
        - dict: A dictionary containing an overview of government agency submission data.
        """
        if Filter is not None:
            endpoint = f"reporting/agencies/overview/?fiscal_year={fiscal_year}&fiscal_period={fiscal_period}&filter={Filter}&page={page}&limit={limit}&order={order}&sort={sort}"
        else:
            endpoint = f"reporting/agencies/overview/?fiscal_year={fiscal_year}&fiscal_period={fiscal_period}&page={page}&limit={limit}&order={order}&sort={sort}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_agency_reporting_publish_dates(self, fiscal_year, Filter=None, page=1, limit=10, order="desc", sort="current_total_budget_authority_amount"):
        """
        Returns list of agency submission information, included published and certified dates for the fiscal year.
        
        Args:
        - fiscal_year (int): The fiscal year.
        - Filter (str): The agency name or abbreviation to filter on (partial match, case insesitive). Defaults to None.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of items per page. Defaults to 10.
        - order (str): The direction (asc or desc) that the sort field will be sorted in. Defaults to desc.
        - sort (str): A data field that will be used to sort the response array. Default is current_total_budget_authority_amount, but other options are agency_name, abbreviation, toptier_code, and publication_date.
          
        Returns:
        - dict: A dictionary containing a list of agency submission information, included published and certified dates for the fiscal year.
        """
        if Filter is not None:
            endpoint = f"reporting/agencies/publish_dates/?fiscal_year={fiscal_year}&filter={Filter}&page={page}&limit={limit}&order={order}&sort={sort}"
        else:
            endpoint = f"reporting/agencies/publish_dates/?fiscal_year={fiscal_year}&page={page}&limit={limit}&order={order}&sort={sort}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_reporting_publishing_dates_for_single_agency(self, toptier_code, fiscal_year, fiscal_period):
        """
        Returns the history of publication and certification dates for a single agency's submission. 
        
        Args:
        - toptier_code (str): The specific agency's toptier code.
        - fiscal_year (int): The fiscal year of the submission.
        - fiscal_period (int): The fiscal period of the submission. valid values: 2-12 (2 = November ... 12 = September) For retriving quarterly submissions, provide the period which equals 'quarter * 3' (e.g. Q2 = P6).
             
        Returns:
        - dict: A dictionary containing a publishing and certification data for a single agency.
        """        
        endpoint = f"reporting/agencies/{toptier_code}/{fiscal_year}/{fiscal_period}/submission_history"
        return mr.make_request(self.base_url+endpoint)
        
    def get_unlinked_awards_for_agency(self, toptier_code, fiscal_year, fiscal_period, Type):
        """
        Returns the number of unlinked and linked awards for the agency in the provided fiscal year and period.
        
        Args:
        - toptier_code (str): The specific agency's toptier code.
        - fiscal_year (int): The fiscal year of the submission.
        - fiscal_period (int): The fiscal period of the submission. valid values: 2-12 (2 = November ... 12 = September) For retriving quarterly submissions, provide the period which equals 'quarter * 3' (e.g. Q2 = P6).
        - Type (str): Possible vales are assistance and procurement. 
        
        Returns:
        - dict: A dictionary containing number of unlinked and linked awards.
        """        
        endpoint = f"reporting/agencies/{toptier_code}/{fiscal_year}/{fiscal_period}/unlinked_awards/{Type}"
        return mr.make_request(self.base_url+endpoint)
        
    ### Search functions
    def get_new_awards_over_time(self, start_date, end_date, recipient_id, group="quarter"):
        """
        Returns the count of new awards grouped by time period in ascending order (earliest to most recent).
        
        Args:
        - start_date (str): (YYYY-MM-DD) Currently limited to an earliest date of 2007-10-01 (FY2008). For data going back to 2000-10-01 (FY2001), use either the Custom Award Download feature on the website or one of our download or bulk_download API endpoints.
        - end_date (str): (YYYY-MM-DD) Currently limited to an earliest date of 2007-10-01 (FY2008). For data going back to 2000-10-01 (FY2001), use either the Custom Award Download feature on the website or one of our download or bulk_download API endpoints.
        - recipient_id (str): Optional. A hash of recipient UEI, DUNS, name, and level. A unique identifier for recipients. Defaults to None.
        - group (str): How to group the data. Default is quarter, but other options are fiscal_year and month.
        
        Returns:
        - dict: A dictionary containing a count of new awards.
        """
        data = {
                  "group": group,
                  "filters": {
                      "recipient_id": recipient_id,
                      "time_period": [
                          {
                              "start_date": start_date,
                              "end_date": end_date
                          }
                      ]
                  }
              }
        endpoint = "search/new_awards_over_time/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_award(self, filters, fields, limit=10, order="desc", page=1, sort=None, subawards=False, last_record_unique_id=None, last_record_sort_value=None):
        """
        Returns the fields of the filtered awards.
         
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - fields (list): Spending by award fields to return. See this endpoint's docs for the available fields.
        - limit (int): Number of items to return. Default is 10.
        - order (str): Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order. Default is desc and other option is asc.
        - page (int): Pagination parameter. Defaults to first page.
        - sort (str): Optional parameter indicating what value results should be sorted by. Valid options are any of the fields in the JSON objects in the response. Defaults to the first field provided, but here it defaults to None.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
        - last_record_unique_id (int): Optional. The unique id of the last record in the results set. Used in the experimental Elasticsearch API functionality. Defaults to None.
        - last_record_sort_value (str): Optional. The value of the last record that is being sorted on. Used in the experimental Elasticsearch API functionality. Defaults to None.
        
        Returns:
        - dict: A dictionary containing the fields of the filtered awards.
        """
        data = {
              "subawards": subawards,
              "limit": limit,
              "page": page,
              "order": order,
              "filters": filters,
              "fields": fields
        }
        if sort is not None:
            data["sort"] = sort
        if last_record_unique_id is not None:
            data["last_record_unique_id"] = last_record_unique_id
        if last_record_sort_value is not None:
            data["last_record_sort_value"] = last_record_sort_value
        endpoint = "search/spending_by_award/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_award_count(self, filters, subawards=False):
        """
        Returns the number of awards in each award type (Contracts, Loans, Direct Payments, Grants, Other and IDVs).
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a number of awards.
        """
        data = {"filters": filters,
                "subawards": subawards} 
        endpoint = "search/spending_by_award_count/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_awarding_agency(self, filters, limit=10, page=1, subawards=False):
        """
        Returns a list of the top results of Awarding Agencies sorted by the total amounts in descending order.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - limit (int): Number of items to return. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of the top results of Awarding Agencies sorted by the total amounts in descending order.
        """
        data = {"filters": filters,
                "category": "awarding_agency",
                "subawards": subawards,
                "page": page,
                "limit": limit} 
        endpoint = "search/spending_by_category/awarding_agency/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_awarding_subagency(self, filters, limit=10, page=1, subawards=False):
        """
        Returns a list of the top results of Awarding Subagencies sorted by the total amounts in descending order.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - limit (int): Number of items to return. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of the top results of Awarding Subagencies sorted by the total amounts in descending order.
        """
        data = {"filters": filters,
                "category": "awarding_subagency",
                "subawards": subawards,
                "page": page,
                "limit": limit} 
        endpoint = "search/spending_by_category/awarding_subagency/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_cfda(self, filters, limit=10, page=1, subawards=False):
        """
        Returns a list of the top results of CFDA sorted by the total amounts in descending order.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - limit (int): Number of items to return. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of the top results of CFDA sorted by the total amounts in descending order.
        """
        data = {"filters": filters,
                "category": "cfda",
                "subawards": subawards,
                "page": page,
                "limit": limit} 
        endpoint = "search/spending_by_category/cfda/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_country(self, filters, limit=10, page=1, subawards=False):
        """
        Returns a list of the top results of Countries sorted by the total amounts in descending order.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - limit (int): Number of items to return. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of the top results of Countries sorted by the total amounts in descending order.
        """
        data = {"filters": filters,
                "category": "country",
                "subawards": subawards,
                "page": page,
                "limit": limit} 
        endpoint = "search/spending_by_category/country/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_county(self, filters, limit=10, page=1, subawards=False):
        """
        Returns a list of the top results of Counties sorted by the total amounts in descending order.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - limit (int): Number of items to return. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of the top results of Counties sorted by the total amounts in descending order.
        """
        data = {"filters": filters,
                "category": "county",
                "subawards": subawards,
                "page": page,
                "limit": limit} 
        endpoint = "search/spending_by_category/county/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_district(self, filters, limit=10, page=1, subawards=False):
        """
        Returns a list of the top results of Congressional Districts sorted by the total amounts in descending order.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - limit (int): Number of items to return. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of the top results of Congressional Districts sorted by the total amounts in descending order.
        """
        data = {"filters": filters,
                "category": "district",
                "subawards": subawards,
                "page": page,
                "limit": limit} 
        endpoint = "search/spending_by_category/district/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_federal_account(self, filters, limit=10, page=1, subawards=False):
        """
        Returns a list of the top results of Federal Accounts sorted by the total amounts in descending order.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - limit (int): Number of items to return. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of the top results of Federal Accounts sorted by the total amounts in descending order.
        """
        data = {"filters": filters,
                "category": "federal_account",
                "subawards": subawards,
                "page": page,
                "limit": limit} 
        endpoint = "search/spending_by_category/federal_account/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_funding_agency(self, filters, limit=10, page=1, subawards=False):
        """
        Returns a list of the top results of Funding Agencies sorted by the total amounts in descending order.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - limit (int): Number of items to return. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of the top results of Funding Agencies sorted by the total amounts in descending order.
        """
        data = {"filters": filters,
                "category": "funding_agency",
                "subawards": subawards,
                "page": page,
                "limit": limit} 
        endpoint = "search/spending_by_category/funding_agency/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_funding_subagency(self, filters, limit=10, page=1, subawards=False):
        """
        Returns a list of the top results of Funding Subagencies sorted by the total amounts in descending order.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - limit (int): Number of items to return. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of the top results of Funding Subagencies sorted by the total amounts in descending order.
        """
        data = {"filters": filters,
                "category": "funding_subagency",
                "subawards": subawards,
                "page": page,
                "limit": limit} 
        endpoint = "search/spending_by_category/funding_subagency/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_naics(self, filters, limit=10, page=1, subawards=False):
        """
        Returns a list of the top results of NAICS sorted by the total amounts in descending order.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - limit (int): Number of items to return. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of the top results of NAICS sorted by the total amounts in descending order.
        """
        data = {"filters": filters,
                "category": "naics",
                "subawards": subawards,
                "page": page,
                "limit": limit} 
        endpoint = "search/spending_by_category/naics/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_psc(self, filters, limit=10, page=1, subawards=False):
        """
        Returns a list of the top results of PSC sorted by the total amounts in descending order.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - limit (int): Number of items to return. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of the top results of PSC sorted by the total amounts in descending order.
        """
        data = {"filters": filters,
                "category": "psc",
                "subawards": subawards,
                "page": page,
                "limit": limit} 
        endpoint = "search/spending_by_category/psc/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
    
    # This enpoint doesn't seem to be working  
#    def get_spending_by_recipient(self, filters, limit=10, page=1, subawards=False):
#        """
#        Returns a list of the top results of Recipients sorted by the total amounts in descending order.
#        
#        Args:
#        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
#        - limit (int): Number of items to return. Default is 10.
#        - page (int): Pagination parameter. Defaults to first page.
#        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
#          
#        Returns:
#        - dict: A dictionary containing a list of the top results of Recipients sorted by the total amounts in descending order.
#        """
#        data = {"filters": filters,
#                "category": "recipient",
#                "subawards": subawards,
#                "page": page,
#                "limit": limit} 
#        endpoint = "search/spending_by_category/recipient/"
#        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)

    def get_spending_by_state_territory(self, filters, limit=10, page=1, subawards=False):
        """
        Returns a list of the top results of State Territories sorted by the total amounts in descending order.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - limit (int): Number of items to return. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of the top results of State Territories sorted by the total amounts in descending order.
        """
        data = {"filters": filters,
                "category": "state_territory",
                "subawards": subawards,
                "page": page,
                "limit": limit} 
        endpoint = "search/spending_by_category/state_territory/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_geography(self, filters, scope, geo_layer, geo_layer_filters=None, subawards=False):
        """
        Returns aggregated obligation amounts in different geographic areas. 
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - scope (str): When fetching transactions, use the primary place of performance or recipient location. Options are place_of_performance and recipient_location.
        - geo_layer (str): Set the type of areas in the response. Options are state, county, district, and country.
        - geo_layer_filters (list): Optional. List of U.S. state codes, U.S. county codes, U.S. Congressional districts, or ISO 3166-1 alpha-3 country codes to show results for.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing aggregated obligation amounts in different geographic areas.
        """
        data = {"filters": filters,
                "scope": scope,
                "geo_layer": geo_layer,
                "subawards": subawards} 
        if geo_layer_filters is not None:
            data["geo_layer_filters"] = geo_layer_filters
        endpoint = "search/spending_by_geography/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_transaction(self, filters, fields, limit=10, page=1, sort="Transaction Amount", order="desc"):
        """
        Returns transaction records which match the provided filters. 
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - fields (list): The field names to include in the response.
        - limit (int): The number of results per page. Default is 10.
        - page (int): Pagination parameter. Defaults to first page.
        - sort (str): The field on which to order results in the response. Default is "Transaction Amount"
        - order (str): The direction in which to order results. asc for ascending or desc for descending. Default is desc.
        
        Returns:
        - dict: A dictionary containing transaction records which match the provided filters.   
        """
        data = {"filters": filters,
                "fields": fields,
                "limit": limit,
                "page": page,
                "sort": sort,
                "order": order
                } 
        endpoint = "search/spending_by_transaction/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_by_transaction_count(self, filters):
        """
        Returns counts of transaction records which match the provided filters. 
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
          
        Returns:
        - dict: A dictionary containing counts transaction records which match the provided filters.   
        """
        data = {"filters": filters} 
        endpoint = "search/spending_by_transaction_count/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_spending_over_time(self, filters, group="fiscal_year", subawards=False):
        """
        Returns a list of aggregated award amounts grouped by time period in ascending order (earliest to most recent).   
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
        - group (str): Default is fiscal_year, and other options are quarter and month.
        - subawards (bool): True when you want to group by Subawards instead of Awards. Defaulted to False.
          
        Returns:
        - dict: A dictionary containing a list of aggregated award amounts grouped by time period in ascending order (earliest to most recent).
        """
        data = {"group": group,
                "filters": filters,
                "subawards": subawards} 
        endpoint = "search/spending_over_time/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_transaction_spending_summary(self, filters):
        """
        Returns the high-level aggregations of the counts and dollar amounts for all transactions which match the keyword filter.
        
        Args:
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
          
        Returns:
        - dict: A dictionary containing the high-level aggregations of the counts and dollar amounts for all transactions which match the keyword filter.
        """
        data = {"filters": filters} 
        endpoint = "search/transaction_spending_summary/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
    
    # Spending Explorer    
    def explore_spending(self, Type, filters):
        """
        Returns spending data information through various types of filters.
        
        Args:
        - Type (str): Options are federal_account, object_class, recipient, award, budget_function, budget_subfunction, agency, and program_activity.   
        - filters (dict): An advanced JSON search object. See this endpoint's docs for the format of this object.
          
        Returns:
        - dict: A dictionary containing spending data information through various types of filters.
        """ 
        data = {"type": Type,
                "filters": filters
                } 
        endpoint = "spending/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
    
    # Subawards    
    def get_subawards(self, sort, page=1, limit=10, order="desc", award_id=None):
        """
        Returns a filtered set of subawards.
        
        Args:
        - sort (str): Required sorting parameter. Options are subaward_number, id, description, action_date, amount, recipient_name.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of items per page. Default is 10.
        - order (str): Ordering parameter. Default is desc (descending) and other option is asc (ascending).
        - award_id (str): Optional. Either a "generated" natural award id (string) or a database surrogate award id (number). Generated award identifiers are preferred as they are effectively permanent. Surrogate award ids are retained for backward compatibility but are deprecated.
        
        Returns:
        - dict: A dictionary containing a filtered set of subawards.
        """ 
        data = {"sort": sort,
                "page": page,
                "limit": limit,
                "order": order
                } 
        if award_id is not None:
            data["award_id"] = award_id
        endpoint = "subawards/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
        
    def get_transactions(self, award_id, sort="action_date", page=1, limit=10, order="desc"):
        """
        Returns a list of transactions, their amount, type, action date, action type, modification number, and description.
        
        Args:
        - award_id (str): Either a "generated" natural award id (string) or a database surrogate award id (number). Generated award identifiers are preferred as they are effectively permanent. Surrogate award ids are retained for backward compatibility but are deprecated.
        - sort (str): The field results are sorted by. Default is action_date, but other options are modification_number, federal_action_obligation, face_value_loan_guarantee, original_loan_subsidy_cost, action_type_description, and description.
        - page (int): Pagination parameter. Defaults to first page.
        - limit (int): Number of items per page. Default is 10. Max is 5000.
        - order (str): Ordering parameter. Default is desc (descending) and other option is asc (ascending).
         
        Returns:
        - dict: A dictionary containing a list of transactions, their amount, type, action date, action type, modification number, and description.
        """
        data = {"award_id": award_id,
                "sort": sort,
                "page": page,
                "limit": limit,
                "order": order
                } 
        endpoint = "transactions/"
        return mr.make_request_with_post_and_json(self.base_url+endpoint, json=data)
  
  
  
  
   
  
  
  
   
  
   
   
   
   
   
   
   
   
   
   
   
 
   
   
  
   
   
   
   
  
   
  
   
    
   
    
 
        
    
        
    
   
 
  
 
  
  
        

    
 
   
 
   
    
  
   
    
        
 
 
 
 
 
 
        
 
    
    
  
  
  
  
  
  
   
   
   
   
        
  
        
    
        
              
        
  
  
        
    
 
        
            
       
    
 
   
     
   
    
    
   
   
   
    
     
       
        
        
  
  
  
  
  
  
  
  
  
    
   
   
   
   
  
   
   
     
    
     
     
   
  
  
  
  
  
  
  
  
   
 
   
        
        
        
                    
                    
    
  
  
    
      
  
  
 
 
 
  
  
   
   
   
   
        
    
        
    
  
       
       
       
        
        