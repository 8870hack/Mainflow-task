import requests
from bs4 import BeautifulSoup

# Function to scrape headlines from a news website
def scrape_headlines(url):
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return []

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract headlines (change the HTML tag and class based on the website structure)
    headlines = []
    for headline in soup.find_all('h3'):  # Assuming headlines are under <h3> tags
        headlines.append(headline.get_text(strip=True))
    
    return headlines

# Define the URL you want to scrape
url = 'https://www.bbc.com/news'

# Scrape headlines
headlines = scrape_headlines(url)

# Print the scraped headlines
print("Headlines:")
for i, headline in enumerate(headlines, start=1):
    print(f"{i}. {headline}")