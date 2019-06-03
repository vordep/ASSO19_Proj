from flask import Flask
import utils
app = Flask(__name__)

toSend = utils.readFile()


@app.route('/mytxt')
def mytxt():
    return toSend
