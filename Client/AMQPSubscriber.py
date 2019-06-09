import pika
import sys
import utils

utils.startTestSetup("AMQPSubscriber", sys.argv[1], int(sys.argv[2]))
counter = 0

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='10.0.2.2'))
channel = connection.channel()

channel.queue_declare(queue=" ".join(["AMQP",sys.argv[1],sys.argv[2]]))


def callback(ch, method, properties, body):
    global counter
    utils.savetofile(body)
    counter += 1
    if counter >= int(sys.argv[2]):
        channel.stop_consuming()
        utils.endTestSetup('AMQPSubscriber')

    # TODO LOGIC


channel.basic_consume(queue=" ".join(["AMQP",sys.argv[1],sys.argv[2]]),
                      auto_ack=True,
                      on_message_callback=callback)


channel.start_consuming()
