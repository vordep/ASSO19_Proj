import requests
import utils
import sys
import time


def sendRequest(method, route):
    try:
        response = requests.request(method, route)
        return response.text
    except:
        time.sleep(1)
        return ""


utils.startTestSetup("RestClient",sys.argv[1], int(sys.argv[2]))

for x in range(0, int(sys.argv[2])):
    response = ""
    while response == "":
        response = sendRequest("GET", "http://192.168.56.105:5000/mytxt")   
    utils.savetofile(response)

utils.endTestSetup("RestClient")

try:
    requests.request("GET", "http://192.168.56.105:5000/mytxt")
except:
    pass
# TODO LOGIC
