from flask import Flask, render_template
import requests
import datetime

today = datetime.datetime.now()
year = today.year

BLOG_ENDPOINT = "https://api.npoint.io/674f5423f73deab1e9a7"


app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get(url=BLOG_ENDPOINT)
    data = response.json()
    return render_template("index.html", all_posts=data, year=year)


@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def get_post(index):
    response = requests.get(url=BLOG_ENDPOINT)
    all_posts = response.json()[index - 1]
    return render_template("post.html", post=all_posts)






if __name__ == "__main__":
    app.run(debug=True)


