from flask import Flask
import utils
import sys
app = Flask(__name__)

toSend = utils.readFile(sys.argv[2])
counter=0
utils.startServerTestSetup(sys.argv[1],int(sys.argv[2]))

@app.route('/mytxt')
def mytxt():
    global counter
    counter+=1
    if counter==32:
        utils.endServerTestSetup()
    return toSend

app.run("0.0.0.0", 5000)