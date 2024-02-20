from flask import Flask
from models import db, WikipediaPage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Iwantajob69$@localhost:3306/practice_1'
db.init_app(app)

# Create tables before running the application
with app.app_context():
    db.create_all()

@app.route('/')
def add_page():
    with app.app_context():
        page = WikipediaPage(title='Example Wikipedia Page', link='wikipedia.com', surrounding_links='Link 1, Link 2, Link 3')
        db.session.add(page)
        db.session.commit()
    return 'Page added successfully!'

@app.route('/delete')
def delete_page():
    with app.app_context():
        page = WikipediaPage.query.filter_by(title='Example Wikipedia Page').first()
        db.session.delete(page)
        db.session.commit()
    return 'Page deleted successfully!'

if __name__ == '__main__':
    app.run(debug=True)