import SOAPpy
import time
import utils
import sys

utils.startTestSetup("SoapClient",sys.argv[1], int(sys.argv[2]))

server = SOAPpy.SOAPProxy("http://192.168.56.105:5001/")

for x in range(0, int(sys.argv[2])):
    response = ""
    while response == "":
        try:
            response = server.mytxt()
        except:
            time.sleep(1)
            response = ""
    utils.savetofile(response)

utils.endTestSetup("SoapClient")
print('exiting')
sys.exit(0)
# TODO LOGIC

