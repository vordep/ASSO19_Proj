import paho.mqtt.client as mqtt
import utils
import sys

broker_url = "10.0.2.2"
broker_port = 1883
utils.startTestSetup("MQTTSubscriber", sys.argv[1], int(sys.argv[2]))
counter = 0
client = mqtt.Client(client_id="".join(["MQTTSubs",sys.argv[1],sys.argv[2]]),clean_session=False)



def on_message(client, userdata, message):
    global counter
    utils.savetofile(message.payload.decode())
    counter += 1
    if counter >= int(sys.argv[2]):
        print('acabei')
        utils.endTestSetup('MQTTSubscriber')
        client.disconnect()
        sys.exit(0)


client.on_message = on_message
client.connect(broker_url, broker_port)

client.subscribe("".join(["MQTT",sys.argv[1],sys.argv[2]]), qos=2)
client.loop_forever()