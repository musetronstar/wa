# This software is committed to the public domain (CCO)
# http://creativecommons.org/publicdomain/zero/1.0/

import os

class config: 
	def __init__(self):
		home = os.environ['HOME']
		config_file = home + "/.warc"

		# default configs
		self.CONFIG = {
			'wapath' :	home + '/var/wa',
			'preserve' :	False
		} 

		if os.path.isfile(config_file):
			for line in open(config_file):
				line = line.strip()
				key, val = line.split('=')
				key  = key.rstrip()
				val = val.lstrip()
				self.CONFIG[key] = val	

	def getopt(self, key):
		if not self.CONFIG.has_key(key):
			return False
		return self.CONFIG[key]

	def setopt(self, key, val):
		self.CONFIG[key] = val

	def isopt(self, key):
		if self.CONFIG.has_key(key):
			return True
		else:
			return False
