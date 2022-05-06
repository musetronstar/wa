wa
==

Web file archiver written in Python

wa (web archiver) uses wget to download resources and store them in a
directory heirarchy according to the hostname and the path of the URL.

## Installation

To install, download the source to a directory (e.g. `~/src/`)
or your choice and run the install script, which will make soft links
to the executables in your path.

    cd ~/src
	./install.sh

or,

	./install.sh /path/to/bin  # override default

### Uninstall

    cd ~/src
	./uninstall.sh

or,

	./uninstall.sh /path/to/bin  # override default

## WAPATH

The web archive directory is given by the environment variable `$WAPATH`.
If not defined, it defaults to `~/var/wa`.

## `.warc`

If it exists, Python will read the file `~/wa.rc`
where the following options can be defined

    # sets a User Agent string
    user_agent = User Agent String
    
The `-m` command line switch will mirror a request *recursivily*
from the authority/path, so use carefully.

The directory heirarchy in the form:

    <wapath>/<tld>/<private>/<subdomain>/<path>/<file>

## Web archive example
Fetches and stores files in wapath (default ~/var/wa):

    wa -t archive,test http://www.example.com

    tree ~/var/wa
    /home/musetronstar/var/wa
    └── com
        └── example
            └── www
                └── index.html
                
A history file is written in the form:

	<DATE>	<TYPE>	<URL>	<PATH>	<TAGS>

    $ tail -n 1 ~/var/wa/.history 
	2021-06-18-11:54:00	S	http://example.com	com/example/index.html	archive,test

### Archive Types
* 'S' single file download
* 'M' mirror

This software is in the public domain.
