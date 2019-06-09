import pika
import utils
import sys

toSend = utils.readFile(sys.argv[1])
counter=0

utils.startServerTestSetup("AMQPPublisher",sys.argv[1],int(sys.argv[2]))

connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.2.2'))
channel = connection.channel()

channel.queue_declare(queue=" ".join(["AMQP",sys.argv[1],sys.argv[2]]))

while counter < int(sys.argv[2]):
    try:
        channel.basic_publish(exchange='',
                      routing_key=" ".join(["AMQP",sys.argv[1],sys.argv[2]]),
                      body=toSend)
        counter+=1
    except:
        pass

connection.close()