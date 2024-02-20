from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:Iwantajob69$@localhost:3306/practice_1"

db.init_app(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))

with app.app_context():
    db.create_all()

@app.route("/")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.id)).scalars()
    return render_template("user/list.html", users=users)
