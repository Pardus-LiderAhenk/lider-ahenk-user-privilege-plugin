#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Style Guide is PEP-8
https://www.python.org/dev/peps/pep-0008/
"""

"""
Some operations of plugin work with using different command (or process) on different machine types,
 desktop environments, kernel versions, etc, ...
You have to create python classes which includes implementation of every action, for every dependent feature of system.
These classes have to be in api folder. You can create and serve instances of environment dependent operations to your
plugin from here. Ahenk Core provides necessary values of system like machine type, kernel version,
desktop environment,...
Naming of classes expected such as below examples:
<featureA1_featureB1.py>

kde_ltsp.py
gnome_ltsp.py
kde_x2go.py
gnome_x2go.py
default_ltsp.py
default_x2go.py
kde_default.py
gnome_default.py
default_default.py
(It depends to number of kind of variation)

You can access some useful values using these statements:
SystemInfo.get_X(),SystemInfo.get_kernel(),SystemInfo.get_machine_type(),...
When you create valid instance according to running system environments, plugin works with valid actions.
"""