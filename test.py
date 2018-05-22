#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 10:27
# @Author  : long.zhang
# @Contact : long.zhang@opg.global
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# @Desc    :
#coding: utf-8
'''
循环调度:
使用工作队列的一个好处就是它能够并行的处理队列。如果堆积了很多任务，我们只需要添加更多的工作者（workers）就可以了，扩展很简单。
若有多个消费者，即打开多个终端，运行消费者程序。默认来说，RabbitMQ会按顺序得把消息发送给每个消费者（consumer）。平均每个消费者都会收到同等数量得消息。这种发送消息得方式叫做——轮询（round-robin）。
'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True) #durable=True　表示为了不让队列消失，需要把队列声明为持久化

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                        delivery_mode = 2,    #我们需要把我们的消息也要设为持久化——将delivery_mode的属性设为2。
                      ))

print(" [x] Sent %r" % (message,))
connection.close()
