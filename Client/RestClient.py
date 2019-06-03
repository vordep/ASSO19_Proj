import requests


def sendRequest(method, route):
    response = requests.request(method, route)
    return response.text


print(sendRequest("GET", "http://127.0.0.1:5000/mytxt"))
# TODO LOGIC
