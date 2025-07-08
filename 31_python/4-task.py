import requests
import json

def get_website_content(url):
    """
    Fetches the content of a website.

    Args:
        url (str): The URL of the website to fetch.

    Returns:
        str: The content of the website.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        json = response.json()
        return json
    except requests.RequestException as e:
        return f"An error occurred: {e}"
    
def main():
    url = input("Enter the URL of the website: ")
    content = get_website_content(url)
    
    if "An error occurred" in content:
        print(content)
    else:
        print(json.dumps(content, indent=4, ensure_ascii=False)) 

main()
