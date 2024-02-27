import json
from urllib.request import urlopen

import requests

"""
adapted from https://www.mediawiki.org/wiki/API:Links
"""


def get_links(title):

    session = requests.Session()

    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": (title.replace(" ", "_")).encode("utf-8"),
        "prop": "links",
        "pllimit": "max",
    }

    response = session.get(url=url, params=params)
    data = response.json()
    pages = data["query"]["pages"]

    pg_count = 1
    page_titles = []

    print("Page %d" % pg_count)
    for key, val in pages.items():
        for link in val["links"]:
            print(link["title"])

            page_titles.append(link["title"])

    while "continue" in data:
        plcontinue = data["continue"]["plcontinue"]
        params["plcontinue"] = plcontinue

        response = session.get(url=url, params=params)
        data = response.json()
        pages = data["query"]["pages"]

        pg_count += 1

        for key, val in pages.items():
            for link in val["links"]:
                if not (
                    (link["title"].startswith("Category"))
                    or (link["title"].startswith("Wikipedia"))
                    or (
                        link["title"].startswith("File")
                        or (link["title"].startswith("Template"))
                        or (link["title"].startswith("Portal"))
                        or (link["title"].startswith("Help"))
                        or (link["title"].startswith("Draft"))
                        or (link["title"].startswith("Module"))
                        or (link["title"].startswith("Book"))
                        or (link["title"].startswith("Talk"))
                        or (link["title"].startswith("List of"))
                        or (title in link["title"])
                    )
                ):
                    page_titles.append(link["title"])

    return page_titles


"""
gets Number of views in 2017-2018
Keyword arguments:
title -- title of wikipedia page
Return: number of views
"""


def get_views(title):
    url = (
        "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/"
        + (title.replace(" ", "_"))
        + "/monthly/2017010100/2018123100"
    )

    response = urlopen(url)

    response = response.read()

    response = response.decode("utf-8")

    data = json.loads(response)

    num_views = 0

    for month in data["items"]:
        num_views += month["views"]

    return num_views


def main():

    titles = get_links("Mexico")
    top_titles = {}
    for title in titles:
        try:
            top_titles[title] = get_views(title)
        except:
            pass

    # top_titles = sorted(top_titles.items(), key=lambda x: x[1], reverse=True)
    print(top_titles)


if __name__ == "__main__":
    main()
