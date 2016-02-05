#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Path check plugin based on spell check plugin.'''

import sys
from zim.plugins import PluginClass, ObjectExtension, extends
from zim.signals import SIGNAL_AFTER
import logging

logger = logging.getLogger('zim.plugins.pathcheck')

class PathChecker(PluginClass):

	plugin_info = {
		'name': _("Path Checker"), # T: plugin name
		'description': _("Checks for broken paths in links."), # T: plugin description
		'author': "Nathaniel Beaver",
	}

with open('/tmp/pathchecker.log', 'a') as mylog:
	mylog.write('running from '+sys.argv[0]+'\n')

@extends('PageView')
class PageViewExtension(ObjectExtension):

	def __init__(self, plugin, pageview):
		self.plugin = plugin
		self.connectto(obj=pageview.ui, signal='open-page', handler=self.on_open_page, order=SIGNAL_AFTER)

	def on_open_page(self, ui, page, path):
		with open('/tmp/pathchecker.log', 'a') as mylog:
			mylog.write('on_open_page:' + page.name + '\n')
