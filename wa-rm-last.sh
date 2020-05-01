#!/bin/bash

function usage {
   	echo "usage: $0 [<wapath>]" >&2
}

wapath=~/var/wa  # default
[ -n "$WAPATH" ] && wapath="$WAPATH"

if [ ! -z "$1" ]; then
	wapath="$1"
fi

history_file="${wapath}/.history"

# .history format
# arctype date url path
# awk everthing after col 3, sed strip leading space
path=$(tail -n 1 "$history_file" | awk '{$1=$2=$3=""; print $0}' | sed -e 's/^[[:space:]]*//')
rm "$path"

# delete last line
sed -i '$ d' "$history_file"
