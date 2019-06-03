import paho.mqtt.client as mqtt  # import the client1
import utils

toSend = utils.readFile()


broker_url = "localhost"
broker_port = 1883

client = mqtt.Client()

client.connect(broker_url, broker_port)

client.publish(topic="mytxt2", payload=toSend, qos=1, retain=False)
client.loop_forever()
