from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class WikipediaPage(db.Model):
    __tablename__ = 'wikipedia_page'  # Specify the table name
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    surrounding_links = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)