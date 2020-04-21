#!/usr/bin/python3

# This software is committed to the public domain (CCO)
# http://creativecommons.org/publicdomain/zero/1.0/

from config import config
from archiver import archiver
from getopt import getopt
from time import strftime
import sys


def usage():
    print("wa.py [-p] http://example.com")
    sys.exit(0)

opts, args = getopt(sys.argv[1:], 'pm')
conf = config()

# archive type S = single file, P = preserve (all reqs), M = mirror
arctype = 'S'

for opt in opts[:]:
    if opt[0] == '-p':
        conf.setopt('preserve', True)
        arctype = 'P'
    elif opt[0] == '-m':
        conf.setopt('mirror', True)
        arctype = 'M'
conf.setopt('arctype', arctype)

wa = archiver()
wa.setconfig(conf)

count = 0
for url in args[:]:
    stat = wa.fetch(url)

    if stat > 0:
        print("wa %s failed" % url, file=sys.stderr)
    else:
        count = count + 1

print("%d urls archived" % count)
