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
    select = Selector(text=html_content)
    link = select.css("div[class=nav-links] a:last-of-type::attr(href)").get()
    if not link:
        return None
    return link


# Requisito 4
def scrape_news(html_content):
    select = Selector(text=html_content)
    url = select.css("head link[rel=canonical]::attr(href)").get()
    title = select.css(".entry-title::text").get()
    if title is None:
        title = select.css(".Hero_hero__title__dCXAM-title::text").get()
    title = title.strip()
    timestamp = select.css(".meta-date::text").get()
    writer = select.css(".author > a::text").get()
    reading_time = int(
        select.css(".meta-reading-time::text").get().split(" ")[0]
    )
    summary = (
        select.css("div[class=entry-content] > p:first-of-type")
        .xpath("string()")
        .get()
        .strip()
    )
    category = select.css(".category-style .label::text").get()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
