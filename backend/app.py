from data_fetch import fetch_wikipedia_page_details
from database_interaction import add_wikipedia_page

def main():
    urls = [
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Flask_(web_framework)'
    ]  # Example URLs
    for url in urls:
        page_data = fetch_wikipedia_page_details(url)
        add_wikipedia_page(page_data)

if __name__ == "__main__":
    main()