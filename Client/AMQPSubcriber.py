import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='mytxt')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ##TODO LOGIC

channel.basic_consume(queue='mytxt',
                    auto_ack=True,
                    on_message_callback=callback)


channel.start_consuming()