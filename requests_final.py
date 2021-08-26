#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:50:21 2021

@author: shalinimustala
"""
import os
# Look to the path of your current working directory
working_directory = os.getcwd()
import requests
session = requests.session()
url = 'https://journals.sagepub.com/action/doLogin?login=cbeckman%40price.usc.edu&password=3ditorAccess!'
response = session.get(url)

with open('xml_urls.txt', 'r') as f:   # Journal Articles from 2011 to to date # Every year has 1 volume and 4 Issues (1,2,3,4) . 2011 is  Volume 56. 2020 is Volume 65 
    for line in f:
        url_paper = line.strip()
        d = url_paper.split('/')[-2:]
        doi = d[0] + '_' + d[1]
        res = session.get(url_paper)
        file_path = working_directory + '/all_papers/' + doi + '.xml'
        with open(file_path, 'wb') as f:
            f.write(res.content)
        print('downloaded')

#Online First Artcles
with open('xml_urls_OF.txt', 'r') as f:
    for line in f:
        url_paper = line.strip()
        d = url_paper.split('/')[-2:]
        doi = d[0] + '_' + d[1]
        res = session.get(url_paper)
        file_path = working_directory + '/OnlineFirst_papers/' + doi + '.xml'
        with open(file_path, 'wb') as f:
            f.write(res.content)
        print('downloaded')
        
        