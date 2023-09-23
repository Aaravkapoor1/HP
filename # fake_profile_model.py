# fake_profile_model.py

import requests
from bs4 import BeautifulSoup
import re

def detect_fake_profile(profile_url):
    # Placeholder for fake profile detection
    try:
        # You can use web scraping techniques to extract profile information
        profile_data = scrape_profile_data(profile_url)

        # Perform some basic checks (customize based on your model)
        is_fake = basic_fake_profile_check(profile_data)

        return is_fake

    except Exception as e:
        print(f"Error detecting fake profile: {str(e)}")
        return False

def scrape_profile_data(profile_url):
    # Use web scraping to extract data from the social media profile
    try:
        response = requests.get(profile_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract profile information, e.g., name, bio, posts, etc.
            profile_data = {
                'name': soup.find('h1').text,
                'bio': soup.find('p', class_='bio').text,
                # Add more fields as needed
            }
            return profile_data
        else:
            raise Exception("Failed to fetch profile data")
    except Exception as e:
        raise e

def basic_fake_profile_check(profile_data):
    # Perform basic checks to detect fake profiles (customize based on your model)
    name = profile_data.get('name', '')
    bio = profile_data.get('bio', '')

    # Example: Check if the bio contains suspicious keywords
    suspicious_keywords = ['fake', 'scam', 'bot', 'spam']
    for keyword in suspicious_keywords:
        if re.search(r'\b' + keyword + r'\b', bio, re.IGNORECASE):
            return True

    # Example: Check if the name is unusual or random characters
    if len(name) <= 3:
        return True

    return False
