# nokey - Access APIs without a Key

nokey is a Python package designed to provide easy access to various APIs that do not require an API key for authentication. This project aims to simplify the process of interacting with different APIs by offering a unified interface for accessing them, all within a single Python package.

## Features

- Access a growing collection of keyless APIs conveniently from one place.
- Organized into submodules based on categories such as country information, finance, geolocation, spaceflight, education, food, random data, jokes, animals, science, and weather.
- Easily installable via pip, making it accessible to all Python developers.

## Installation

You can install the module using pip:

```
pip install nokey
```

## Usage

Here is a simple example of how to use one of the APIs to access a random dog image:

```python
from nokey.animals import dog_api

# Initialize the DogAPI object
dog = dog_api.DogAPI()

# Get a random dog image URL
dog_image_url = dog.get_random_dog_image()

# Print the URL
print(dog_image_url)
```

## Contributing
We welcome contributions to expand the range of APIs available in nokey. Whether you want to add a new submodule or enhance an existing one, your contributions are valuable. To contribute, please fork the repository, make your changes, and submit a pull request.

Supported APIs
## Country Info
RestCountries
## Finance
Wallstreet Bets
## Geolocation
IP API
## Spaceflight
Spaceflight News
## Education
University Names and Domains
## Food
Fruityvice
## Random
RandomUserGenerator
## Jokes
JokeAPI
## Animals
DogAPI
## Science
Nobel Prize API
## Weather
National Weather Service API

# Future Roadmap
As the project grows, we envision expanding the collection of keyless APIs to cover a wide range of categories. Your feedback and contributions will play a crucial role in shaping the future of nokey.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
