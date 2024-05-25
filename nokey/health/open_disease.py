import requests_cache
from .. helperFuncs import make_request as mr

class OpenDisease:
    """
    A class for interacting with the Open Disease API.
    
    Attributes:
    - base_url: The base URL for the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="open_disease_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://disease.sh/v3/"
        self.about = "Open Disease is a Third Party API for reliable global disease information, serving COVID and influenza data (Note: None of the data in this API seems to be up to date)"
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Open Disease API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://disease.sh/docs/"
        
    # COVID WORLDOMETERS
    def get_worldometers_global_covid_data(self, day=0, allow_null=False):
        """
        Returns global COVID-19 totals for today, yesterday and two days ago.
        
        Args:
        - day (int): Which day's data to return. Supported values are 0 for today, 1 for yesterday, and 2 for the day before yesterday. Default is 0, today.
        - allow_null (bool): True if, where the value is 0, null is instead retired. Default is False.
        
        Returns:
        - dict: A dictionary containing global COVID-19 totals.
        """
        if day == 0:
            endpoint = f"covid-19/all?allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        elif day == 1:
            endpoint = f"covid-19/all?yesterday=true&allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        elif day == 2:
            endpoint = f"covid-19/all?twoDaysAgo=true&allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        else:
            print("Value of day must be 0, 1, or 2, for today, yesterday, or the day before yesterday, respectively.")
            exit()
            
    def get_worldometers_covid_data_for_all_states(self, sort=None, day=0, allow_null=False):
        """
        Returns COVID-19 totals for the states.
        
        Args:
        - sort (str): Provided a key (e.g. cases, todayCases, deaths, active), result will be sorted from greatest to least. See docs for possible fields to sort by. Default is None.
        - day (int): Which day's data to return. Supported values are 0 for today and 1 for yesterday. Default is 0, today.
        - allow_null (bool): True if, where the value is 0, null is instead retired. Default is False.
        
        Returns:
        - dict: A dictionary containing state COVID-19 totals.
        """
        if sort is not None:
            if day == 0:
                endpoint = f"covid-19/states?sort={sort}&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            elif day == 1:
                endpoint = f"covid-19/states?sort={sort}&yesterday=true&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            else:
                print("Value of day must be 0 or 1, for today or yesterday, respectively.")
                exit()
        else:
            if day == 0:
                endpoint = f"covid-19/states?allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            elif day == 1:
                endpoint = f"covid-19/states?yesterday=true&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            else:
                print("Value of day must be 0 or 1, for today or yesterday, respectively.")
                exit()
                
    def get_worldometers_covid_data_for_specific_states(self, states, day=0, allow_null=False):
        """
        Returns COVID-19 totals for the specified state(s).
        
        Args:
        - states (str): State name or comma separated non-spaced names, spelled correctly.
        - day (int): Which day's data to return. Supported values are 0 for today and 1 for yesterday. Default is 0, today.
        - allow_null (bool): True if, where the value is 0, null is instead retired. Default is False.
        
        Returns:
        - dict: A dictionary containing COVID-19 totals for specified state(s).
        """
        if day == 0:
            endpoint = f"covid-19/states/{states}?allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        elif day == 1:
            endpoint = f"covid-19/states/{states}?yesterday=true&allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        else:
            print("Value of day must be 0 or 1, for today or yesterday, respectively.")
            exit()
            
    def get_worldometers_covid_data_for_all_continents(self, sort=None, day=0, allow_null=False):
        """
        Returns COVID-19 totals for all the continents.
        
        Args:
        - sort (str): Provided a key (e.g. cases, todayCases, deaths, active), result will be sorted from greatest to least. See docs for possible fields to sort by. Default is None.
        - day (int): Which day's data to return. Supported values are 0 for today, 1 for yesterday, and 2 for the day before yesterday. Default is 0, today.
        - allow_null (bool): True if, where the value is 0, null is instead retired. Default is False.
        
        Returns:
        - dict: A dictionary containing COVID-19 totals for the continents.
        """
        if sort is not None:
            if day == 0:
                endpoint = f"covid-19/continents?sort={sort}&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            elif day == 1:
                endpoint = f"covid-19/continents?sort={sort}&yesterday=true&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            elif day == 2:
                endpoint = f"covid-19/continents?twoDaysAgo=true&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)     
            else:
                print("Value of day must be 0, 1, or 2, for today, yesterday, or the day before yesterday, respectively.")
                exit()
        else:
            if day == 0:
                endpoint = f"covid-19/continents?allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            elif day == 1:
                endpoint = f"covid-19/continents?yesterday=true&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            elif day == 2:
                endpoint = f"covid-19/continents?twoDaysAgo=true&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            else:
                print("Value of day must be 0, 1, or 2, for today, yesterday, or the day before yesterday, respectively.")
                exit()
                
    def get_worldometers_covid_data_for_specific_continent(self, continent, day=0, strict=True, allow_null=False):
        """
        Returns COVID-19 totals for the specified continent.
        
        Args:
        - continent (str): Name of the continent, spelled correctly.
        - day (int): Which day's data to return. Supported values are 0 for today, 1 for yesterday, and 2 for the day before yesterday. Default is 0, today.
        - strict (bool): Setting to false gives you the ability to fuzzy search continents (i.e. Oman vs. rOMANia). Default is True.
        - allow_null (bool): True if, where the value is 0, null is instead retired. Default is False.
        
        Returns:
        - dict: A dictionary containing COVID-19 totals for specified continent.
        """
        if day == 0:
            endpoint = f"covid-19/continents/{continent}?strict={str(strict).lower()}&allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        elif day == 1:
            endpoint = f"covid-19/continents/{continent}?yesterday=true&strict={str(strict).lower()}&allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        elif day == 2:
            endpoint = f"covid-19/continents{continent}?twoDaysAgo=true&strict={str(strict).lower()}&allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        else:
            print("Value of day must be 0, 1, or 2, for today, yesterday, or the day before yesterday, respectively.")
            exit()
            
    def get_worldometers_covid_data_for_all_countries(self, sort=None, day=0, allow_null=False):
        """
        Returns COVID-19 totals for all the countries.
        
        Args:
        - sort (str): Provided a key (e.g. cases, todayCases, deaths, active), result will be sorted from greatest to least. See docs for possible fields to sort by. Default is None.
        - day (int): Which day's data to return. Supported values are 0 for today and 1 for yesterday. Default is 0, today.
        - allow_null (bool): True if, where the value is 0, null is instead retired. Default is False.
        
        Returns:
        - dict: A dictionary containing COVID-19 totals for the countries.
        """
        if sort is not None:
            if day == 0:
                endpoint = f"covid-19/countries?sort={sort}&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            elif day == 1:
                endpoint = f"covid-19/countries?sort={sort}&yesterday=true&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            elif day == 2:
                endpoint = f"covid-19/countries?twoDaysAgo=true&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            else:
                print("Value of day must be 0, 1, or 2, for today, yesterday, or the day before yesterday, respectively.")
                exit()
        else:
            if day == 0:
                endpoint = f"covid-19/countries?allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            elif day == 1:
                endpoint = f"covid-19/countries?yesterday=true&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            elif day == 2:
                endpoint = f"covid-19/countries?twoDaysAgo=true&allowNull={str(allow_null).lower()}"
                return mr.make_request(self.base_url+endpoint)
            else:
                print("Value of day must be 0, 1, or 2, for today, yesterday, or the day before yesterday, respectively.")
                exit()
                
    def get_worldometers_covid_data_for_specific_country(self, country, day=0, strict=True, allow_null=False):
        """
        Returns COVID-19 totals for the specified country.
        
        Args:
        - country (str): A country name, iso2, iso3, or country ID code
        - day (int): Which day's data to return. Supported values are 0 for today, 1 for yesterday, and 2 for the day before yesterday. Default is 0, today.
        - strict (bool): Setting to false gives you the ability to fuzzy search countries (i.e. Oman vs. rOMANia). Default is True.
        - allow_null (bool): True if, where the value is 0, null is instead retired. Default is False.
        
        Returns:
        - dict: A dictionary containing COVID-19 totals for specified country.
        """
        if day == 0:
            endpoint = f"covid-19/countries/{country}?strict={str(strict).lower()}&allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        elif day == 1:
            endpoint = f"covid-19/countries/{country}?yesterday=true&strict={str(strict).lower()}&allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        elif day == 2:
            endpoint = f"covid-19/countries{country}?twoDaysAgo=true&strict={str(strict).lower()}&allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        else:
            print("Value of day must be 0, 1, or 2, for today, yesterday, or the day before yesterday, respectively.")
            exit()
            
    def get_worldometers_covid_data_for_specific_countries(self, countries, day=0, strict=True, allow_null=False):
        """
        Returns COVID-19 totals for the specified countries.
        
        Args:
        - countries (str): Multiple country names, iso2s, iso3s, or country ID codes, separated by commas, non spaces.
        - day (int): Which day's data to return. Supported values are 0 for today, 1 for yesterday, and 2 for the day before yesterday. Default is 0, today.
        - strict (bool): Setting to false gives you the ability to fuzzy search countries (i.e. Oman vs. rOMANia). Default is True.
        - allow_null (bool): True if, where the value is 0, null is instead retired. Default is False.
        
        Returns:
        - dict: A dictionary containing COVID-19 totals for specified countries.
        """
        if day == 0:
            endpoint = f"covid-19/countries/{countries}?strict={str(strict).lower()}&allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        elif day == 1:
            endpoint = f"covid-19/countries/{countries}?yesterday=true&strict={str(strict).lower()}&allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        elif day == 2:
            endpoint = f"covid-19/countries{countries}?twoDaysAgo=true&strict={str(strict).lower()}&allowNull={str(allow_null).lower()}"
            return mr.make_request(self.base_url+endpoint)
        else:
            print("Value of day must be 0, 1, or 2, for today, yesterday, or the day before yesterday, respectively.")
            exit()
            
            
    # JHUCSSE (Johns Hopkins University) COVID data
    # This data doesn't seem to be current. It seems to end at 3/9/23.
    def get_jhu_global_time_series_covid_data(self, last_days=30):
        """
        Returns COVID-19 time series data for all countries and all their provences.
        
        Args:
        - last_days (int, str): Number of days' data to return. Use 'all' to return all data. Default is 30.
        
        Returns:
        - dict: A dictionary containing COVID-19 time series data.
        """
        endpoint = f"covid-19/historical?lastdays={last_days}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_jhu_global_accumulated_covid_data(self, last_days=30):
        """
        Returns global accumulated COVID-19 time series data for all countries and all their provences.
        
        Args:
        - last_days (int, str): Number of days' data to return. Use 'all' to return all data. Default is 30.
        
        Returns:
        - dict: A dictionary containing global accumulated COVID-19 time series data.
        """
        endpoint = f"covid-19/historical/all?lastdays={last_days}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_jhu_time_series_covid_data_for_country(self, country, last_days=30):
        """
        Returns COVID-19 time series data for a specific country.
        
        Args:
        - country (str): A country name, iso2, iso3, or country ID code.
        - last_days (int, str): Number of days' data to return. Use 'all' to return all data. Default is 30.
        
        Returns:
        - dict: A dictionary containing COVID-19 time series data.
        """
        endpoint = f"covid-19/historical/{country}?lastdays={last_days}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_jhu_time_series_covid_data_for_countries(self, countries, last_days=30):
        """
        Returns COVID-19 time series data for a specific countries.
        
        Args:
        - country (str): Multiple country names, iso2s, iso3s, or country ID codes, in comma separated no spaced string.
        - last_days (int, str): Number of days' data to return. Use 'all' to return all data. Default is 30.
        
        Returns:
        - dict: A dictionary containing COVID-19 time series data.
        """
        endpoint = f"covid-19/historical/{countries}?lastdays={last_days}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_jhu_time_series_covid_data_for_province(self, province, country, last_days=30):
        """
        Returns COVID-19 time series data for a specific province in a country.
        
        Args:
        - country (str): A country name, iso2, iso3, or country ID code.
        - province (str): Province name. All available names can be found in the /v3/covid-19/historical/{query} endpoint.
        - last_days (int, str): Number of days' data to return. Use 'all' to return all data. Default is 30.
        
        Returns:
        - dict: A dictionary containing COVID-19 time series data.
        """
        endpoint = f"covid-19/historical/{country}/{province}?lastdays={last_days}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_jhu_time_series_covid_data_for_provinces(self, provinces, country, last_days=30):
        """
        Returns COVID-19 time series data for a specific set of provinces in a country.
        
        Args:
        - country (str): A country name, iso2, iso3, or country ID code.
        - province (str): Provinces spelled correctly separated by ',' or '|' delimiters, never both in the same query.
        - last_days (int, str): Number of days' data to return. Use 'all' to return all data. Default is 30.
        
        Returns:
        - dict: A dictionary containing COVID-19 time series data.
        """
        endpoint = f"covid-19/historical/{country}/{provinces}?lastdays={last_days}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_all_us_states_jhu(self):
        """
        Returns all possible US States and provinces to query the /historical/usacounties/{state} endpoint with.
        
        Args:
        - None
        
        Returns:
        - list: A list containing all US states and provinces.
        """
        endpoint = "covid-19/historical/usacounties"
        return mr.make_request(self.base_url+endpoint)
        
    def get_jhu_time_series_covid_data_for_state(self, state, last_days=30):
        """
        Returns COVID-19 time series data for all counties in a specific state.
        
        Args:
        - state (str): US state name, validated in the array returned from the /v3/covid-19/historical/usacounties endpoint.
        - last_days (int, str): Number of days' data to return. Use 'all' to return all data. Default is 30.
        
        Returns:
        - dict: A dictionary containing COVID-19 time series data.
        """
        endpoint = f"covid-19/historical/usacounties/{state.lower()}?lastdays={last_days}"
        return mr.make_request(self.base_url+endpoint)
        
    # NEW YORK TIMES (NYT) COVID DATA (This doesn't seem up to date. Last date seems to be 2/23/23)
    def get_nyt_time_series_covid_data_for_all_states(self, last_days=30):
        """
        Returns COVID-19 time series data for all states, with an entry for each day since the pandemic began.
        
        Args:
        - last_days (int, str): Number of days' data to return. Use 'all' to return all data. Default is 30.
        
        Returns:
        - dict: A dictionary containing COVID-19 time series data.
        """
        endpoint = f"covid-19/nyt/states/?lastdays={last_days}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_nyt_time_series_covid_data_for_specific_states(self, states, last_days=30):
        """
        Returns COVID-19 time series data for specific state(s), with an entry for each day since the pandemic began.
        
        Args:
        - states (str): State name(s), separated by commas (e.g. 'Illinois, California').
        - last_days (int, str): Number of days' data to return. Use 'all' to return all data. Default is 30.
        
        Returns:
        - dict: A dictionary containing COVID-19 time series data.
        """
        endpoint = f"covid-19/nyt/states/{states}?lastdays={last_days}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_nyt_time_series_covid_data_for_all_us_counties(self, last_days=30):
        """
        Returns COVID-19 time series data for all available US counties, with an entry for each day since the pandemic began.
        
        Args:
        - last_days (int, str): Number of days' data to return. Use 'all' to return all data. Default is 30.
        
        Returns:
        - dict: A dictionary containing COVID-19 time series data.
        """
        endpoint = f"covid-19/nyt/counties/?lastdays={last_days}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_nyt_time_series_covid_data_for_specific_us_counties(self, counties, last_days=30):
        """
        Returns COVID-19 time series data for specific state(s), with an entry for each day since the pandemic began.
        
        Args:
        - states (str): County name(s), separated by commas (e.g. 'Alameda, Humboldt').
        - last_days (int, str): Number of days' data to return. Use 'all' to return all data. Default is 30.
        
        Returns:
        - dict: A dictionary containing COVID-19 time series data.
        """
        endpoint = f"covid-19/nyt/counties/{counties}?lastdays={last_days}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_nyt_time_series_covid_data_for_entire_usa(self):
        """
        Returns COVID-19 time series data for entire USA, with an entry for each day since the pandemic began.
        
        Args:
        - None 
        Returns:
        - dict: A dictionary containing COVID-19 time series data.
        """
        endpoint = "covid-19/nyt/usa"
        return mr.make_request(self.base_url+endpoint)
        
        
    # APPLE COVID-19 DATA (COVID-19 related mobility trend data from Apple). This data is also not current. It goes up to 4/12/22.
    def get_all_countries_apple(self):
        """
        Returns a list of supported country names.
        
        Args:
        - None
        
        Returns:
        - list: A list containing supported country names.
        """
        endpoint = "covid-19/apple/countries"
        return mr.make_request(self.base_url+endpoint)
        
    def get_apple_supported_subregions_for_country(self, country):
        """
        Returns a list of supported subregions in a country where data is available.
        
        Args:
        - country (str): A valid country name from the /v3/covid-19/apple/countries endpoint
        
        Returns:
        - dict: A dictionary containing a list of supported subregions.
        """
        endpoint = f"covid-19/apple/countries/{country}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_apple_mobility_data_for_subregions(self, country, subregions):
        """
        Returns a list of mobility data entries for subregion(s) every day since January 13th. Each entry has driving, transit, and walking data with an associated number of percentage change since January 13th. 
        
        Args:
        - country (str): A valid country name from the /v3/covid-19/apple/countries endpoint.
        - subregions (str): Valid subregion(s) from the /v3/covid-19/apple/countries/{country} endpoint, separated by with commas.
        
        Returns:
        - dict: A dictionary containing a list of mobility data.
        """
        endpoint = f"covid-19/apple/countries/{country}/{subregions}"
        return mr.make_request(self.base_url+endpoint)
        
        
    # GOVERNMENT COVID-19 DATA. (Data not current. It stops at 12/1/23)
    def get_all_countries_gov(self):
        """
        Returns a list of supported country names for government specific data.
        
        Args:
        - None
        
        Returns:
        - list: A list containing supported country names.
        """
        endpoint = "covid-19/gov"
        return mr.make_request(self.base_url+endpoint)
        
    def get_gov_covid_data_for_country(self, country, allow_null=False):
        """
        Returns government supported data for a specific country.
        
        Args:
        - country (str): A valid country name from the /v3/covid-19/gov endpoint.
        - allow_null (bool): By default, if a value is missing, it is returned as 0. This allows nulls to be returned.
        
        Returns:
        - dict: A dictionary containing a list of supported subregions.
        """
        endpoint = f"covid-19/gov/{country}?allowNull={str(allow_null).lower()}"
        return mr.make_request(self.base_url+endpoint)
        
        
    # VACCINE TRIAL DATA (RAPS - Regulatory Affairs Professional Society) (The dates of the data are current, but the data itself is not)
    #This endpoint doesn't seem to be working.
#    def get_raps_covid_vaccine_trial_data(self):
#        """
#        Returns vaccine trial data from RAPS.
#        
#        Args:
#        - None
#        
#        Returns:
#        - dict: A dictionary containing vaccine trial data.
#        """
#        endpoint = "covid-19/vaccine"
#        return mr.make_request(self.base_url+endpoint)

    def get_raps_total_covid_vaccines_administered(self, last_days=30, full_data=False):
        """
        Returns total global COVID-19 vaccine doses administered. Sourced from https://covid.ourworldindata.org.
        
        Args:
        - last_data (int, str): Number of days to return. Use 'all' for the full data set (e.g. 15, all, 24
        - full_data (bool): Flag indicating whether to return data type as simpleVaccineTimeline (false) or fullVaccineTimeline (true). 
        
        Returns:
        - dict: A dictionary containing vaccine administration data.
        """
        endpoint = f"covid-19/vaccine/coverage?lastdays={last_days}&fullData={str(full_data).lower()}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_raps_covid_vaccines_administered_for_all_countries(self, last_days=30, full_data=False):
        """
        Returns Get COVID-19 vaccine doses administered for all countries that have reported rolling out vaccination. Sourced from https://covid.ourworldindata.org/
        
        Args:
        - last_data (int, str): Number of days to return. Use 'all' for the full data set (e.g. 15, all, 24
        - full_data (bool): Flag indicating whether to return data type as simpleVaccineTimeline (false) or fullVaccineTimeline (true). 
        
        Returns:
        - dict: A dictionary containing vaccine administration data.
        """
        endpoint = f"covid-19/vaccine/coverage/countries?lastdays={last_days}&fullData={str(full_data).lower()}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_raps_covid_vaccines_administered_for_country(self, country, last_days=30, full_data=False):
        """
        Returns Get COVID-19 vaccine doses administered for any country that has reported rolling out vaccination. Sourced from https://covid.ourworldindata.org/
        
        Args:
        - country (str): A valid country name, iso2, iso3.
        - last_data (int, str): Number of days to return. Use 'all' for the full data set (e.g. 15, all, 24
        - full_data (bool): Flag indicating whether to return data type as simpleVaccineTimeline (false) or fullVaccineTimeline (true). 
        
        Returns:
        - dict: A dictionary containing vaccine administration data.
        """
        endpoint = f"covid-19/vaccine/coverage/countries/{country}?lastdays={last_days}&fullData={str(full_data).lower()}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_raps_covid_vaccines_administered_for_all_states(self, last_days=30, full_data=False):
        """
        Returns Get COVID-19 vaccine doses administered for all states that have reported rolling out vaccination. Sourced from https://covid.ourworldindata.org/
        
        Args:
        - last_data (int, str): Number of days to return. Use 'all' for the full data set (e.g. 15, all, 24
        - full_data (bool): Flag indicating whether to return data type as simpleVaccineTimeline (false) or fullVaccineTimeline (true). 
        
        Returns:
        - dict: A dictionary containing vaccine administration data.
        """
        endpoint = f"covid-19/vaccine/coverage/states?lastdays={last_days}&fullData={str(full_data).lower()}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_raps_covid_vaccines_administered_for_state(self, state, last_days=30, full_data=False):
        """
        Returns Get COVID-19 vaccine doses administered for any state that has reported rolling out vaccination. Sourced from https://covid.ourworldindata.org/
        
        Args:
        - country (str): A valid state name
        - last_data (int, str): Number of days to return. Use 'all' for the full data set (e.g. 15, all, 24
        - full_data (bool): Flag indicating whether to return data type as simpleVaccineTimeline (false) or fullVaccineTimeline (true). 
        
        Returns:
        - dict: A dictionary containing vaccine administration data.
        """
        endpoint = f"covid-19/vaccine/coverage/states/{state}?lastdays={last_days}&fullData={str(full_data).lower()}"
        return mr.make_request(self.base_url+endpoint)
        
    # THERAPEUTICS (from RAPS)
    # This endpoint doesn't seem to be working.
#    def get_covid_therapeutics_data(self):
#        """
#        Returns therapeutics trial data from RAPS (Regulatory Affairs Professional Society). Specifically published by Jeff Craven at https://www.raps.org/news-and-articles/news-articles/2020/3/covid-19-therapeutics-tracker.
#        
#        Args:
#        - None
#        
#        Returns:
#        - dict: A dictionary containing therapeutics trial data.
#        """
#        endpoint = "covid-19/therapeutics"
#        return mr.make_request(self.base_url+endpoint)

    
    # VARIANTS (COVID-19 data from The European Surveillance System -TESSy, provided by [Austria, Belgium, Bulgaria, Croatia, Cyprus, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain and Sweden] https://www.ecdc.europa.eu and released by ECDC updated every week)
    def get_all_countries_ecdc(self):
        """
        Returns a list of supported country names.
        
        Args:
        - None
        
        Returns:
        - list: A list containing supported country names.
        """
        endpoint = "covid-19/variants/countries"
        return mr.make_request(self.base_url+endpoint)
        
    def get_ecdc_covid_variant_data_for_country(self, country):
        """
        Returns COVID-19 ECDC reported data for a specific country. 
        
        Args:
        - country (str): A valid country name from the /v3/covid-19/variants/countries/ endpoint
        
        Returns:
        - dict: A dictionary containing covid data.
        """
        endpoint = f"covid-19/variants/countries/{country}"
        return mr.make_request(self.base_url+endpoint)
   
   
  
   
   
    
    
    
 
  
    
 
 
 
    
   
  
 
  
  
    
  
 
 
  
    
  
        
     
        
    
       
  
    
      
  
   
        