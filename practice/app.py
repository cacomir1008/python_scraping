import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    # """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    with urlopen("http://feeds.feedburner.com/hatena/b/hotentry") as res:
        html = res.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        items = soup.select("item")
        shuffle(items)
        item = items[0]
        print(item)

    return json.dumps({
        "content" : item.find("title").string,
        "link" : item.get('rdf:about')
    })

@app.route("/api/mental_article")
def api_mental_article():
    with urlopen("https://news.yahoo.co.jp/") as res:
        html = res.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        topics = soup.select(".sc-ksYbfQ .sc-hmzhuo")
        shuffle(topics)
        topic = topics[0]
        print(topic)

    
    return json.dumps({
        # "content" : topic.find(".sc-hmzhuo"),
        "content" : topic.string,
        "link" : topic.get('href')
    })

    pass

if __name__ == "__main__":
    app.run(debug=True, port=5004)
