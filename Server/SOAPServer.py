import SOAPpy
import utils
import sys

toSend = utils.readFile(sys.argv[1])
counter=0
utils.startServerTestSetup("SoapServer",sys.argv[1],int(sys.argv[2]))

def mytxt():
    global counter
    counter+=1
    if counter>int(sys.argv[2]):
        sys.exit(0)
        return ""
    return toSend


server = SOAPpy.SOAPServer(("0.0.0.0", 5001))
server.registerFunction(mytxt)
server.serve_forever()