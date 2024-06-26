from wikis.models import WikiPage


def add_wikipedia_pages(page_data):
    links_str = ','.join(page_data['links'])
    categories_str = ','.join(page_data['categories'])
    links_titles_str = ','.join(page_data['links_titles'])

    p = WikiPage(
        title=page_data['title'],
        surrounding_links=links_str,
        surrounding_titles=links_titles_str,
        link=page_data['url'],
        categories=categories_str,
    )
    p.save()
    print(f"Added page: {page_data['title']}")
