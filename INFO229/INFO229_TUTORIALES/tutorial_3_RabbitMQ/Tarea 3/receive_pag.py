#!/usr/bin/env python
import pika
import wikipedia
import pageviewapi

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.exchange_declare(exchange='logs', exchange_type='fanout')


result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue


channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)
    number=pageviewapi.per_article('en.wikipedia', body, '20151119', '20151120',access='all-access', agent='all-agents', granularity='daily')
    number2=number(u'items')
    number3=number2[0]
    number4=number3(u'views')
    print("Las visitas de la pagina son: ",number4)

    
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
