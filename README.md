# addok-openaddresses

Helpers to import [OpenAddresses](https://openaddresses.io) data into Addok.


## Install

Install addok, addok-trigrams and addok-openaddresses (this repository):

    pip install git+https://github.com/addok/addok
    pip install git+https://github.com/addok/addok-trigrams
    pip install git+https://github.com/addok/addok-openaddresses


Copy the sample local config:

    cp sample.local.py somewhere/local.py

It should work as is, but you can have a look at the
[addok configuration](http://addok.readthedocs.io/en/latest/config/)
to adapt it to your needs.

This plugin adds one configuration key that needs more consideration:


- OPENADDRESSES_EXTRA, which is a dict to be added to each row (they often miss City, or District, etc.)


## Importing

Get the files from https://results.openaddresses.io/
Then:

    addok batch path/to/file.csv
