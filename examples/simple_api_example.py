#!/usr/bin/env python3
"""
Simplest possible API example - Get a random dog image
"""

import requests

# Make a GET request to the Dog API
response = requests.get("https://dog.ceo/api/breeds/image/random")

# Parse the JSON response
data = response.json()

# Print the result
print("Random Dog Image URL:")
print(data['message'])
