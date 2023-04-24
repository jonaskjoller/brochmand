# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 18:20:37 2023

@author: jonas
"""

import re
import os

file_name = ['brochmand_sabbati_sanctificatio_vinter_@.txt','brochmand_sabbati_sanctificatio_sommer_@.txt']

def brochmand_sabbati_sanctificatio_vinter():
    file_name = 'brochmand_sabbati_sanctificatio_vinter_@.txt'
    dir_name = file_name[:len(file_name)-6]
    
    with open(file_name,'r',encoding='utf-8') as file:
        doc = file.read()
    
    #Make directories if not already existing
    try:
        os.mkdir(dir_name)
    except:
        pass
    try:
        os.mkdir(dir_name+'/prayer')
    except:
        pass
    
    doc_split = doc.split('@')
    
    descriptor = ['1SinAdv','2SinAdv','3SinAdv','4SinAdv','Christmas','StSteph','StJohn','1SafChr','NewYear',
                  '1SaftNY','Epiph','1SaftEpi', '2SaftEpi','3SaftEpi','4SaftEpi','5SaftEpi','6SaftEpi',
                  'MaryPur','Sept','Sexa','Lent','1SinLent','2SinLent','3SinLent','Laetare','SaftLat',
                  'MaryAnnun','PalmSun','MaunThur','GoodFri']
    
    counter, descriptor_counter = 0, 0
    exceptions = {48:'_EGP',80:'_G',82:'_G',83:'_G'}
    modifiers = ['_E','_G','_P']
    section = ['/','/','/prayer/']
    
    for i in range(len(doc_split)):
        if i == len(doc_split)-1:
            break
        if i in exceptions:
            file_name = dir_name+section[counter]+str(i).zfill(2)+'_'+descriptor[descriptor_counter]+exceptions[i]+'.txt'
            counter = 0
            descriptor_counter += 1
        else:
            file_name = dir_name+section[counter]+str(i).zfill(2)+'_'+descriptor[descriptor_counter]+modifiers[counter]+'.txt'
            if counter == 2:
                counter = 0
                descriptor_counter += 1
            else:
                counter += 1
        with open(file_name,'w',encoding='utf-8') as output:
            output.write(doc_split[i])

def brochmand_sabbati_sanctificatio_sommer():
    file_name = 'brochmand_sabbati_sanctificatio_sommer_@.txt'
    dir_name = file_name[:len(file_name)-6]
    
    with open(file_name,'r',encoding='utf-8') as file:
        doc = file.read()
    
    #Make directories if not already existing
    try:
        os.mkdir(dir_name)
    except:
        pass
    try:
        os.mkdir(dir_name+'/prayer')
    except:
        pass
    
    doc_split = doc.split('@')
    
    descriptor = ['Easter','2aftEas','3aftEas','1SafEas','2SafEas','3SafEas',
                  '4SafEas','5SafEas','Ascension','6SafEas','Pentecost','2aftPent',
                  '3aftPent','Trinity','1SaftTrin','2SaftTrin','3SaftTrin',
                  'StJohBap','4SaftTrin','MaryVisit','5SaftTrin','6SaftTrin',
                  '7SaftTrin','8SaftTrin','9SaftTrin','10SaftTrin','11SaftTrin',
                  '12SaftTrin','13SaftTrin','14SaftTrin','15SaftTrin','16SaftTrin',
                  'StMichael','17SaftTrin','18SaftTrin','19SaftTrin','20SaftTrin',
                  '21SaftTrin','AllSaints','22SaftTrin','23SaftTrin','24SaftTrin',
                  '25SaftTrin','26SaftTrin','27SaftTrin']
    
    counter, descriptor_counter = 0, 0
    modifiers = ['_E','_G','_P']
    section = ['/','/','/prayer/']
    
    for i in range(len(doc_split)):
        if i == len(doc_split)-1:
            break
        file_name = dir_name+section[counter]+str(i).zfill(2)+'_'+descriptor[descriptor_counter]+modifiers[counter]+'.txt'
        if counter == 2:
            counter = 0
            descriptor_counter += 1
        else:
            counter += 1
        with open(file_name,'w',encoding='utf-8') as output:
            output.write(doc_split[i])

functions = [['brochmand_sabbati_sanctificatio_vinter_@.txt',brochmand_sabbati_sanctificatio_vinter],
             ['brochmand_sabbati_sanctificatio_sommer_@.txt',brochmand_sabbati_sanctificatio_sommer]]

for file in file_name:
    for i in range(len(functions)):
        if file in functions[i]:
            functions[i][1]()
