from time import sleep
from requests import get
from parsel import Selector


# Requisito 1


def fetch(url):
    try:
        sleep(1)
        response = get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
        return response.text
    except Exception:
        return None


# Requisito 2
def scrape_updates(html_content):
    list = []
    select = Selector(text=html_content)
    links = select.css("h2[class=entry-title] a::attr(href)").getall()
    list.extend(links)
    return list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
