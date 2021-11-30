import re
import os

os.chdir('../ss-winter/') #For testing purposes only

list_i = ['jeg','mig','min','mit']
list_you = ['j','eder','eders','vi','os','i','dig','du','din','dit']
filter_you = ['guds børn','gode guds','guds tienere','gvds børn','hellige guds']

foldername = 'sermons'
doc_list = []

for doc in os.listdir(foldername):
    if doc.endswith('.txt'):
        doc_list.append(foldername + '/' + doc)

for doc in doc_list[5:6]:  
    with open(doc,'r',encoding='utf-8') as file:
        freq_section = []
        freq = ()
        file = file.read().split()
        file_section = []
        for i in range(0, len(file), 150):
            file_section.append(file[i:i + 150])
        for section in file_section:
            counter_i = 0
            counter_you = 0
            for word in section:
                counter = 0
                if word in list_i:
                    counter_i+= 1             
                elif word in list_you:
                    if word == 'i':
                        if str(file[counter+1]+' '+file[counter+2]) in filter_you:
                            counter_you += 1
                    else:
                        counter_you += 1   
                counter += 1
            freq = (counter_you,counter_i)
            freq_section.append(freq)
            if counter_i > counter_you:
                print(freq,':',end=' ')
                for passage in file_section[file_section.index(section)-1:file_section.index(section)+2]:
                    for word in passage:
                        print(word,end=' ')
                print('\n')
        print(freq_section)
