from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name = 'eclipse-profile-selector',
	version = version,
	description = 'Manage separate Eclipse profiles and workspaces with a nice graphical user interface.',
	keywords = 'eclipse profile',
	author = 'Stephan Klein',
	url = 'https://github.com/privatwolke/eclipse-profile-selector',
	license = 'MIT',
	packages = ['eclipseprofileselector'],
	package_dir = {
		'eclipseprofileselector': 'src'
	},
	package_data = {
		'eclipseprofileselector': ['*.glade']
	},
	include_package_data = True,
	zip_safe = False,
	entry_points = {
		'gui_scripts': [
			'eclipse-profile-selector=eclipseprofileselector.profile:main'
		]
	}
)
