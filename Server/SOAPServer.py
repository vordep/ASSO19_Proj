import SOAPpy
import utils
import sys
import signal

toSend = utils.readFile(sys.argv[1])
counter=0
utils.startServerTestSetup("SoapServer",sys.argv[1],int(sys.argv[2]))
server = SOAPpy.SOAPServer(("0.0.0.0", 5001))

def mytxt():
    global counter
    counter+=1
    if counter>=int(sys.argv[2]):
        print('exiting')
        signal.signal(signal.SIGALRM, utils.kill_server)
        signal.setitimer(signal.ITIMER_REAL, 1)
    return toSend

server.registerFunction(mytxt)
server.serve_forever()