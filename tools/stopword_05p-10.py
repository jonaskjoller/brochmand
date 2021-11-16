import re
import os

wordlist = []
wordfreq = {}
file_list = []
counter = 0

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
    file = re.sub('[/.:?]','',file) #Remove special characters
    file = re.sub('=\n','',file) #Contract hyphenated words
    file = re.sub('\n',' ',file) #Substitute new line with space
    file = re.sub(' +', ' ', file) #Reduce surplus spacing
    wordlist = file.split()

#Build word frequency
for w in wordlist:
    wordfreq[w] =  wordfreq.get(w,0) + 1

#Get position of top 0.5 percent
pos_top05 = int(len(wordfreq)*0.005)

#Save a new file
with open('stopword_' + keyword + '_05p-10.txt','w',encoding='utf-8') as file:
    for k,v in sorted(wordfreq.items(),key=lambda item: item[1], reverse=True)[:pos_top05]:
        file.write(k+'\n')
    #
    for k,v in sorted(wordfreq.items(),key=lambda item: item[1], reverse=True)[pos_top05:]:
        if v <= 10:
            file.write(k+'\n')
