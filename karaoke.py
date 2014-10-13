#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler 
import sys
import os

class KaraokeLocal():
    
    def __init__(self, fich):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fichero))
        self.tags = sHandler.tags_list
    
    def __str__(self):
        full_fich = ""
        for tag in self.tags:
            t_name = tag.keys()[0]
            full_tag = t_name
            for attr in tag[t_name]:
                value = tag[t_name][attr]    
                if value != "":
                    full_tag += '\t' + attr + '=' + value   
            full_fich += full_tag + '\n'
        return full_fich
    
    def do_local(self):
        for tag in self.tags:
            t_name = tag.keys()[0]
            full_tag = t_name
            for attr in tag[t_name]: 
                value = tag[t_name][attr] 
                if attr == "src":                       
                    os.system ('wget -q ' + value)
                    tag[t_name][attr] = value.split('/')[-1]
 
try:
    fichero = sys.argv[1]
except IndexError:
    print 'Usage: python karaoke.py file.smil'
    raise SystemExit

K = KaraokeLocal(fichero)
print K
K.do_local()
print K
