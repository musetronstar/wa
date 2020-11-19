# This software is committed to the public domain (CCO)
# http://creativecommons.org/publicdomain/zero/1.0/

import os

# script directory
def realdir():
    return os.path.dirname(os.path.realpath(__file__))

class config:
    def __init__(self):
        home = os.environ['HOME']
        config_file = home + "/.warc"

        # default configs
        self.CONFIG = {'preserve': False}

        if 'WAPATH' in os.environ:
            self.CONFIG['wapath'] = os.environ['WAPATH']
        else:
            self.CONFIG['wapath'] = home + '/var/wa'

        if os.path.isfile(config_file):
            with open(config_file) as file_in:
                for line in file_in:
                    line = line.strip()
                    key, val = line.split('=')
                    self.CONFIG[key.rstrip()] = val.rstrip()

    def getopt(self, key):
        if not key in self.CONFIG:
            return False
        return self.CONFIG[key]

    def setopt(self, key, val):
        self.CONFIG[key] = val

    def isopt(self, key):
        if key in self.CONFIG:
            return True
        else:
            return False
