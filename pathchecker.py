#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Path check plugin based on spell check plugin.'''

import sys
import os.path
import urlparse

from zim.plugins import PluginClass, ObjectExtension, extends
from zim.signals import SIGNAL_AFTER
import zim.formats
import zim.parsing
import logging

import inspect

def lineno():
    """Returns the current line number in our program."""
    return str(inspect.currentframe().f_back.f_lineno)

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

	def get_links(self, page):
		'''Generator for links in the page content

		This method gives the raw links from the content, if you want
		nice L{Link} objects use
		L{index.list_links()<zim.index.Index.list_links()>} instead.

		@returns: yields a list of 3-tuples C{(type, href, attrib)}
		where:
		  - C{type} is the link type (e.g. "page" or "file")
		  - C{href} is the link itself
		  - C{attrib} is a dict with link properties
		'''
		# FIXME optimize with a ParseTree.get_links that does not
		#       use Node
		mylog = open('/tmp/pathchecker2.log', 'a')
		mylog.write(lineno()+'\n')
		tree = page.get_parsetree()
		if tree:
			for elt in tree.findall(zim.formats.LINK):
				href = elt.attrib.pop('href')
				type = zim.parsing.link_type(href)
				yield type, href, elt.attrib

			for elt in tree.findall(zim.formats.IMAGE):
				if not 'href' in elt.attrib:
					continue
				href = elt.attrib.pop('href')
				type = zim.parsing.link_type(href)
				yield type, href, elt.attrib

	def on_open_page(self, ui, page, path):
		mylog = open('/tmp/pathchecker.log', 'a')
		mylog.write(lineno()+'\n')
		for link_type, href, node in self.get_links(page):
			#mylog.write('link:' + href + '\n')
			if link_type == 'file':
				if href.startswith('file://'):
					path = urlparse.urlparse(href).path
				else:
					path = os.path.expanduser(href)
				if not os.path.exists(path):
					mylog.write('broken link:' + path + '\n')
		mylog.close()
