# nokey - Access APIs without a Key

nokey is a Python package designed to provide easy access to various APIs that do not require an API key for authentication. This project aims to simplify the process of interacting with different APIs by offering a unified interface for accessing them, all within a single Python package.

## Features

- Access a growing collection of keyless APIs conveniently from one place.
- Organized into submodules based on categories such as country information, finance, geolocation, spaceflight, education, food, random data, jokes, animals, science, and weather, developer tools, language, and games.
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

Also, to print out a list of the APIs supported by nokey, simply run the following script:

```python
from nokey.helperFuncs.get_api_list import get_api_list

api_list = get_api_list()

print(api_list)
```

Each API class has optional caching with requests_cache. To enable caching, set the use_caching argument when calling the class to True.

Each API class has an "about" attribute that returns a short description of the API. To get the URL for the API documentation of any API, simply call the get_docs_url() method for the API class.

## Contributing
We welcome contributions to expand the range of APIs available in nokey. Whether you want to add a new submodule or enhance an existing one, your contributions are valuable. To contribute, please fork the repository, make your changes, and submit a pull request.

# Supported APIs
## country_info
RestCountries

## finance_and_crypto
Wallstreet Bets

Exchange API

Coinmap

## geolocation
IP API

Zippopotomus

## spaceflight
Spaceflight News

## education
University Domains and Names

## food
Fruityvice

## random
RandomUserGenerator

## jokes
JokeAPI

## animals
DogAPI

## science_and_nature
Nobel Prize API

Integrated Taxonomic Information System

## weather
National Weather Service API

## developer_tools
URL Shortener

URLHaus

APIsGuru

Microlink

FilterLists

## inspiration
Dictum

## language
Free Dictionary

## games
Free To Game

Open Trivia Database

Shadify

## activities
Bored API

## calendar
Nager.Date

## government
Federal Register

USA Spending

## tv_and_film
Star Trek API

## books_and_literature
Gutendex

## art_and_images
Lorum Picsum

Art Institute of Chicago

## health
Open Disease

# Future Roadmap
As the project grows, we envision expanding the collection of keyless APIs to cover a wide range of categories. Your feedback and contributions will play a crucial role in shaping the future of nokey.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Documentation
Check out the [docs](https://nokey.readthedocs.io/en/latest/).

# Disclaimer:
Be sure to read the API documentation if you plan to use any of the APIs for development. This package is for accessing keyless, free, open source APIs and I am not responsible for the content of the APIs themselves.
