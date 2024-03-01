from .data_fetch import fetch_wikipedia_page_details
from .database_interaction import add_wikipedia_pages


def run():
    urls = [
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Flask_(web_framework)',
        'https://en.wikipedia.org/wiki/Canada',
    ]
    # Example URLs
    for url in urls:
        page_data = fetch_wikipedia_page_details(url)
        add_wikipedia_pages(page_data)
