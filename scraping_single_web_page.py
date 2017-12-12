import requests
import MySQLdb
from bs4 import BeautifulSoup

#SQL connection data to connect and save the data in
HOST = "localhost"
USERNAME = "scraping_sample_user"
PASSWORD = ""
DATABASE = "scraping_sample_user"

#URL to be scraped
url_to_scrape = 'https://howpcrules.com/sample-page-for-web-scraping/'
#Load html's plain data into a variable
plain_html_text = requests.get(url_to_scrape)
#parse the data
soup = BeautifulSoup(plain_html_text.text, "html.parser")

print(soup.prettify())