from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    new = search_news({"title": {"$regex": title, "$options": "i"}})
    if new:
        return [(i["title"], i["url"]) for i in new]
    return []


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
