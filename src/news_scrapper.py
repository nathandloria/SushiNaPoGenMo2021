from newspaper import Article
from GoogleNews import GoogleNews
import json

def get_search_results(keyword:str):
    googlenews = GoogleNews(lang="en", period="7d", encode="utf-8")
    googlenews.get_news(keyword)
    googlenews.search(keyword)
    googlenews.get_page(1)
    results = googlenews.results()
    return results

def scrape_article(link:str):
    article = Article(url)
    article.download()
    article.parse()
    return(article.text)

if __name__ == "__main__":
    # search_results = search_topic("Gamestop")
    # print(search_results)
    url = "https://www.forbes.com/sites/jackbrewster/2021/04/30/biden-sticks-with-his-mask-as-critics-claim-hes-sending-the-wrong-message-about-vaccines/?sh=4ce813614b06"
    print(scrape_article(url))
    # TODO: fix article download error