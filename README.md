# Simple Web Scraper

## Overview

This project is a simple web scraper built using Python. It utilizes the requests library to fetch web pages and BeautifulSoup from the bs4 library to parse HTML content. The scraper extracts text, links, and images from a specified URL and saves the data into a CSV file. It also downloads images into a separate directory.

## Features

- Scrapes text from all <p> (paragraph) elements.
- Collects links from <a> tags that start with "http".
- Extracts image source URLs from <img> tags.
- Downloads images to a local folder.
- Saves scraped data to a CSV file.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation

1. *Clone the repository:*
   ```bash
   git clone https://github.com/yourusername/simple-web-scraper.git
   cd simple-web-scraper


2. Install the required packages:

pip install requests beautifulsoup4 pandas



Usage

1. Open the scraper.py file in a text editor.


2. Replace the URL in the example usage with the target website you want to scrape:

scrape_website("https://www.example.com")


3. Run the script:

python scraper.py


4. The scraped data will be saved in scraped_data.csv, and images will be downloaded to the images directory.



Example

Here's an example of how to scrape data from a webpage:

scrape_website("https://en.wikipedia.org/wiki/Web_scraping")

Error Handling

The scraper includes basic error handling for network requests. If any errors occur while fetching the webpage or downloading images, appropriate messages will be displayed in the console.

Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

   
