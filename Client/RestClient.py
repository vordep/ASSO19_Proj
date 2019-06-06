import requests


def sendRequest(method, route):
    response = requests.request(method, route)
    return response.text


print(sendRequest("GET", "http://192.168.56.105:5000/mytxt"))
# TODO LOGIC
