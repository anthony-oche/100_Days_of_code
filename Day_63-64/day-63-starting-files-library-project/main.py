from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = db.session.execute(db.select(Books).order_by(Books.title))
    result = all_books.scalars()
    return render_template("index.html", books=result)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Books(title=request.form["bookname"], author=request.form["author"],
                                     rating=request.form["rating"])

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("add"))


    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():

    if request.method == "POST":
        book_id = request.form["id"]
        rate_update = db.get_or_404(Books, book_id)
        rate_update.rating = request.form.get("rating")
        db.session.commit()

        return redirect(url_for("home"))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Books, book_id)
    return render_template("edit.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

