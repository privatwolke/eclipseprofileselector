eclipse-profile-selector
========================

This little application manages Eclipse profiles for you. It understands
a _profile_ to be a configuration and a workspace folder and is compatible
with the Mars release of Eclipse.

Profiles are stored by default in `~/.eclipse-profiles`.


Installation
------------

Either install directly using `python setup.py install` or create an egg with
`python setup.py bdist_egg`.


Dependencies
------------

  * `sudo apt-get install python3-gi` (on Ubuntu/Debian)
  * python 2.7 (may work on lower versions)
  * eclipse should be installed and in your `$PATH`
