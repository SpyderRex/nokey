import requests
from requests.exceptions import HTTPError, Timeout, RequestException

def make_request(url, headers=None, payload=None):
    """
    Make an HTTP request to the specified URL with optional headers and payload.
    
    Args:
        url (str): The URL of the API endpoint.
        headers (dict, optional): Headers to be included in the request.
        payload (dict, optional): The payload to be sent in the request body.
        
    Returns:
        dict: A dictionary containing the response data or error information.
    """
    try:
        if payload is not None:
            response = requests.post(url, headers=headers, json=payload)
        else:
            response = requests.get(url, headers=headers)
        
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response.json()  # Return JSON response
    except HTTPError as http_err:
        # Handle HTTP error
        return {"error": f"HTTP error occurred: {http_err}", "message": response.json()["message"] if "message" in response.json() else None}
    except Timeout:
        # Handle timeout error
        return {"error": "Request timed out."}
    except RequestException as req_err:
        # Handle other request exceptions
        return {"error": f"Request exception occurred: {req_err}"}
    except Exception as err:
        # Handle any other unexpected errors
        return {"error": f"An unexpected error occurred: {err}"}


def make_request_with_params(url, params):
    """
    Make a request to an API if the API call requires params.
    
    Args:
    - url (str): The url of the API.
    - params (dict): The params to be included in the request.
    
    Returns:
    - dict: A dictionary containing either the response data or an error message.
    """
    try:
        response = requests.get(url, params)
        return response.json()
    except HTTPError as http_err:
        # Handle HTTP error
        return {"error": f"HTTP error occurred: {http_err}", "message": response.json()["message"] if "message" in response.json() else None}
    except Timeout:
        # Handle timeout error
        return {"error": "Request timed out."}
    except RequestException as req_err:
        # Handle other request exceptions
        return {"error": f"Request exception occurred: {req_err}"}
    except Exception as err:
        # Handle any other unexpected errors
        return {"error": f"An unexpected error occurred: {err}"}
        
def make_request_for_content(url):
    """
    Make a request to an API if the API call returns content other than in JSON format.
    
    Args:
    - url (str): The url of the API.
    
    Returns:
    - string: Text in any format containing either the response data or an error message.
    """
    try:
        response = requests.get(url)
        return response.content
    except HTTPError as http_err:
        # Handle HTTP error
        return {"error": f"HTTP error occurred: {http_err}"}
    except Timeout:
        # Handle timeout error
        return {"error": "Request timed out."}
    except RequestException as req_err:
        # Handle other request exceptions
        return {"error": f"Request exception occurred: {req_err}"}
    except Exception as err:
        # Handle any other unexpected errors
        return {"error": f"An unexpected error occurred: {err}"}
        
def make_request_for_content_with_params(url, params):
    """
    Make a request to an API if the API call returns content other than in JSON format.
    
    Args:
    - url (str): The url of the API.
    
    Returns:
    - string: Text in any format containing either the response data or an error message.
    """
    try:
        response = requests.get(url, params)
        return response.content
    except HTTPError as http_err:
        # Handle HTTP error
        return {"error": f"HTTP error occurred: {http_err}"}
    except Timeout:
        # Handle timeout error
        return {"error": "Request timed out."}
    except RequestException as req_err:
        # Handle other request exceptions
        return {"error": f"Request exception occurred: {req_err}"}
    except Exception as err:
        # Handle any other unexpected errors
        return {"error": f"An unexpected error occurred: {err}"}
        
        
def make_request_with_post_and_data(url, data):
    """
    Make a request to an API if the API using the POST method.
    
    Args:
    - url (str): The url of the API.
    - data (dict): The data to be included in the request.
    
    Returns:
    - dict: A dictionary containing either the response data or an error message.
    """
    try:
        response = requests.post(url, data=data)
        return response.json()
    except HTTPError as http_err:
        # Handle HTTP error
        return {"error": f"HTTP error occurred: {http_err}", "message": response.json()["message"] if "message" in response.json() else None}
    except Timeout:
        # Handle timeout error
        return {"error": "Request timed out."}
    except RequestException as req_err:
        # Handle other request exceptions
        return {"error": f"Request exception occurred: {req_err}"}
    except Exception as err:
        # Handle any other unexpected errors
        return {"error": f"An unexpected error occurred: {err}"}
        
def make_request_with_post_and_json(url, json):
    """
    Make a request to an API if the API using the POST method.
    
    Args:
    - url (str): The url of the API.
    - data (dict): The data to be included in the request.
    
    Returns:
    - dict: A dictionary containing either the response data or an error message.
    """
    try:
        response = requests.post(url, json=json)
        return response.json()
    except HTTPError as http_err:
        # Handle HTTP error
        return {"error": f"HTTP error occurred: {http_err}", "message": response.json()["message"] if "message" in response.json() else None}
    except Timeout:
        # Handle timeout error
        return {"error": "Request timed out."}
    except RequestException as req_err:
        # Handle other request exceptions
        return {"error": f"Request exception occurred: {req_err}"}
    except Exception as err:
        # Handle any other unexpected errors
        return {"error": f"An unexpected error occurred: {err}"}
        
def add_params(params, params_list):
    """
    Adds parameters to the params dictionary if their values are not None.

    Args:
        params (dict): The dictionary to add parameters to.
        params_list (list of tuples): Each tuple contains (original_param_name, new_param_name).
    """
    for original_param_name, new_param_name in params_list:
        if new_param_name is not None:
            params[original_param_name] = new_param_name
        
      
        