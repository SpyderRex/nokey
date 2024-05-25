import requests_cache
from .. helperFuncs import make_request as mr


class NationalWeatherService:
    """
    A class to interact with the National Weather Service API.
    
    Attributes:
    - base_url: The base URL of the National Weather Service API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="nws_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://api.weather.gov/"
        self.about = "The National Weather Service (NWS) API allows developers access to critical forecasts, alerts, and observations, along with other weather data."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns URL for API docs.
        
        Args:
        - None
        
        Returns:
        - string: URL for API documentation.
        """
        return "https://www.weather.gov/documentation/services-web-api"       
    
    def get_alerts(self):
        """
        Returns a collection of weather alerts.

        Args:
        - None

        Returns:
        - dict: Inforation on weather alerts
        """
        endpoint = "alerts"
        return mr.make_request(self.base_url+endpoint)
        
    def get_active_alerts(self):
        """
        Returns a collection of currently active weather alerts.

        Args:
        - None

        Returns:
        - dict: Inforation on currently active weather alerts
        """
        endpoint = "alerts/active"
        return mr.make_request(self.base_url+endpoint)
        
    def get_active_alerts_count(self):
        """
        Returns the count of currently active weather alerts broken down by various categories.

        Args:
        - None

        Returns:
        - dict: Count of currently active weather alerts broke down by categories.
        """
        endpoint = "alerts/active/count"
        return mr.make_request(self.base_url+endpoint)
        
    def get_active_alerts_by_zone(self, zoneID):
        """
        Returns active alerts for the given NWS public zone or county.
        
        Args:
        - zoneID (str): NWS public zone/county identifier
        
        Returns:
        - dict: Information of active alerts in the zone specified by zoneID.
        """
        endpoint = f"alerts/active/zone/{zoneID}"
        return mr.make_request(self.base_url+endpoint)
    
    def get_active_alerts_by_area(self, area):
        """
        Returns active alerts for the given area (state or marine area).
        
        Args:
        - area (str): State or marine area ID
        
        Returns:
        - dict: Information of active alerts in the area specified.
        """
        endpoint = f"alerts/active/area/{area}"
        return mr.make_request(self.base_url+endpoint)
    
    def get_active_alerts_by_region(self, region):
        """
        Returns active alerts for the given marine region ID. Available values : AL, AT, GL, GM, PA, PI."
        
        Args:
        - region (str): Marine region ID. Available values : AL, AT, GL, GM, PA, PI.
        
        Returns:
        - dict: Information of active alerts in the area specified.
        """
        endpoint = f"alerts/active/region/{region}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_alert_types(self):
        """
        Returns a list of alerts types.

        Args:
        - None

        Returns:
        - dict: A dictionary containing a list of alert types.
        """
        endpoint = "alerts/types"
        return mr.make_request(self.base_url+endpoint)
        
    def get_alert_by_id(self, ID):
        """
        Returns a specific alert record.

        Args:
        - ID (str): Alert identifier.

        Returns:
        - dict: A dictionary containing information about a specific alert.
        """
        endpoint = f"alerts/{ID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_cwsu_metadata(self, cwsuID):
        """
        Returns metadata about a Center Weather Service Unit.

        Args:
        - cwsuID (str): NWS CWSU ID. Available values : ZAB, ZAN, ZAU, ZBW, ZDC, ZDV, ZFA, ZFW, ZHU, ZID, ZJX, ZKC, ZLA, ZLC, ZMA, ZME, ZMP, ZNY, ZOA, ZOB, ZSE, ZTL.

        Returns:
        - dict: Metadata about a cwsu.
        """
        endpoint = f"aviation/cwsus/{cwsuID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_cwsu_advisories(self, cwsuID):
        """
        Returns a list of Center Weather Advisories from a CWSU.

        Args:
        - cwsuID (str): NWS CWSU ID. Available values : ZAB, ZAN, ZAU, ZBW, ZDC, ZDV, ZFA, ZFW, ZHU, ZID, ZJX, ZKC, ZLA, ZLC, ZMA, ZME, ZMP, ZNY, ZOA, ZOB, ZSE, ZTL.

        Returns:
        - dict: Dictionary containing list of  Center Weather Advisories from a CWSU.
        """
        endpoint = f"aviation/cwsus/{cwsuID}/cwas"
        return mr.make_request(self.base_url+endpoint)
    
    def get_cwsu_advisories_by_date_and_seq(self, cwsuID, date, sequence):
        """
        Returns a list of Center Weather Advisories from a CWSU.

        Args:
        - cwsuID (str): NWS CWSU ID. Available values : ZAB, ZAN, ZAU, ZBW, ZDC, ZDV, ZFA, ZFW, ZHU, ZID, ZJX, ZKC, ZLA, ZLC, ZMA, ZME, ZMP, ZNY, ZOA, ZOB, ZSE, ZTL.
        - date (str): (YYYY-MM-DD format) Date of advisory.
        - sequence (int): Sequence number
        
        Returns:
        - dict: Dictionary containing list of Center Weather Advisories from a CWSU.
        """
        endpoint = f"aviation/cwsus/{cwsuID}/cwas/{date}/{sequence}"
        return mr.make_request(self.base_url+endpoint)

# DON'T YET KNOW HOW THIS WORKS. ARGS ARE QUERIES, NOT PATHS      
#    def get_sigmets(self, start_time, end_time, date, atsu, sequence):
#        """
#        Returns a list of SIGMET/AIRMETs.
#
#        Args:
#        - start_time (str): Start time.
#        - end_time (str): End time.
#        - date (str): (YYYY-MM-DD format) Date
#        - atsu (str): ATSU identifier
#        - sequence (str): SIGMET sequence number
#
#        Returns:
#        - dict: Metadata about a cwsu.
#        """
#        endpoint = f"aviation/sigmet?{start_time}?{end_time}?{date}?{atsu}?{sequence}"
#        return mr.make_request(self.base_url+endpoint)

    def get_sigmets_by_atsu(self, atsu):
        """
        Returns a list of SIGMET/AIRMETs for the specified ATSU.

        Args:
        - atsu (str): ATSU identifier.
        
        Returns:
        - dict: Dictionary containing list of SIGMET/AIRMETs for the specified ATSU.
        """
        endpoint = f"aviation/sigmets/{atsu}"
        return mr.make_request(self.base_url+endpoint)

    def get_sigmets_by_atsu_and_date(self, atsu, date):
        """
        Returns a list of SIGMET/AIRMETs for the specified ATSU for the specified date.

        Args:
        - atsu (str): ATSU identifier.
        - date (str): Date (YYYY-MM-DD format)
        
        Returns:
        - dict: Dictionary containing list of SIGMET/AIRMETs for the specified ATSU and specified date.
        """
        endpoint = f"aviation/sigmets/{atsu}/{date}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_specific_sigmet(self, atsu, date, time):
        """
        Returns a list of SIGMET/AIRMETs for the specified ATSU for the specified date.

        Args:
        - atsu (str): ATSU identifier.
        - date (str): Date (YYYY-MM-DD format)
        - time (str): Time (HHMM format). This time is always specified in UTC (Zulu) time.
        
        Returns:
        - dict: Dictionary containing a specific SIGMET/AIRMET.
        """
        endpoint = f"aviation/sigmets/{atsu}/{date}/{time}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_glossary(self):
        """
        Returns glossary terms.

        Args:
        - None

        Returns:
        - dict: A dictionary containing a list of glossary terms and definitions.
        """
        endpoint = "glossary"
        return mr.make_request(self.base_url+endpoint)
        
    def get_raw_data_by_gridpoints(self, wfo, x, y):
        """
        Returns raw numerical forecast data for a 2.5km grid area.

        Args:
        - wfo (str): Forecast office ID. Available values : AKQ, ALY, BGM, BOX, BTV, BUF, CAE, CAR, CHS, CLE, CTP, GSP, GYX, ILM, ILN, LWX, MHX, OKX, PBZ, PHI, RAH, RLX, RNK, ABQ, AMA, BMX, BRO, CRP, EPZ, EWX, FFC, FWD, HGX, HUN, JAN, JAX, KEY, LCH, LIX, LUB, LZK, MAF, MEG, MFL, MLB, MOB, MRX, OHX, OUN, SHV, SJT, SJU, TAE, TBW, TSA, ABR, APX, ARX, BIS, BOU, CYS, DDC, DLH, DMX, DTX, DVN, EAX, FGF, FSD, GID, GJT, GLD, GRB, GRR, ICT, ILX, IND, IWX, JKL, LBF, LMK, LOT, LSX, MKX, MPX, MQT, OAX, PAH, PUB, RIW, SGF, TOP, UNR, BOI, BYZ, EKA, FGZ, GGW, HNX, LKN, LOX, MFR, MSO, MTR, OTX, PDT, PIH, PQR, PSR, REV, SEW, SGX, SLC, STO, TFX, TWC, VEF, AER, AFC, AFG, AJK, ALU, GUM, HPA, HFO, PPG, STU, NH1, NH2, ONA, ONP
        - x (int): Forecast grid X coordinate.
        - y (int): Forecast grid Y coordinate.
        
        Returns:
        - dict: Dictionary containing the raw numerical forcast data.
        """
        endpoint = f"gridpoints/{wfo}/{x},{y}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_textual_forecast_by_gridpoints(self, wfo, x, y):
        """
        Returns a textual forecast for a 2.5km grid area.

        Args:
        - wfo (str): Forecast office ID. Available values : AKQ, ALY, BGM, BOX, BTV, BUF, CAE, CAR, CHS, CLE, CTP, GSP, GYX, ILM, ILN, LWX, MHX, OKX, PBZ, PHI, RAH, RLX, RNK, ABQ, AMA, BMX, BRO, CRP, EPZ, EWX, FFC, FWD, HGX, HUN, JAN, JAX, KEY, LCH, LIX, LUB, LZK, MAF, MEG, MFL, MLB, MOB, MRX, OHX, OUN, SHV, SJT, SJU, TAE, TBW, TSA, ABR, APX, ARX, BIS, BOU, CYS, DDC, DLH, DMX, DTX, DVN, EAX, FGF, FSD, GID, GJT, GLD, GRB, GRR, ICT, ILX, IND, IWX, JKL, LBF, LMK, LOT, LSX, MKX, MPX, MQT, OAX, PAH, PUB, RIW, SGF, TOP, UNR, BOI, BYZ, EKA, FGZ, GGW, HNX, LKN, LOX, MFR, MSO, MTR, OTX, PDT, PIH, PQR, PSR, REV, SEW, SGX, SLC, STO, TFX, TWC, VEF, AER, AFC, AFG, AJK, ALU, GUM, HPA, HFO, PPG, STU, NH1, NH2, ONA, ONP
        - x (int): Forecast grid X coordinate.
        - y (int): Forecast grid Y coordinate.
        
        Returns:
        - dict: Dictionary containing the textual forcast data.
        """
        endpoint = f"gridpoints/{wfo}/{x},{y}/forecast"
        return mr.make_request(self.base_url+endpoint)
        
    def get_textual_hourly_forecast_by_gridpoints(self, wfo, x, y):
        """
        Returns a textual hourly forecast for a 2.5km grid area.

        Args:
        - wfo (str): Forecast office ID. Available values : AKQ, ALY, BGM, BOX, BTV, BUF, CAE, CAR, CHS, CLE, CTP, GSP, GYX, ILM, ILN, LWX, MHX, OKX, PBZ, PHI, RAH, RLX, RNK, ABQ, AMA, BMX, BRO, CRP, EPZ, EWX, FFC, FWD, HGX, HUN, JAN, JAX, KEY, LCH, LIX, LUB, LZK, MAF, MEG, MFL, MLB, MOB, MRX, OHX, OUN, SHV, SJT, SJU, TAE, TBW, TSA, ABR, APX, ARX, BIS, BOU, CYS, DDC, DLH, DMX, DTX, DVN, EAX, FGF, FSD, GID, GJT, GLD, GRB, GRR, ICT, ILX, IND, IWX, JKL, LBF, LMK, LOT, LSX, MKX, MPX, MQT, OAX, PAH, PUB, RIW, SGF, TOP, UNR, BOI, BYZ, EKA, FGZ, GGW, HNX, LKN, LOX, MFR, MSO, MTR, OTX, PDT, PIH, PQR, PSR, REV, SEW, SGX, SLC, STO, TFX, TWC, VEF, AER, AFC, AFG, AJK, ALU, GUM, HPA, HFO, PPG, STU, NH1, NH2, ONA, ONP
        - x (int): Forecast grid X coordinate.
        - y (int): Forecast grid Y coordinate.
        
        Returns:
        - dict: Dictionary containing the textual hourly forcast data.
        """
        endpoint = f"gridpoints/{wfo}/{x},{y}/forecast/hourly"
        return mr.make_request(self.base_url+endpoint)
        
    def get_observation_stations_by_gridpoints(self, wfo, x, y):
        """
        Returns a list of observation stations usable for a given 2.5km grid area.

        Args:
        - wfo (str): Forecast office ID. Available values : AKQ, ALY, BGM, BOX, BTV, BUF, CAE, CAR, CHS, CLE, CTP, GSP, GYX, ILM, ILN, LWX, MHX, OKX, PBZ, PHI, RAH, RLX, RNK, ABQ, AMA, BMX, BRO, CRP, EPZ, EWX, FFC, FWD, HGX, HUN, JAN, JAX, KEY, LCH, LIX, LUB, LZK, MAF, MEG, MFL, MLB, MOB, MRX, OHX, OUN, SHV, SJT, SJU, TAE, TBW, TSA, ABR, APX, ARX, BIS, BOU, CYS, DDC, DLH, DMX, DTX, DVN, EAX, FGF, FSD, GID, GJT, GLD, GRB, GRR, ICT, ILX, IND, IWX, JKL, LBF, LMK, LOT, LSX, MKX, MPX, MQT, OAX, PAH, PUB, RIW, SGF, TOP, UNR, BOI, BYZ, EKA, FGZ, GGW, HNX, LKN, LOX, MFR, MSO, MTR, OTX, PDT, PIH, PQR, PSR, REV, SEW, SGX, SLC, STO, TFX, TWC, VEF, AER, AFC, AFG, AJK, ALU, GUM, HPA, HFO, PPG, STU, NH1, NH2, ONA, ONP
        - x (int): Forecast grid X coordinate.
        - y (int): Forecast grid Y coordinate.
        
        Returns:
        - dict: Dictionary containing a list of observation stations usable for a given 2.5km grid area.
        """
        endpoint = f"gridpoints/{wfo}/{x},{y}/stations"
        return mr.make_request(self.base_url+endpoint)
        
    def get_observations_by_station(self, stationID):
        """
        Returns a list of observations for a given station.

        Args:
        - stationID (str): Observation station ID.
        
        Returns:
        - dict: Dictionary containing list of observations for a given station.
        """
        endpoint = f"stations/{stationID}/observations"
        return mr.make_request(self.base_url+endpoint)
        
    def get_station_observation_by_time(self, stationID, time):
        """
        Returns a single observation.

        Args:
        - stationID (str): Observation station ID.
        - time (str): Timestamp of requested observation.
        
        Returns:
        - dict: Dictionary containing single observation for a given station at a given time.
        """
        endpoint = f"stations/{stationID}/observations/{time}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_tafs_by_station(self, stationID):
        """
        Returns Terminal Aerodrome Forecasts for the specified airport station.

        Args:
        - stationID (str): Observation station ID.
        
        Returns:
        - dict: Dictionary containing TAFS for given station.
        """
        endpoint = f"stations/{stationID}/tafs"
        return mr.make_request(self.base_url+endpoint)
        
    def get_taf_by_date_time(self, stationID, date, time):
        """
        Returns a single Terminal Aerodrome Forecast..

        Args:
        - stationID (str): Observation station ID.
        - date (str): Date (YYYY-MM-DD format)
        - time (str) Time (HHMM format). This time is always specified in UTC (Zulu) time.
        
        Returns:
        - dict: Dictionary containing TAF.
        """
        endpoint = f"stations/{stationID}/tafs/{date}/{time}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_stations(self):
        """
        Returns a list of observation stations.

        Args:
        - None

        Returns:
        - dict: A dictionary containing a list of observation stations.
        """
        endpoint = "stations"
        return mr.make_request(self.base_url+endpoint)
        
    def get_station_metadata(self, stationID):
        """
        Returns metadata about a given observation station.

        Args:
        - stationID (str): Observation station ID.
        
        Returns:
        - dict: Dictionary containing metadata for given station.
        """
        endpoint = f"stations/{stationID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_NWS_office_metadata(self, officeID):
        """
        Returns metadata about a NWS forecast office.

        Args:
        - officeID (str): NWS office ID.
        
        Returns:
        - dict: Dictionary containing metadata for given NWS office.
        """
        endpoint = f"offices/{officeID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_NWS_office_headline_by_headline_id(self, officeID, headlineID):
        """
        Returns a specific news headline for a given NWS office.

        Args:
        - officeID (str): NWS office ID.
        - headlineID (str): Headline record ID.
        
        Returns:
        - dict: Dictionary containing headline for given NWS office and given headline ID.
        """
        endpoint = f"offices/{officeID}/headlines/{headlineID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_NWS_office_headlines(self, officeID):
        """
        Returns a list of news headlines for a given NWS office.

        Args:
        - officeID (str): NWS office ID.
        
        Returns:
        - dict: Dictionary containing headlines for given NWS office.
        """
        endpoint = f"offices/{officeID}/headlines"
        return mr.make_request(self.base_url+endpoint)

# HAVEN'T FIGURED THIS ONE OUT, HOW TO PASS POINT ARG AS LAT AND LONG      
#    def get_metadata_by_point(self, point):
#        """
#        Returns metadata about a given latitude/longitude point.
#
#        Args:
#        - point (str): Point(latitude,longitude)
#        
#        Returns:
#        - dict: Dictionary containing metadata for given point.
#        """
#        endpoint = f"points/{point}"
#        return mr.make_request(self.base_url+endpoint)

    def get_radar_servers(self):
        """
        Returns a list of radar servers.

        Args:
        - None

        Returns:
        - dict: A dictionary containing a list of radar servers.
        """
        endpoint = "radar/servers"
        return mr.make_request(self.base_url+endpoint)
        
    def get_radar_server_metadata_by_id(self, serverID):
        """
        Returns metadata about a given radar server.

        Args:
        - serverID (str): Radar server ID.
        
        Returns:
        - dict: Dictionary containing metadata for given radar server.
        """
        endpoint = f"radar/servers/{serverID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_radar_stations(self):
        """
        Returns a list of radar stations.

        Args:
        - None

        Returns:
        - dict: A dictionary containing a list of radar stations.
        """
        endpoint = "radar/stations"
        return mr.make_request(self.base_url+endpoint)
        
    def get_radar_station_metadata_by_id(self, stationID):
        """
        Returns metadata about a given radar station.

        Args:
        - stationID (str): Radar station ID.
        
        Returns:
        - dict: Dictionary containing metadata for given radar station.
        """
        endpoint = f"radar/stations/{stationID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_radar_station_alarms_metadata_by_id(self, stationID):
        """
        Returns metadata about a given radar station alarms.

        Args:
        - stationID (str): Radar station ID.
        
        Returns:
        - dict: Dictionary containing metadata for given radar station alarms.
        """
        endpoint = f"radar/stations/{stationID}/alarms"
        return mr.make_request(self.base_url+endpoint)
        
    def get_radar_queue_metadata(self, host):
        """
        Returns metadata about a given radar queue.

        Args:
        - host (str): LDM host.
        
        Returns:
        - dict: Dictionary containing metadata for given radar queue.
        """
        endpoint = f"radar/queues/{host}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_radar_wind_profiler_metadata(self, stationID):
        """
        Returns metadata about a given radar wind profiler.

        Args:
        - stationID (str): Profiler station ID.
        
        Returns:
        - dict: Dictionary containing metadata for given radar wind profiler.
        """
        endpoint = f"radar/profilers/{stationID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_text_products(self):
        """
        Returns a list of text products.

        Args:
        - None

        Returns:
        - dict: A dictionary containing a list of text products.
        """
        endpoint = "products"
        return mr.make_request(self.base_url+endpoint)
        
    def get_text_product_locations(self):
        """
        Returns a list of valid text product issuance locations.

        Args:
        - None

        Returns:
        - dict: A dictionary containing a list of valid text product issuance locations.
        """
        endpoint = "products/locations"
        return mr.make_request(self.base_url+endpoint)
        
    def get_text_product_types(self):
        """
        Returns a list of valid text product types and codes.

        Args:
        - None

        Returns:
        - dict: A dictionary containing a list of valid text product types and codes.
        """
        endpoint = "products/types"
        return mr.make_request(self.base_url+endpoint)
        
    def get_text_product_by_id(self, productID):
        """
        Returns a specific text product.

        Args:
        - productID (str): Text product ID.
        
        Returns:
        - dict: Dictionary containing specific text product.
        """
        endpoint = f"products/{productID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_text_products_by_type(self, typeID):
        """
        Returns a list of text products of a given type.

        Args:
        - typeID (str): Text product type ID.
        
        Returns:
        - dict: Dictionary containing list of text products of given type.
        """
        endpoint = f"products/types/{typeID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_text_product_locations_by_type(self, typeID):
        """
        Returns a list of valid text product issuance locations for a given product type.

        Args:
        - typeID (str): Text product type ID.
        
        Returns:
        - dict: Dictionary containing list of valid text product issuance locations for a given type.
        """
        endpoint = f"products/types/{typeID}/locations"
        return mr.make_request(self.base_url+endpoint)
        
    def get_text_product_types_by_location(self, locationID):
        """
        Returns a list of valid text product types for a given issuance location.

        Args:
        - locationID (str): Location ID.
        
        Returns:
        - dict: Dictionary containing list of valid text product types for a given location.
        """
        endpoint = f"products/locations/{locationID}/types"
        return mr.make_request(self.base_url+endpoint)
        
    def get_text_products_by_type_and_location(self, typeID, locationID):
        """
        Returns a list of text products of a given type for a given issuance location.

        Args:
        - typeID (str): Text product type ID.
        - locationID (str): Location ID.
        
        Returns:
        - dict: Dictionary containing list of text product of a given type for a given issuance location.
        """
        endpoint = f"products/types/{typeID}/locations/{locationID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_zones(self):
        """
        Returns a list of zones.

        Args:
        - None

        Returns:
        - dict: A dictionary containing a list of zones.
        """
        endpoint = "zones"
        return mr.make_request(self.base_url+endpoint)

# HAVEN'T FIGURED THIS ONE OUT. PARAMETER IS A QUERY, NOT PATH  
    def get_zones_by_type(self, Type):
        """
        Returns a list of valid text product types for a given issuance location.

        Args:
        - Type (str): Zone type. Available values : land, marine, forecast, public, coastal, offshore, fire, county.
        
        Returns:
        - dict: Dictionary containing list of valid text product types for a given location.
        """
        endpoint = f"zones/{Type}"
        return mr.make_request(self.base_url+endpoint)

    def get_zone_metadata(self, Type, zoneID):
        """
        Returns metadata about a given zone.

        Args:
        - Type (str): Zone type. Available values : land, marine, forecast, public, coastal, offshore, fire, county.
        - zoneID (str): NWS public zone/county identifier.
        
        Returns:
        - dict: Dictionary containing metadata about a given zone.
        """
        endpoint = f"zones/{Type}/{zoneID}"
        return mr.make_request(self.base_url+endpoint)
        
    def get_zone_forecast(self, Type, zoneID):
        """
        Returns the current zone forecast for a given zone.

        Args:
        - Type (str): Zone type. Available values : land, marine, forecast, public, coastal, offshore, fire, county.
        - zoneID (str): NWS public zone/county identifier.
        
        Returns:
        - dict: Dictionary containing zone forecast for a given zone.
        """
        endpoint = f"zones/{Type}/{zoneID}/forecast"
        return mr.make_request(self.base_url+endpoint)
        
    def get_zone_observations(self, zoneID):
        """
        Returns a list of observations for a given zone.

        Args:
        - zoneID (str): NWS public zone/county identifier.
        
        Returns:
        - dict: Dictionary containing a list of observations for a given zkne.
        """
        endpoint = f"zones/forecast/{zoneID}/observations"
        return mr.make_request(self.base_url+endpoint)
        
    def get_observation_stations_by_zone(self, zoneID):
        """
        Returns a list of observation stations for a given zone.

        Args:
        - zoneID (str): NWS public zone/county identifier.
        
        Returns:
        - dict: Dictionary containing a list of observation stations for a given zkne.
        """
        endpoint = f"zones/forecast/{zoneID}/stations"
        return mr.make_request(self.base_url+endpoint)
    
    
    
    
  
       
       
        
        
     
      
      
      
        
    
    
      
      
      
   
   
   
   
        
 
      
      
      
        
        
        
    
       
     
     
     
        
    
       
        
        
   
        
        
    
    
    