# This software is committed to the public domain (CCO)
# http://creativecommons.org/publicdomain/zero/1.0/

import os
import urllib2
from urllib import urlencode
from urlparse import urlparse

class archiver:

	def __init__(self):
		self.path = "./"
		self.res = None
		self.config = None
		self.wgetopts = ['-nH --no-check-certificate']

	def setconfig(self, conf):
		if conf.isopt('wapath'):
			self.path = conf.getopt('wapath')
		if conf.getopt('preserve'):
			self.wgetopts.append('-p')
		elif conf.getopt('mirror'):
			self.wgetopts.append('--mirror --no-parent -nH -erobots=off --timeout=5 --tries=2 --convert-links -p')
		if conf.isopt('user_agent'):
			self.wgetopts.append('-U "' + conf.getopt('user_agent') + '"')
		self.config = conf

	def fetch(self, url): 
		pu = urlparse(url)
		hp = pu.netloc.partition(':')	# FQDN
		ht = hp[0].split('.')
		ht.reverse()
		hostdir = self.path + '/' + '/'.join(ht)

		# mirror creates path part
		if not self.config.isopt('mirror'):	
			pp = pu.path.rpartition('/')
			if len(pp[0]):
				hostdir += pp[0]

		if not ( os.path.isdir(hostdir) or os.path.isfile(hostdir) ):
			os.makedirs(hostdir)

		self.wgetopts.append('-P ' + hostdir)
		cmd = 'wget ' + ' '.join(self.wgetopts) + ' "' + url + '"'
		#print cmd
		stat = os.system(cmd)
		return stat
