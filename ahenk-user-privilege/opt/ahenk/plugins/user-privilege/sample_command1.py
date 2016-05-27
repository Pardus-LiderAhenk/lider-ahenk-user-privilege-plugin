#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Style Guide is PEP-8
https://www.python.org/dev/peps/pep-0008/
"""

from base.plugin.AbstractCommand import AbstractCommand


class SampleTask1(AbstractCommand):
    def __init__(self, task, context):
        super(SampleTask1, self).__init__()
        self.task = task
        self.context = context

    def handle_task(self):
         print('Handling task')
        #self.context.put('name', 'anything')
        #self.context.get('something')
        # TODO plugin task works here


def handle_task(task, context):
    # Do what ever you want here
    # You can create command class but it is not necessary
    # You can use directly this method.
    print('Sample Task - CommandId 1')
    print('Task Data : {}'.format(str(task)))
    my_task = SampleTask1(task, context)
    my_task.handle_task()
