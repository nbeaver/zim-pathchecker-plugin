# -*- coding: utf-8 -*-

# Copyright 2008 Jaap Karssenberg <jaap.karssenberg@gmail.com>

'''Path check plugin based on spell check plugin.'''

import os
import gobject

from zim.config import get_environ
from zim.plugins import PluginClass
from zim.gui.widgets import ErrorDialog
from zim.signals import SIGNAL_AFTER

ui_xml = '''
<ui>
	<menubar name='menubar'>
		<menu action='tools_menu'>
			<placeholder name='page_tools'>
				<menuitem action='toggle_pathcheck'/>
			</placeholder>
		</menu>
	</menubar>
	<toolbar name='toolbar'>
		<placeholder name='tools'>
			<toolitem action='toggle_pathcheck'/>
		</placeholder>
	</toolbar>
</ui>
'''

ui_toggle_actions = (
	# name, stock id, label, accelerator, tooltip, initial state, readonly
	('toggle_pathcheck', 'path-check', _('Check _paths'), 'F8', 'Path check', False, True), # T: menu item
)

class PathChecker(PluginClass):

	plugin_info = {
		'name': _('Path Checker'), # T: plugin name
		'description': _('''\
Adds path checking.

'''), # T: plugin description
		'author': 'Nathaniel Beaver',
		'help': 'Plugins:Path Checker',
	}

	plugin_preferences = (
		('language', 'string', 'Default Language', ''),
	)

	def __init__(self, ui):
		PluginClass.__init__(self, ui)
		self.uistate.setdefault('active', False)
		if self.ui.ui_type == 'gtk':
			self.ui.add_toggle_actions(ui_toggle_actions, self)
			self.ui.add_ui(ui_xml, self)
			self.connectto(self.ui, 'open-page', order=SIGNAL_AFTER)

	def toggle_patchcheck(self, enable=None):
		action = self.actiongroup.get_action('toggle_patchcheck')
		if enable is None or enable != action.get_active():
			action.activate()
		else:
			self.do_toggle_patchcheck(enable=enable)

	def do_toggle_patchcheck(self, enable=None):
		if enable is None:
			action = self.actiongroup.get_action('toggle_patchcheck')
			enable = action.get_active()

		textview = self.ui.mainwindow.pageview.view

		self.uistate['active'] = enable
		return False # we can be called from idle event

	def on_open_page(self, ui, page, record):
		# Assume the old object is detached by hard coded
		# hook in TextView, just attach a new one.
		# Use idle timer to avoid lag in page loading.
		# This hook also synchronizes the state of the toggle with
		# the uistate when loading the first page
		if self.uistate['active']:
			gobject.idle_add(self.toggle_patchcheck, True)

