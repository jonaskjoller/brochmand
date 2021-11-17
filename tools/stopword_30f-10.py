import re
import os

wordlist = []
wordfreq = {}
file_list = []
counter = 0
counter_file = 0
wordfreq_files = {}
file_list_files = []

os.chdir('../ss-winter/')

# List possible files in folder
for items in os.listdir():
    if items.endswith('.txt'):
        file_list.append(items)
        print (counter, items)
        counter += 1
    
filename = file_list[int(input('Select file by entering file number: '))]

#Get name of folder to use as naming scheme
keyword = os.getcwd().split('\\')[-1]

#Clean file
with open(filename,'r',encoding='utf-8') as file:
    file = file.read()
    file = file.lower() #Lower case
    file = re.sub('[/.:?;]','',file) #Remove special characters
    file = re.sub('=\n','',file) #Contract hyphenated words
    file = re.sub('\n',' ',file) #Substitute new line with space
    file = re.sub(' +', ' ', file) #Reduce surplus spacing
    wordlist = file.split()

#Build word frequency
for w in wordlist:
    wordfreq[w] =  wordfreq.get(w,0) + 1

#Generate list of indidividual files
os.chdir('sermons/')
for items in os.listdir():
    if items.endswith('.txt'):
        file_list_files.append(items)

#Computes occurences in individual files
for items in file_list_files:
    with open(items,'r',encoding='utf-8') as file:
        file_dic = {} #Generate dictionary of unique words in file
        for w in file.read().split():
            file_dic[w] = file_dic.get(w,0) +1
        for k in wordfreq: #Compares to word frequency list
            for i in file_dic:
                if k == i:
                    wordfreq_files[k] = wordfreq_files.get(k,0) + 1
    #Keeps track of files processed
    counter_file += 1
    print('Completed',counter_file, 'out of',len(file_list_files))
                 
#Save a new file
with open('stopword_' + keyword + '_30f-10.txt','w',encoding='utf-8') as file:
    for k,v in sorted(wordfreq_files.items(),key=lambda item: item[1]):
        if v >= len(file_list_files)*0.3:
            file.write(k+'\n')
    for k,v in sorted(wordfreq.items(),key=lambda item: item[1]):
        if v <= 10:
            file.write(k+'\n')
