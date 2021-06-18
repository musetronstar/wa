wa
==

Web file archiver written in Python

wa (web archiver) uses wget to download resources and store them in a
directory heirarchy according to the hostname and the path of the URL.

To install, download the source to a directory (e.g. `~/src/`)
or your choice and run the install script, which will make soft links
to the executables in your path.

    cd ~/src
	./install.sh

or,

	./install /path/to/bin  # override default

The web archive directory, `wapath`, is by default `~/var/wa`.  This can be
changed by creating a file `~/.warc` and defining another path:

    wapath = /some/other/dir

The `-m` command line switch will mirror a request *recursivily*
from the authority/path, so use carefully.

The directory heirarchy in the form:

    <wapath>/<tld>/<private>/<subdomain>/<path>/<file>

## Web archive example
Fetches and stores files in wapath (default ~/var/wa):

    $ tree ~/var/wa
    /home/musetronstar/var/wa
    └── com
        └── example
            └── www
                └── index.html
                
    $ wa -t archive,test http://www.example.com
    ...

A history file is written in the form:
	<DATE>	<TYPE>	<URL>	<PATH>	<TAGS>

    $ tail -n 1 ~/var/wa/.history 
	2021-06-18-11:54:00	S	http://example.com	com/example/index.html	archive,test

### Archive Types
* 'S' single file download
* 'M' mirror

This software is in the public domain.
