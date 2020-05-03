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

# .history format (tsv)
# date	arctype	url	rel_path
path="${wapath}/$(tail -n 1 "$history_file" | awk -F "\t" '{print $4}')"
rm -v "$path"

# delete last line
sed -i '$ d' "$history_file"
