from .. helperFuncs import make_request as mr

class DogAPI:
    """
    A class to interact with the Dog API.
    
    Attributes:
    - base_url: The base URL for the API.
    """
    def __init__(self):
        self.base_url = "https://dog.ceo/api/"
        
    def get_docs_url(self):
        """
        Returns the URL for the Dog API documentation.
        
        Args:
        - None
        
        Returns:
        - string: The URL for the Dog API documentation.
        """
        return "https://dog.ceo/dog-api/documentation/"
        
    def get_all_dog_breeds(self):
        """
        Returns a list of all the dog breeds in the Dog API.
        
        Args:
        - None
        
        Returns:
        - dict: Returns a dictionary containing a list of all the dog breeds in the Dog API.
        """
        endpoint = "breeds/list/all"
        return mr.make_request(self.base_url+endpoint)
        
    def get_random_dog_image(self):
        """
        Returns the URL for a random dog image.
        
        Args:
        - None
        
        Returns:
        - dict: Dictionary containing the URL for a random dog image.
        """
        endpoint = "breeds/image/random"
        return mr.make_request(self.base_url+endpoint)
        
    def get_dog_images_by_breed(self, breed):
        """
        Returns an array of URLs for images of dogs of the specified breed.
        
        Args:
        - breed (str): The breed of the dog.
        
        Returns:
        - dict: Dictionary containing a list of URLs of images for the specified dog breed.
        """
        endpoint = f"breed/{breed.lower()}/images"
        return mr.make_request(self.base_url+endpoint)
        
    def get_all_subBreeds(self, breed):
        """
        Returns a list of all sub-breeds for the specified dog breed.
        
        Args:
        - breed (str): The breed of the dog.
        
        Returns:
        - dict: Dictionary containing a list of all sub-breeds for the specified dog breed.
        """
        endpoint = f"breed/{breed.lower()}/list"
        return mr.make_request(self.base_url+endpoint)
        
    def get_random_dog_image_by_breed(self, breed):
        """
        Returns the URL for a random dog image of the specified breed.
        
        Args:
        - breed (str): The breed of the dog.
        
        Returns:
        - dict: Dictionary the URL for a random dog image of the specified breed.
        """
        endpoint = f"breed/{breed.lower()}/images/random"
        return mr.make_request(self.base_url+endpoint)
  
   
        
    