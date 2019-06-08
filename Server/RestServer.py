from flask import Flask
import utils
import sys
app = Flask(__name__)

toSend = utils.readFile()
counter=0
utils.startServerTestSetup(32,32)

@app.route('/mytxt')
def mytxt():
    global counter
    if counter==33:
        sys.exit(0)
    counter+=1
    return toSend

app.run("0.0.0.0", 5000)