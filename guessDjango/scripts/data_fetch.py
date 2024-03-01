import requests
from bs4 import BeautifulSoup


def remove_meta_cats(cats, title):
    """meow meow meow (I HATE THIS SO MUCH)
    remove the categories,  that have the title in it
    meow meow meow
    """
    non_meta_cats = []
    for cat in cats:
        if not (title in cat):
            non_meta_cats.append(cat)
    return non_meta_cats


def fetch_wikipedia_page_details(url):
    """Returns categories and links from Wikipedia.
    Excludes the sections given in <exclude_sections>
    """
    exclude_sections = [
        "See also",
        "References",
        "External links",
        "Further reading",
        "Notes",
        "Bibliography",
    ]

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the title of the Wikipedia page
    title = (
        soup.find("h1", id="firstHeading").text
        if soup.find("h1", id="firstHeading")
        else "No Title Found"
    )

    all_links = []

    # Exclude links with these prefixes
    exclude_prefixes = [
        "/wiki/Special:",
        "/wiki/Category:",
        "/wiki/Portal:",
        "/wiki/Help:",
        "/wiki/File:",
        "/wiki/Template:",
        "/wiki/Wikipedia:",
    ]
    # Find links from the introductory section
    parser_output = soup.find("div", class_="mw-parser-output")
    if parser_output:
        intro_section = parser_output.find("p")
        if intro_section:
            all_links.extend(
                [
                    "https://en.wikipedia.org" + a["href"]
                    for a in intro_section.find_all("a", href=True)
                    if a["href"].startswith("/wiki/")
                    and not any(
                        a["href"].startswith(prefix) for prefix in exclude_prefixes
                    )
                ]
            )

    # Find subsections and their links, avoiding excluded sections
    subsections = soup.find_all("span", class_="mw-headline")
    for subsection in subsections:
        if subsection.text not in exclude_sections:
            parent_section = subsection.find_parent(
                "h2" if subsection.name == "span" else "h3"
            )
            if parent_section:
                links = [
                    "https://en.wikipedia.org" + a["href"]
                    for a in parent_section.find_all_next("a", href=True)
                    if a["href"].startswith("/wiki/")
                    and not any(
                        a["href"].startswith(prefix) for prefix in exclude_prefixes
                    )
                ]
                all_links.extend(links)
                next_header = parent_section.find_next_sibling(["h2", "h3"])
                if next_header and next_header.find("span", class_="mw-headline"):
                    break

    # Deduplicate the links list
    all_links = list(set(all_links))

    # grab categories
    categories = []
    # cat links goes meow
    cat_links = soup.find("div", {"id": "mw-normal-catlinks"})
    if cat_links:
        categories = [
            a.text
            for a in cat_links.find_all("a", href=True)
            if a["href"].startswith("/wiki/Category:")
        ]

    categories = list(set(categories))
    categories = remove_meta_cats(categories, title)

    # Construct the return dictionary
    page_data = {
        "title": title,
        "links": all_links,
        "url": url,
        "categories": categories,
    }

    return page_data
