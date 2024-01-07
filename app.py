import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.velvetwatches.uk'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the article titles (modify this based on the actual structure of the website)
    article_titles = soup.find_all('h2', class_='article-title')

    # Extract and print the titles
    for title in article_titles:
        print(title.text)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
