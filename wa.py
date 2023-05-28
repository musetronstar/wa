#!/usr/bin/python3
"""
    Downloads Web resources to an archive directory and maintains a history log.

    usage:
        wa [-p] [-m] [-d] [-t CSV,tag,list] <URL1> [URL2...]

    options:
        -p    preserve (download dependencies)
        -m    mirror authority/path
        -d    override wapath
        -t    comma seperated list of tags without whitespace
"""

# This software is committed to the public domain (CCO)
# http://creativecommons.org/publicdomain/zero/1.0/

from config import config
from archiver import archiver
from getopt import getopt
from time import strftime
import sys


def die_usage():
    print(__doc__)
    sys.exit(0)

opts, args = getopt(sys.argv[1:], 'hpmt:d:')
conf = config()

# archive type S = single file, P = preserve (all reqs), M = mirror
arctype = 'S'

tags=None
for opt in opts:
    if opt[0] == '-h':
        die_usage()
    if opt[0] == '-p':
        conf.setopt('preserve', True)
        arctype = 'P'
    elif opt[0] == '-m':
        conf.setopt('mirror', True)
        arctype = 'M'
    elif opt[0] == '-d':  # override default wapath
        conf.setopt('wapath', opt[1])
    elif opt[0] == '-t':  # list of CSV tags, no whitespace
        tags = opt[1]

conf.setopt('arctype', arctype)
wa = archiver(conf, tags)
urls = args[:]

if len(urls) == 0:
    die_usage()

count = 0
for url in urls:
    stat = wa.fetch(url)

    if stat > 0:
        print("wa %s failed" % url, file=sys.stderr)
    else:
        count += 1

print("%i urls archived" % count)
