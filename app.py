from flask import Flask
from Creadit_card.logger import logging
from Creadit_card.exception import CreaditException
import sys

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        pass
    except Exception as e:
        creadit = CreaditException(e, sys)
        logging.info(creadit.error_message)
        logging.info("We are testing logging module")
    return "HELLO DUDE"

if __name__ == "__main__":
    app.run(debug=True)