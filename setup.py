from setuptools import setup, find_packages
import sys, os

version = '0.2.1'

setup(name = 'eclipseprofileselector',
	version = version,
	description = 'Manage separate Eclipse profiles and workspaces with a nice graphical user interface.',
	long_description = open('README.md', 'r').read(),
	keywords = 'eclipse profile',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Environment :: X11 Applications :: GTK',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Operating System :: POSIX',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Topic :: Utilities'
	],
	author = 'Stephan Klein',
	url = 'https://github.com/privatwolke/eclipse-profile-selector',
	license = 'MIT',
	packages = ['eclipseprofileselector'],
	package_data = {
		'eclipseprofileselector': ['ui.glade']
	},
	include_package_data = True,
	zip_safe = True,
	entry_points = {
		'gui_scripts': [
			'eclipse-profile-selector = eclipseprofileselector.profile:main'
		]
	}
)
