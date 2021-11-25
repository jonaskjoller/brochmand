import re
import os

list_i = ['jeg','mig','min','mit']
list_you = ['j','eder','eders','vi','os']

foldername = 'sermons'
doc_list = []

for doc in os.listdir(foldername):
    if doc.endswith('.txt'):
        doc_list.append(foldername + '/' + doc)

for doc in doc_list:  
    with open(doc,'r',encoding='utf-8') as file:
        freq_section = []
        freq = ()
        counter_i = 0
        counter_you = 0
        file = file.read().split()
        file_section = []
        for i in range(0, len(file), int(len(file)/10)):
            file_section.append(file[i:i + int(len(file)/10)])
        for section in file_section:
            for word in section:
                if word in list_i:
                    counter_i += 1
                elif word in list_you:
                    counter_you += 1
            freq = (counter_you,counter_i)
            freq_section.append(freq)
        print(freq_section)
            # if counter_you-counter_i > 0:
            #    print(doc[8:],counter_you,counter_i,counter_you-counter_i)
