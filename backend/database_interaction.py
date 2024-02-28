from models import WikipediaPage, Session

def add_wikipedia_page(page_data):
    session = Session()
    # Since 'links' is now a list, convert it to a string for storage
    links_str = ', '.join(page_data['links'])
    new_page = WikipediaPage(title=page_data['title'], surrounding_links=links_str, link=page_data['url'])
    session.add(new_page)
    try:
        session.commit()
        print(f"Added page: {page_data['title']}")
    except Exception as e:
        print(f"Error adding page {page_data['title']}: {e}")
        session.rollback()
    finally:
        session.close()