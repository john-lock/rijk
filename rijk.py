from flask import Flask, render_template
import json
import requests
import os
from random import randint

app = Flask(__name__)
APIKEY = os.environ['APIKEY']


@app.route('/', methods=['GET'])
def random():
    # Api sets cap at 10000
    P = str(randint(1, 10000))
    r = requests.get(
        "https://www.rijksmuseum.nl/api/en/collection/?key=" + APIKEY + "&format=json&imgonly=True&ps=1&p=" + P
    )
    rjson = json.loads(r.text)

    artimg = rjson['artObjects'][0]['webImage']['url']
    arttitle = rjson['artObjects'][0]['title']
    artlongtitle = rjson['artObjects'][0]['longTitle']
    artist = rjson['artObjects'][0]['principalOrFirstMaker']
    artlink = rjson['artObjects'][0]['links']['web']

    return render_template(
        'index.html',
        artimg=artimg, arttitle=arttitle, artlongtitle=artlongtitle, artist=artist, artlink=artlink
    )


if __name__ == '__main__':
    app.run()
