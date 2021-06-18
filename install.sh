#!/bin/bash

# usage:
#   install.sh               # installs to default $HOME/bin
#   install.sh /path/to/bin  # installs to given directory

if [ -z "$1" ]; then
	BIN=$HOME/bin
else
	BIN="$1"
fi

SRC=$(dirname $(realpath $0))

ln -s ${SRC}/wa.py ${BIN}/wa
ln -s ${SRC}/wa-file ${BIN}/wa-file
ln -s ${SRC}/wa-rm-last ${BIN}/wa-rm-last
ln -s ${SRC}/wa-vid ${BIN}/wa-vid
