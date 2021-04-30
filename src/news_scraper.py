import requests

from GoogleNews import GoogleNews
from bs4 import BeautifulSoup


def get_search_results(keyword: str):
    googlenews = GoogleNews(lang="en", period="7d", encode="utf-8")
    googlenews.get_news(keyword)
    googlenews.search(keyword)
    googlenews.get_page(1)
    results = googlenews.results()
    return results[0:5]


def scrape_article(link: str):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Max-Age": "3600",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    }
    req = requests.get(link, headers)
    soup = BeautifulSoup(req.content, "html.parser")
    ps = soup.find_all("p")
    cont = []

    for p in ps:
        str = p.get_text()
        if not "https://" in str.lower():
            if "about us" in str.lower():
                break
            else:
                cont.append(str.lower().rstrip())

    return cont
