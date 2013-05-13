wa
==

http or ftp web file archiver written in python

wa (web archiver) is a simple python program that uses wget to download http
or ftp resources and store them in a directory heirarchy according to the
hostname and the path of the URL.

To install, download the source to a directory or your choice (for example,
~/src).  Then make a soft link to the executable to a something in your path,
for example:

    ln -s ~/src/wa/wa.py ~/bin/wa

The web archive directory, <wapath>, is by default ~/var/wa.  This can be
changed by creating a file ~/.warc and defining another path:

    wapath = /some/other/dir

A command line switch -m can be added to mirror a request.  Be careful,
all dependencies will be downloaded recursively.

The directory heirarchy in the form:

    <wapath>/<tld>/<private>/<subdomain>/<path>/<file>

For example (using default wapath):

    $ wa http://www.hypermega.com
    ...

    $ tree ~/var/wa
    /home/icolley/var/wa
    └── com
        └── hypermega
            └── www
                └── index.html
                
A history file is also written:

    $ cat ~/var/wa/.history 
    S 2013-05-13-07:32:07 http://www.hypermega.com

The 'S' indicates a single file download.
An 'M' would indicated a mirrored download.

Enjoy...
