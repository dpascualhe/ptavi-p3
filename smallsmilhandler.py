#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        self.tags_list = []

    def get_tags(self, name, attrs):
        add = 1
        if name == 'root-layout':
            root_layout = {}
            root_layout['width'] = attrs.get('width',"")            
            root_layout['height'] = attrs.get('height',"")
            root_layout['background-color'] = attrs.get('background-color',"")
            actual = {'root-layout': root_layout}

        elif name == 'region':
            region = {}
            region['id'] = attrs.get('id', "")
            region['top'] = attrs.get('top', "")
            region['bottom'] = attrs.get('bottom', "")
            region['left'] = attrs.get('left', "")
            region['right'] = attrs.get('right', "")
            actual = {'region': region}
                   
        elif name == 'img':
            img = {}
            img['src'] = attrs.get('src', "")
            img['region'] = attrs.get('region', "")
            img['begin'] = attrs.get('begin', "")
            img['dur'] = attrs.get('dur', "")
            actual = {'img': img} 
        
        elif name == 'audio':
            audio = {}
            audio['src'] = attrs.get('src', "")
            audio['begin'] = attrs.get('begin', "")
            audio['dur'] = attrs.get('dur', "")             
            actual = {'audio': audio}
        elif name == 'textstream':     
            textstream = {} 
            textstream['src'] = attrs.get('src', "")
            textstream['region'] = attrs.get('region', "")
            actual = {'textstream': textstream} 
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
