import SOAPpy
import utils
toSend = utils.readFile()

def mytxt():
    return toSend


server = SOAPpy.SOAPServer(("localhost", 5001))
server.registerFunction(mytxt)
server.serve_forever()
