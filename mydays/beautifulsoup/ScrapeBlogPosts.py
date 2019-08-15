import bs4
import requests

article_titles = []

def get_site_text():
    response = requests.get("http://www.feoh.org")
    response.raise_for_status()
    return response.text


def get_article_titles(soup):
    title_headers = soup.find_all('h1', 'entry-title')

    for title_header in title_headers:
       article_titles.append(title_header.a.string)

    return article_titles

site_text = get_site_text()

soup = bs4.BeautifulSoup(site_text, 'html.parser')

article_titles = get_article_titles(soup)

site_title = soup.title.string

print(f"Site Title: {site_title}")

for article_title in article_titles:
   print(f"Article Title: {article_title}")
