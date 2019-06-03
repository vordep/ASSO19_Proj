import paho.mqtt.client as mqtt

broker_url = "localhost"
broker_port = 1883


def on_connect(client, userdata, flags, rc):
    print(rc)


def on_message(client, userdata, message):
    print(message.payload.decode())


client = mqtt.Client()
client.on_connect = on_connect
# To Process Every Other Message
client.on_message = on_message

client.connect(broker_url, broker_port)

client.subscribe("mytxt2", qos=1)


client.loop_forever()
