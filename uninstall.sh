#!/bin/bash

# usage:
#   uninstall.sh               # installs to default $HOME/bin
#   uninstall.sh /path/to/bin  # installs to given directory

if [ -z "$1" ]; then
	BIN=$HOME/bin
	[ -d "$BIN" ] || mkdir -v "$BIN"
else
	BIN="$1"
fi

SRC=$(dirname $(realpath $0))

[ -e $BIN/wa ] && rm -v $BIN/wa
for p in $SRC/bin/*; do
	f="${p##*/}"  # filename without leading path
	[ -e $BIN/$f ] && rm -v $BIN/$f
done

