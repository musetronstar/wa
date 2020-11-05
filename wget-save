#!/bin/bash

function usage {

	PRG=$(basename $0)
echo "usage:
	$PRG <wapath> <arctype> [wget-opts ...] <url>

where <arctype> is one of:
	S	single file
	P	download page requisites (wget -p option)
	M	mirror" >&2

}

if [ "$#" -lt 3 ]; then
	usage
	exit 1
fi

wapath=$1  # must be first arg
if [ ! -d "$wapath" ]; then
   	echo "no such wapath directory: $wapath" >&2
	usage
	exit 1
fi

shift # wapath not passed to wget

declare -A ARCTYPES
ARCTYPES[S]="S"	# TODO use corresponding wget opts as values
ARCTYPES[P]="P"
ARCTYPES[M]="M"

arctype=$1  # must be second arg (see shift above)
if [ "${ARCTYPES[$arctype]+exists}" != "exists"  ]; then
   	echo "invalid arctype: $arctype" >&2
	usage
	exit 1
fi

shift # arctype not passed to wget

url=${!#}  # must be last arg
if [ -z $url ]; then
   	echo "url required" >&2
	usage
	exit 1
fi

TMP=/tmp/wget-saved.$BASHPID

wget "$@" 2>&1 | tee $TMP

# 'saved' line looks like:
# 2020-04-05 08:34:06 (47.6 MB/s) - ‘/path/to/file’ saved [318/318]
# where the saved file is enclosed in unicode:
#	‘	LEFT SINGLE QUOTATION MARK	\u2018
#	’	RIGHT SINGLE QUOTATION MARK	\u2019
saved=$(grep 'saved' $TMP | sed -n 's/^.*‘\(.*\)’.*$/\1/p')
pos=
if [ "${pos: -1}" == '/' ]; then
   	pos=${#wapath}
else
	pos=$(expr ${#wapath} + 1)
fi

 # relative path of saved file inside wapath
rsaved=${saved:$pos}

# history file format:
# 2020-04-05-11:09:11	S	http://example.com/file.html	/wapath/com/example/file.html
if [ ! -z "$saved" ]; then
	history_file="${wapath}/.history"
	echo "$(date +%F-%T)	$arctype	$url	$rsaved" >> $history_file
fi

rm $TMP
