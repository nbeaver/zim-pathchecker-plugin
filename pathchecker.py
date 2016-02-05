#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Path check plugin based on spell check plugin.'''

import sys
from zim.plugins import PluginClass

class PathChecker(PluginClass):

	plugin_info = {
		'name': _("Path Checker"), # T: plugin name
		'description': _("Checks for broken paths in links."), # T: plugin description
		'author': "Nathaniel Beaver",
	}

with open('/tmp/pathchecker.log', 'a') as mylog:
	mylog.write('running from '+sys.argv[0]+'\n')
