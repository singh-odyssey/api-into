#!/usr/bin/env python3
"""
Simple example of using free public APIs
This script demonstrates how to fetch data from public APIs without authentication
"""

import requests
import json


def example_1_random_dog():
    """
    Example 1: Random Dog API
    Returns a random dog image
    """
    print("\n=== Example 1: Random Dog Image ===")
    url = "https://dog.ceo/api/breeds/image/random"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Status: {data['status']}")
        print(f"Dog Image URL: {data['message']}")
    else:
        print(f"Error: {response.status_code}")


def example_2_public_holidays():
    """
    Example 2: Public Holidays API
    Get public holidays for a country
    """
    print("\n=== Example 2: Public Holidays (USA 2025) ===")
    url = "https://date.nager.at/api/v3/PublicHolidays/2025/US"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        holidays = response.json()
        print(f"Found {len(holidays)} holidays")
        # Show first 3 holidays
        for holiday in holidays[:3]:
            print(f"- {holiday['date']}: {holiday['name']}")
    else:
        print(f"Error: {response.status_code}")


def example_3_random_user():
    """
    Example 3: Random User Generator API
    Generate random user data
    """
    print("\n=== Example 3: Random User Data ===")
    url = "https://randomuser.me/api/"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]
        print(f"Name: {user['name']['first']} {user['name']['last']}")
        print(f"Email: {user['email']}")
        print(f"Location: {user['location']['city']}, {user['location']['country']}")
    else:
        print(f"Error: {response.status_code}")


def example_4_activity():
    """
    Example 4: Bored API
    Get a random activity suggestion
    """
    print("\n=== Example 4: Random Activity Suggestion ===")
    url = "https://www.boredapi.com/api/activity"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Activity: {data['activity']}")
        print(f"Type: {data['type']}")
        print(f"Participants: {data['participants']}")
    else:
        print(f"Error: {response.status_code}")


def example_5_cat_fact():
    """
    Example 5: Cat Facts API
    Get a random cat fact
    """
    print("\n=== Example 5: Random Cat Fact ===")
    url = "https://catfact.ninja/fact"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Fact: {data['fact']}")
        print(f"Length: {data['length']} characters")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    print("=" * 60)
    print("FREE PUBLIC API EXAMPLES")
    print("=" * 60)
    
    try:
        example_1_random_dog()
        example_2_public_holidays()
        example_3_random_user()
        example_4_activity()
        example_5_cat_fact()
        
        print("\n" + "=" * 60)
        print("All examples completed successfully!")
        print("=" * 60)
        
    except requests.exceptions.RequestException as e:
        print(f"\nNetwork Error: {e}")
    except Exception as e:
        print(f"\nError: {e}")
