from flask import Flask
from flask import request
import utils
import sys
app = Flask(__name__)

toSend = utils.readFile(sys.argv[1])
counter=0
utils.startServerTestSetup("RestServer",sys.argv[1],int(sys.argv[2]))

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/mytxt')
def mytxt():
    global counter
    counter+=1
    if counter>int(sys.argv[2]):
        shutdown_server()
        return ""
    return toSend

app.run("0.0.0.0", 5000)