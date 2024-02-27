import random as rand

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from models import WikipediaPage, db

app = Flask(__name__)
CORS(app, origins="*")
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+mysqlconnector://root:Iwantajob69$@localhost:3306/practice_1"
)
db.init_app(app)

# Create tables before running the application
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    pages = db.session.execute(
        db.select(WikipediaPage).order_by(WikipediaPage.id)
    ).fetchone()
    print(pages)
    return render_template("home.html", users=pages)


@app.route("/add")
def add_page():
    with app.app_context():
        page = WikipediaPage(
            title="Canada",
            link="https://en.wikipedia.org/wiki/Canada",
            surrounding_links="https://en.wikipedia.org/wiki/United_States,https://en.wikipedia.org/wiki/Mexico",
        )
        db.session.add(page)
        page = WikipediaPage(
            title="United States",
            link="https://en.wikipedia.org/wiki/United_States",
            surrounding_links="https://en.wikipedia.org/wiki/Canada,https://en.wikipedia.org/wiki/Mexico",
        )
        db.session.add(page)
        page = WikipediaPage(
            title="Mexico",
            link="https://en.wikipedia.org/wiki/Mexico",
            surrounding_links="https://en.wikipedia.org/wiki/United_States,https://en.wikipedia.org/wiki/Canada",
        )
        # page = WikipediaPage(title='Example Wikipedia Page', link='wikipedia.com', surrounding_links='Link 1, Link 2, Link 3')
        db.session.add(page)
        db.session.commit()
    return "Page added successfully!"


@app.route("/delete")
def delete_page():
    with app.app_context():
        page = WikipediaPage.query.filter_by(title="Example Wikipedia Page").first()
        db.session.delete(page)
        db.session.commit()
    return "Page deleted successfully!"


@app.route("/get_wikis")
def hello():
    wikiList = WikipediaPage.query.all()

    wikis = []
    i = 0
    for wiki in wikiList:
        wikis.append(
            {
                "id": i,
                "title": wiki.title,
                "link": wiki.link,
                "surrounding_links": wiki.surrounding_links,
            }
        )
        i += 1

    return jsonify({"wikis": wikis})


@app.route("/get_wiki_name")
def get_wiki_name():
    wikiList = WikipediaPage.query.all()

    wikis = []
    i = 0
    for wiki in wikiList:
        wikis.append({"value": wiki.title, "label": wiki.title})
    return jsonify({"wikis": wikis})


# just used to test the connection to front end
@app.route("/check_wiki", methods=["POST"])
def check_wiki():
    data = request.get_json()

    print(f"type is: {type(data)}, data is: {data} title' in data: {data['wiki']}")

    # return jsonify({'guess': data['wiki']})

    if data["wiki"] == "Canada":
        return jsonify({"guess": 1})
    else:
        return jsonify({"guess": 0})


if __name__ == "__main__":
    app.run(debug=True)
