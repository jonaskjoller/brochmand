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
    if w not in wordfreq:
        wordfreq[w] = 1
    else:
        wordfreq[w] += 1

#Get position of top 1 percent and bottom 10 percent
pos_top20 = int(len(wordfreq)*0.01)
pos_low10 = int(len(wordfreq)*0.1)

#Save a new file
with open('stopword_' + keyword + '_1p-10p.txt','w',encoding='utf-8') as file:
    for k,v in sorted(wordfreq.items(),key=lambda item: item[1], reverse=True)[:pos_top20]:
        file.write(k+'\n')
    for k,v in sorted(wordfreq.items(),key=lambda item: item[1], reverse=False)[:pos_low10]:
        file.write(k+'\n')
