from flask import Flask, render_template
from flask_frozen import Freezer
import feedparser

app = Flask(__name__)
freezer = Freezer(app)
app.config.update({
    "FREEZER_DESTINATION": "docs/",
    "FREEZER_BASE_URL": "https://ketozhang.github.com/frontpage/"
})


class Resources:
    xkcd = feedparser.parse("https://xkcd.com/rss.xml")["items"][0]
    arxiv = feedparser.parse("https://arxiv.org/rss/astro-ph.CO")
    arxiv_articles = arxiv["items"]


@app.route("/")
def home():
    return render_template("home.html", resources=Resources())


if __name__ == "__main__":
    freezer.freeze()
