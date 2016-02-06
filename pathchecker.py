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
		'name': "Path Checker", # T: plugin name
		'description': "Checks for broken paths in links.", # T: plugin description
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
		mylog = open('/tmp/pathchecker.log', 'a')
		mylog.write('on_open_page:' + page.name + '\n')
		mylog.write('on_open_page: page is ' + str(type(page)) + '\n')
		mylog.write('on_open_page: ui is ' + str(type(ui)) + '\n')
		for link_type, href, attrib in page.get_links():
			mylog.write('link_type = '+ str(link_type) + ', href = ' + href + ', attrib = ' + str(attrib) + '\n')
		mylog.close()
