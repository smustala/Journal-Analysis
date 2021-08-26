#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:16:17 2021

@author: shalinimustala
"""

import xml.etree.ElementTree as ET
import pdb
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

#ignore = ["ext-link", "xref"]

def print_text_ignore(el, file):
    if el.tag in ignore:
        return
    if type(el.text) is str:
        with open (file, 'a') as f:
            f.write(el.text + "\n")
    for child in el:
        print_text_ignore(child, file)

def handle_abstract(el):
    for elc in el.iterfind(".*"):
       print(elc.text)
    pdb.set_trace()

def print_text_keep(el, file):
    #if el.tag == "abstract":
     #  handle_abstract(el)
    
    if (el.tag in keep) and (type(el.text) is str):
        with open (file, 'a') as f:
            f.write(el.text + "\n")

    for child in el:
        print_text_keep(child, file)
        if type(child.tail) is str and (el.tag in keep):
            with open(file, 'a') as f:
                f.write(child.tail + "\n")

file = '/Users/shalinimustala/Documents/Journal_analysis/allpapersTXT/10.1177_0001839214523602_3.txt' #'converted_new.txt'
with open(file, 'w') as f:
    f.write("")

tree = ET.parse('/Users/shalinimustala/Documents/Journal_analysis/all_papers/10.1177_0001839214523602.xml')    #ET parser helps in iterating the tree
root = tree.getroot()
for child in root:
   if child.tag != 'back':
        print_text_keep(child, file)
        

            
            
            
            
            
            
            
            
            
            
            
            
            
            
