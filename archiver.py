# This software is committed to the public domain (CCO)
# http://creativecommons.org/publicdomain/zero/1.0/

import os
import subprocess
from urllib.parse import urlencode
from urllib.parse import urlparse
import config

class archiver:
    def __init__(self):
        self.path = "./"
        self.res = None
        self.config = None
        self.wgetopts = ['-nH', '--no-check-certificate', '--timeout=5', '--tries=2']

    def setconfig(self, conf):
        self.arctype = conf.getopt('arctype')
        if conf.isopt('wapath'):
            self.path = conf.getopt('wapath')
        if conf.getopt('preserve'):
            self.wgetopts.append('-p')
        elif conf.getopt('mirror'):
            self.wgetopts.extend(
                ['--mirror', '--no-parent', '-nH', '--convert-links', '-p']
            )
        if conf.isopt('user_agent'):
            self.wgetopts.extend(['-U', conf.getopt('user_agent')])
        self.config = conf

    def fetch(self, url):
        pu = urlparse(url)
        hp = pu.netloc.partition(':')  # FQDN
        ht = hp[0].split('.')
        ht.reverse()
        hostdir = self.path + '/' + '/'.join(ht)
        archdir = hostdir

        # mirror creates path part
        if not self.config.isopt('mirror'):
            pp = pu.path.rpartition('/')
            # NAME_MAX is 255 for most linuxes (~140 using eCryptfs)
            archdir += (pp[0][:137] + '~') if len(pp[0]) > 140 else pp[0]

        if os.path.isdir(archdir):
            pass
        else:
            try:
                os.makedirs(archdir)
            except NotADirectoryError:
                # previous archive wrote a file
                # that we now know should be a directory
                # so, convert file to dir and copy file dir/index.wa
                while not os.path.isdir(archdir):
                    if len(hostdir) > len(archdir):
                        raise IOError("Cannot create directory " + archdir + " for: " + url)
                    if os.path.isfile(archdir):
                        tmp = self.path + "/.tmp"
                        os.rename(archdir, tmp)
                        os.makedirs(archdir)
                        os.rename(tmp, archdir + '/index.wa')
                        break
                    pp = archdir.rpartition('/')
                    archdir = pp[0]
                if not os.path.isdir(archdir):
                    raise IOError("Failed to create directory " + archdir + " for: " + url)

        wget_save = config.realdir() + '/wget-save'
        cmd = [wget_save, self.path, self.arctype]
        cmd.extend(self.wgetopts)
        cmd.extend(['-P', archdir])
        cmd.append(url)
        #print('cmd: ', cmd)
        stat = subprocess.call(cmd)
        return stat
