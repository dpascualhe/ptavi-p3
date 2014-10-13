#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler 
import sys
import os


try:
    fichero = sys.argv[1]
except IndexError:
    print 'Usage: python karaoke.py file.smil'
    raise SystemExit

parser = make_parser()
sHandler = SmallSMILHandler()
parser.setContentHandler(sHandler)
parser.parse(open(fichero))

tags = sHandler.tags_list

for tag in tags:
    t_name = tag.keys()[0]
    full_tag = t_name
    for attr in tag[t_name]:
        value = tag[t_name][attr] 
        if attr == "src":
            os.system ('wget -q ' + value)        
        if value != "":
            full_tag += '\t' + attr + '=' + value
            
    print full_tag
