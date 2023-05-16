from tech_news.database import search_news
from datetime import datetime


def format_func(list):
    format_list = []

    for i in list:
        format_new = (i["title"], i["url"])
        format_list.append(format_new)

    return format_list


# Requisito 7
def search_by_title(title):
    new = search_news({"title": {"$regex": title, "$options": "i"}})
    if new:
        return [(i["title"], i["url"]) for i in new]
    return []


# Requisito 8
def search_by_date(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    list = search_news({"timestamp": (date.strftime("%d/%m/%Y"))})

    return format_func(list)


# Requisito 9
def search_by_category(category: str):
    new = search_news({"category": category.lower().capitalize()})
    if new:
        return [(i["title"], i["url"]) for i in new]
    return []
