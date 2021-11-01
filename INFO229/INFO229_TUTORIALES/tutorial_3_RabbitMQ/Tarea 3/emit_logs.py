#!/usr/bin/env python
import pika
import sys
import wikipedia

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "Chile"


channel.basic_publish(exchange='logs', routing_key='', body=message)

print(" [x] Sent %r" % message)

connection.close()
