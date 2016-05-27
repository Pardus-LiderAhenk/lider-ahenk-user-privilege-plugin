#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Style Guide is PEP-8
https://www.python.org/dev/peps/pep-0008/
"""

from base.plugin.AbstractCommand import AbstractCommand


class PluginName(AbstractCommand):
    def __init__(self, data, context):
        super(PluginName, self).__init__()
        self.data = data
        self.context = context

    def handle_policy(self):
        print('Handling policy')
        #self.context.create_response(code=MessageCode.POLICY_PROCESSED.value, message='Message about process result', data=data, content_type=ContentType.APPLICATION_JSON.value)
        #self.context.get('something')
        #self.context.execute('terminal command')
        # etc ...
        # TODO plugin policy works here


def handle_policy(profile_data, context):
        # Do what ever you want here
    # You can create command class but it is not necessary
    # You can use directly this method.
    print('Sample Plugin Policy')
    print('Profile Data : {}'.format(str(profile_data)))
    plugin = PluginName(profile_data, context)
    plugin.handle_policy()
