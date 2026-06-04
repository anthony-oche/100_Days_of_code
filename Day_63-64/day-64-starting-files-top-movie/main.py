from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
db = SQLAlchemy(model_class= Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True, default=0.0)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True, default="")
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


#API PARAMS
url = "https://api.themoviedb.org/3/movie"
TOKEN = ""

header = {
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN}",
}


#Todo 2: form for edit
class FormEdit(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")



#Todo 4: Add movies
class AddMovies(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Done")



@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    rate_movie = FormEdit()
    movie_id = request.args.get("id")
    movie_to_rate = db.get_or_404(Movie, movie_id)
    if rate_movie.validate_on_submit():
        rating = rate_movie.rating.data
        review = rate_movie.review.data

        movie_to_rate.rating = rating
        movie_to_rate.review = review
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=rate_movie, movie=movie_to_rate)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))



@app.route("/add", methods=["GET", "POST"])
def add():
    add_movies = AddMovies()
    if add_movies.validate_on_submit():
        query = {
            "query": add_movies.title.data
        }

        response = requests.get("https://api.themoviedb.org/3/search/movie", params=query, headers=header)
        result = response.json()["results"]
        return render_template('select.html', all_movies=result)
    return render_template("add.html", form=add_movies)



@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{url}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": "eee2cd37c49332f474bf388ca7323546", "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))




if __name__ == '__main__':
    app.run(debug=True)


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )



# new_movie = Movie(
#         title=movie.title.data,
#         year=movie.year.data,
#         description=movie.description.data,
#         rating=movie.rating.data,
#         ranking=movie.ranking.data,
#         review=movie.review.data,
#         img_url=movie.img_url.data
#     )
#     db.session.add(new_movie)
#     db.session.commit()

