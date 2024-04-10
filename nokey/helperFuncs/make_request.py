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
