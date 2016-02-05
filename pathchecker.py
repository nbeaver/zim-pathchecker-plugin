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
		self.connectto_all(pageview.ui, ('open-page'), order=SIGNAL_AFTER)

	def on_open_page(self, ui, page, path):
		with open('/tmp/pathchecker.log', 'a') as mylog:
			mylog.write(page.name + '\n')

@extends('Notebook')
class NotebookExtension(ObjectExtension):

	def __init__(self, plugin, notebook):
		self.plugin = plugin
		self.connectto_all(notebook,
			('deleted-page', 'stored-page'), order=SIGNAL_AFTER)

	def on_deleted_page(self, page, path):
		logger.debug("Deleted page: %s", page.name)

	def on_stored_page(self, page, path):
		logger.debug("Modified page: %s", page.name)
