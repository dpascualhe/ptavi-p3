#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        self.root_layout = {}
        self.region = {}
        self.img = {}
        self.audio = {}
        self.textstream = {}
        self.tags_list = []

    def get_tags(self, name, attrs):
        add = 1
        if name == 'root-layout':
            self.root_layout['width'] = attrs.get('width',"")            
            self.root_layout['height'] = attrs.get('height',"")
            self.root_layout['background-color'] = attrs.get('background-color',"")
            actual = {'root-layout': self.root_layout}

        elif name == 'region':
            self.region['id'] = attrs.get('id', "")
            self.region['top'] = attrs.get('top', "")
            self.region['bottom'] = attrs.get('bottom', "")
            self.region['left'] = attrs.get('left', "")
            self.region['right'] = attrs.get('right', "")
            actual = {'region': self.region} 
       
        elif name == 'img':
            self.img['src'] = attrs.get('src', "")
            self.img['region'] = attrs.get('region', "")
            self.img['begin'] = attrs.get('begin', "")
            self.img['dur'] = attrs.get('dur', "")
            actual = {'img': self.img} 
        
        elif name == 'audio':
            self.audio['src'] = attrs.get('src', "")
            self.audio['begin'] = attrs.get('begin', "")
            self.audio['dur'] = attrs.get('dur', "")             
            actual = {'audio': self.audio}
        elif name == 'textstream':      
            self.textstream['src'] = attrs.get('src', "")
            self.textstream['region'] = attrs.get('region', "")
            actual = {'textstream': self.textstream} 
        else:
            add = 0

        if add:
            self.tags_list.append(actual)

    
    def startElement(self, name, attrs):
        self.get_tags(name, attrs)    


if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))

    print sHandler.tags_list
