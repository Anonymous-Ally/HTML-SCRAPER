import requests # Learn more: https://python.org/pypi/requests
from bs4 import BeautifulSoup as bs # Learn more: https://python.org/pypi/beautifulsoup4

url = 'https://' + input('URL: ') # Store the URL in a variable.
r = requests.get(url) # Get a request from the website.
soup = bs(r.content, 'html.parser') # Parse the HTML content.
tag_names = [tag.name for tag in soup.find_all(name=True)] # Get all the tag names.

print(soup) # Print the HTML content.
