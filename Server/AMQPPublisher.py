import pika
import utils

toSend = utils.readFile()
connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.2.2'))
channel = connection.channel()

channel.queue_declare(queue='mytxt')

channel.basic_publish(exchange='',
                      routing_key='mytxt',
                      body=toSend)


connection.close()
