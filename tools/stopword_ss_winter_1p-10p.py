import re

wordlist = []
wordfreq = {}

#filename = input('Enter filename: ')
filename = 'Sabbati_Sanctificatio_Vinter_(Brochmand).txt'

with open(filename,'r',encoding='utf-8') as file:
    file = file.read()
    file = file.lower() #Lower case
    file = re.sub('[/.:?]','',file) #Remove special characters
    file = re.sub('=\n','',file) #Contract hyphenated words
    file = re.sub('\n',' ',file) #Substitute new line with space
    file = re.sub(' +', ' ', file) #Reduce surplus spacing
    wordlist = file.split()
   
for w in wordlist:
    if w not in wordfreq:
        wordfreq[w] = 1
    else:
        wordfreq[w] += 1

pos_top20 = int(len(wordfreq)*0.01)
pos_low10 = int(len(wordfreq)*0.1)


with open('stopword_ss_winter_1p-10p.txt','w',encoding='utf-8') as file:
    for k,v in sorted(wordfreq.items(),key=lambda item: item[1], reverse=True)[:pos_top20]:
        file.write(k+'\n')
    for k,v in sorted(wordfreq.items(),key=lambda item: item[1], reverse=False)[:pos_low10]:
        file.write(k+'\n')
