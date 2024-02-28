from sqlalchemy.exc import SQLAlchemyError
from models import SessionLocal, WikipediaPage

def add_wikipedia_page(page_data):
    session = SessionLocal()
    try:
        links_str = ', '.join(page_data['links'])
        new_page = WikipediaPage(title=page_data['title'], surrounding_links=links_str, link=page_data['url'])
        session.add(new_page)
        session.commit()
        print(f"Added page: {page_data['title']}")
    except SQLAlchemyError as e:
        print(f"Error adding page {page_data['title']}: {e}")
        session.rollback()
    finally:
        session.close()