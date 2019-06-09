import paho.mqtt.client as mqtt  # import the client1
import utils
import sys

toSend = utils.readFile(sys.argv[1])
counter=0
counter2=0
broker_url = "10.0.2.2"
broker_port = 1883
utils.startServerTestSetup("MQTTPublisher",sys.argv[1],int(sys.argv[2]))

def publish_handler(client,userdata,result):
    global counter2
    counter2+=1
    if counter2 >= int(sys.argv[2]):
        sys.exit(0)

client = mqtt.Client()

client.connect(broker_url, broker_port)

while counter < int(sys.argv[2]):
    try:
        client.publish(topic=" ".join(["MQTT",sys.argv[1],sys.argv[2]]), payload=toSend, qos=0, retain=False) 
        counter+=1
    except:
        pass

client.on_publish = publish_handler
client.loop_forever()
