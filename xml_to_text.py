#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:16:17 2021

@author: shalinimustala
"""

import xml.etree.ElementTree as ET

keep = [
        "title-group",
        "article-title",
        "subtitle",
        "abstract",
        "kwd",
        "body",
        "p",
        "sec",
        "title",
        "bold",
        "italic"
        ]



def print_text_keep(el, file):
  
    if (el.tag in keep) and (type(el.text) is str):
        with open (file, 'a') as f:
            f.write(el.text + "\n")

    for child in el:
        print_text_keep(child, file)
        if type(child.tail) is str and (el.tag in keep):
            with open(file, 'a') as f:
                f.write(child.tail + "\n")
                
#file = 'converted_new.txt'
#with open(file, 'w') as f:
#    f.write("")

#tree = ET.parse('paper.xml')    #ET parser helps in iterating the tree
#root = tree.getroot()
#for child in root:
#    if child.tag != 'back':
#        print_text_keep(child, file)
        
def allpapers(in_dir, out_dir):
    import os
    #directory = os.getcwd() + '/all_papers/'
    for entry in os.scandir(in_dir):
        if entry.path.endswith(".xml") and entry.is_file():
            path_paper = entry.path
            file = out_dir + "/" + path_paper.split("/")[-1].replace("xml", "txt")
            with open(file, 'w') as f:
                f.write("")
            tree = ET.parse(path_paper)
            root = tree.getroot()
            for child in root:
                if child.tag != 'back':
                    print_text_keep(child, file)
            
            
            
            
            
            
            
            
            
            
            
            
            
            