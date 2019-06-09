import paho.mqtt.client as mqtt
import utils
import sys

broker_url = "10.0.2.2"
broker_port = 1883
utils.startTestSetup("MQTTSubscriber", sys.argv[1], int(sys.argv[2]))
counter = 0
client = mqtt.Client()



def on_message(client, userdata, message):
    global counter
    print('recebo')
    utils.savetofile(message.payload.decode())
    counter += 1
    if counter >= int(sys.argv[2]):
        utils.endTestSetup('MQTTSubscriber')
        sys.exit(0)


client.on_message = on_message
client.connect(broker_url, broker_port)

client.subscribe(" ".join(["MQTT",sys.argv[1],sys.argv[2]]), qos=0)
client.loop_forever()