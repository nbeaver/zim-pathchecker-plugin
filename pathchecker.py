#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Path check plugin based on spell check plugin.'''

from zim.plugins import PluginClass

class PathChecker(PluginClass):

	plugin_info = {
		'name': _('Path Checker'),
		'description': _('''\
Adds path checking.
'''),
		'author': 'Nathaniel Beaver',
	}
