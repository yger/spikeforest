#!/usr/bin/env python

from mountaintools import client as mt

sha1_path = mt.saveFile('spyking_circus.simg')
print(sha1_path)
sha1_path = mt.saveFile('spyking_circus.simg', upload_to='spikeforest.public')
print(sha1_path)
