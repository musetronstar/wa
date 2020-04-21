#!/bin/bash

function usage {
   	echo "usage: $0 [<wapath>]" >&2
}

wapath=~/var/wa  # default
if [ ! -z "$1" ]; then
	wapath="$1"
fi

history_file="${wapath}/.history"

# .history format
# arctype date url path
path=$(tail -n 1 "$history_file" | awk '{print $4}')
rm "$path"

# delete last line
sed -i '$ d' "$history_file"
