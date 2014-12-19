#!/usr/bin/env python
# coding: utf-8

import os
import subprocess

from gi.repository import Gtk

class EclipseProfileSelector:
	
	PROFILE_TEMPLATE = "<big><b>{name}</b></big>\n<span size='2000'> </span>\n<small>{path}</small>"
	PROFILE_DIRECTORY = os.path.expanduser("~/.eclipse-profiles")
	
	def __init__(self):
		
		if not os.path.isdir(EclipseProfileSelector.PROFILE_DIRECTORY):
			os.mkdir(EclipseProfileSelector.PROFILE_DIRECTORY)
		
		builder = Gtk.Builder()
		builder.add_from_file("eclipse-profile-selector.glade")
		builder.connect_signals(self)
		
		self.store = Gtk.ListStore(str, str)
		self.launchButton = builder.get_object("launchButton")
		self.list  = builder.get_object("profileView")
		self.list.set_model(self.store)
		
		## Profile Creator
		self.profileCreator = builder.get_object("profileCreatorDialog")
		self.profileNameInput = builder.get_object("newProfileName")
		self.addButton = builder.get_object("addButton")
	
		column1 = Gtk.TreeViewColumn("path", Gtk.CellRendererText(visible = False))
		self.list.append_column(column1)
		
		column2 = Gtk.TreeViewColumn("profile", Gtk.CellRendererText(xpad = 6, ypad = 6), markup = 0)
		self.list.append_column(column2)
		
		self.add_content()
		
		window = builder.get_object("profileSelectionWindow")
		window.show_all()


	def add_content(self):
		self.store.clear()
		
		for profile in os.listdir(EclipseProfileSelector.PROFILE_DIRECTORY):
			self.store.append([
				EclipseProfileSelector.PROFILE_TEMPLATE.format(
					name = profile,
					path = os.path.join(EclipseProfileSelector.PROFILE_DIRECTORY, profile)
				),
				profile
			])
		
		self.launchButton.set_sensitive(len(self.store) > 0)
	
	
	def launch_eclipse(self, *widget):
		_, it = self.list.get_selection().get_selected()
		profile = os.path.join(
			EclipseProfileSelector.PROFILE_DIRECTORY,
			self.store.get_value(it, 1)
		)
		
		configuration = os.path.join(profile, "configuration")
		workspace = os.path.join(profile, "workspace")
		
		subprocess.Popen(
			[
				"nohup",
				"eclipse",
				"-configuration",
				configuration,
				"-data",
				workspace
			],
			stdout = open("/dev/null", "w"),
			stderr = open("/dev/null", "w")
		)
		
		self.exit(None)
	
	
	def create_new_profile(self, widget):
		self.profileNameInput.set_text("")
		if self.profileCreator.run() == 0: 
			profile = os.path.join(
				EclipseProfileSelector.PROFILE_DIRECTORY,
				self.profileNameInput.get_text()
			)
			
			os.mkdir(profile)
			self.add_content()
		
		self.profileCreator.destroy()


	def profile_name_changed(self, widget):
		profile = os.path.join(
			EclipseProfileSelector.PROFILE_DIRECTORY,
			widget.get_text()
		)
		
		self.addButton.set_sensitive(
			(not os.path.exists(profile)) and is_valid_path(profile)
		)
	
	
	def exit(self, widget):
		Gtk.main_quit()



def is_valid_path(path):
	try:
		f = open(path, "w")
		f.close()
		os.unlink(path)
		return True
	
	except OSError:
		return False

if __name__ == "__main__":
	EclipseProfileSelector()
	Gtk.main()
