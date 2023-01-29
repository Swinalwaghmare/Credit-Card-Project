from flask import Flask
from Creadit_card.logger import logging

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    logging.info("We are testing logging module")
    return "HELLO DUDE"

if __name__ == "__main__":
    app.run(debug=True)