import requests
import utils
import sys


def sendRequest(method, route):
    response = requests.request(method, route)
    return response.text


utils.startTestSetup(sys.argv[1], int(sys.argv[2]))

for x in range(0, int(sys.argv[2])):
    utils.savetofile(sendRequest("GET", "http://192.168.56.105:5000/mytxt"))
sendRequest("GET", "http://192.168.56.105:5000/mytxt")
utils.endTestSetup("RestClient")
# TODO LOGIC
