import requests
import requests_cache
from .. helperFuncs import make_request as mr

class LoremPicsum:
    """
    A class for interacting with the Lorem Picsum API.
    
    Attributes:
    - base_url: The base URL of the API.
    - about: A short description of the API.
    """
    def __init__(self, use_caching=False, cache_name="lorem_picsum_cache", backend="sqlite", expire_after=3600):
        self.base_url = "https://picsum.photos/"
        self.about = "This is an API for getting placeholder images, a Lorem Ipsum for images."
        
        if use_caching:
            requests_cache.install_cache(cache_name, backend=backend, expire_after=expire_after)
            
    def get_docs_url(self):
        """
        Returns the URL for the Lorem Picsum API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the API docs.
        """
        return "https://picsum.photos/"
        
    def get_random_image(self, width, height=None, grayscale=False, blur=None):
        """
        Returns the URL for to a random placeholder image with the given dimensions.
        
        Args:
        - width (int): The width of the image.
        - height (int): The height of the image. Defaults to None in which case the image is square.
        - grayscale (boolean): Optional argument for returning a grayscale picture. The default value is False.
        - blur (int): An option to return a blurred photo. Values range from 1 to 10.
        
        Returns:
        string: The URL of the placeholder image.
        """
        if height is not None:
            if grayscale:
                if blur is not None:
                    endpoint = f"{width}/{height}?grayscale&blur={blur}"
                    return self.base_url+endpoint
                else:
                    endpoint = f"{width}/{height}?grayscale"
                    return self.base_url+endpoint
            else:
                if blur is not None:
                    endpoint = f"{width}/{height}?blur={blur}"
                    return self.base_url+endpoint
                else:
                    endpoint = f"{width}/{height}"
                    return self.base_url+endpoint
        else:
            if grayscale:
                if blur is not None:
                    endpoint = f"{width}?grayscale&blur={blur}"
                    return self.base_url+endpoint
                else:
                    endpoint = f"{width}?grayscale"
                    return self.base_url+endpoint
            else:
                if blur is not None:
                    endpoint = f"{width}?blur={blur}"
                    return self.base_url+endpoint
                else:
                    endpoint = f"{width}"
                    return self.base_url+endpoint
            
    def get_image_by_id(self, image_id, width, height=None, grayscale=False, blur=None):
        """
        Returns the URL for a specific image matching the given id number.
        
        Args:
        - image_id (int): A unique numerical id matching a specific image.
        - width (int): The width of the image.
        - height (int): The height of the image. Defaults to None in which case the image is square.
        
        Returns:
        - string: The URL to the image matching the given parameters.
        """
        if height is not None:
            if grayscale:
                if blur is not None:
                    endpoint = f"id/{image_id}/{width}/{height}?grayscale&blur={blur}"
                    return self.base_url+endpoint
                else:
                    endpoint = f"id/{image_id}/{width}/{height}?grayscale"
                    return self.base_url+endpoint
            else:
                if blur is not None:
                    endpoint = f"id/{image_id}/{width}/{height}?blur={blur}"
                    return self.base_url+endpoint
                else:
                    endpoint = f"id/{image_id}/{width}/{height}"
                    return self.base_url+endpoint
        else:
            if grayscale:
                if blur is not None:
                    endpoint = f"id/{image_id}/{width}?grayscale&blur={blur}"
                    return self.base_url+endpoint
                else:
                    endpoint = f"id/{image_id}/{width}?grayscale"
                    return self.base_url+endpoint
            else:
                if blur is not None:
                    endpoint = f"id/{image_id}/{width}?blur={blur}"
                    return self.base_url+endpoint
                else:
                    endpoint = f"id/{image_id}/{width}"
                    return self.base_url+endpoint
            
            
    def get_static_random_image(self, seed, width, height=None, grayscale=False, blur=None):
        """
        Returns the URL for to a random placeholder image with the given dimensions.
        
        Args:
        - seed (str): A seed term to ensure the same random image is returned each time.
        - width (int): The width of the image.
        - height (int): The height of the image. Defaults to None in which case the image is square.
        
        Returns:
        string: The URL of the placeholder image.
        """
        if height is not None:
            if grayscale:
                if blur is not None:
                    endpoint = f"seed/{seed}/{width}/{height}?grayscale&blur={blur}"
                    return self.base_url+endpoint
                else:
                    endpoint = f"seed/{seed}/{width}/{height}?grayscale"
                    return self.base_url+endpoint
            else:
                if blur is not None:
                    endpoint = f"seed/{seed}/{width}/{height}?blur={blur}"
                    return self.base_url+endpoint
                else:
                    endpoint = f"seed/{seed}/{width}/{height}"
                    return self.base_url+endpoint
        else:
            if grayscale:
                if blur is not None:
                    endpoint = f"seed/{seed}/{width}?grayscale&blur={blur}"
                    return self.base_url+endpoint
                else:
                    endpoint = f"seed/{seed}/{width}?grayscale"
                    return self.base_url+endpoint
            else:
                if blur is not None:
                    endpoint = f"seed/{seed}/{width}?blur={blur}"
                    return self.base_url+endpoint
                else:
                    endpoint = f"seed/{seed}/{width}"
                    return self.base_url+endpoint
                    
    def list_images(self, page=1, limit=30):
        """
        Returns a list of images in the Lorem Picsum API.
        
        Args:
        - page (int): The page of images to return. Default is the first page.
        - limit (int): The number of items per page. Default is 30.
        
        Returns:
        - list: A list of images in the Lorem Picsum API.
        """
        endpoint = f"v2/list?page={page}&limit={limit}"
        content = requests.get(self.base_url+endpoint)
        return content.text
        
    def get_image_info_by_id(self, image_id):
        """
        Returns info about a specific image matching the given id.
        
        Args:
        - image_id (int): A number matching a specific image.
        
        Returns:
        - dict: A dictionary containing info about a specific image.
        """
        endpoint = f"id/{image_id}/info"
        return mr.make_request(self.base_url+endpoint)
        
    def get_image_info_by_seed(self, seed):
        """
        Returns info about a specific image matching the given seed.
        
        Args:
        - seed (str): The seed matching a specific image.
        
        Returns:
        - dict: A dictionary containing info about a specific image.
        """
        endpoint = f"seed/{seed}/info"
        return mr.make_request(self.base_url+endpoint)
   
            
        
        
        