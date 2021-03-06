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

for doc in doc_list[14:15]:  
    with open(doc,'r',encoding='utf-8') as file:
        freq_section = []
        freq = ()
        file = file.read().split()
        file_section = []
        #Split file into smaller sections
        for i in range(0, len(file), 150):
            file_section.append(file[i:i + 150])
        #Count frequence of 1st and 2nd person pronouns in section
        for section in file_section:
            counter_i = 0
            counter_you = 0
            for w in range(0,len(section)):
                if section[w] in list_i:
                    counter_i+= 1             
                elif section[w] in list_you:
                    if section[w] == 'i':
                        if str(file[w+1]+' '+file[w+2]) in filter_you:
                            counter_you += 1
                    else:
                        counter_you += 1   
            # freq = (counter_you,counter_i)
            # freq_section.append(freq)
            freq_section.append(counter_you-counter_i)
        for x in range(0,len(file_section)):
            if freq_section[x] < 0:
                if freq_section[x-1] >= 0:
                    print(freq_section[x],':',end=' ')
                for word in file_section[x]:
                    print(word,end=' ')
                try:
                    if freq_section[x+1] >= 0:
                        print('\n')
                except:
                    print('\n')
        print(freq_section)
