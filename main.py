import requests

from bs4 import BeautifulSoup

website_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(website_url)
response.raise_for_status()

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

print(soup.prettify())
