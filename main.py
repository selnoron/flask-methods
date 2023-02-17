#flask 
from flask import (
    Flask,
    render_template
)
from flask.app import \
    Flask as FlaskApp

#requests
import requests
from requests import Response

app: FlaskApp = Flask(__name__)
URL = (
    'https://api.hearthstonejson.com/v1/'
    '121569/ruRU/cards.collectible.json'
)
hearthstone_cards: list[dict] = []

@app.route("/")
def main_page() -> Response:
    return render_template(
        template_name_or_list= \
            'index.html',
            hrth=hearthstone_cards
    )
     
@app.route("/<id>")
def card_page(id: str) -> FlaskApp:
    if int(id) > len(hearthstone_cards):
        return "Doesnt exist"
    return render_template(
        "card.html",
        card=hearthstone_cards[int(id)]
    )

if __name__ == '__main__':
    response: requests.Response = \
        requests.get(
            URL
        )
    data: list[dict] = response.json()
    hearthstone_cards = data
    app.run(
        port=8080,
        debug=True
    )   
