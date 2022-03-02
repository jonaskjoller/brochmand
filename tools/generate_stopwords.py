import re
import os
import textwrap
import collections

wordlist = []
word_freqs = collections.defaultdict(int) #Dictionary of word frequencies in corpus
wordfreq_doc = collections.defaultdict(int) #Dictionary of document frquency of word forms
file_list = []
dir_list = []
doc_list = []


#path = os.chdir('../ss-winter/') #For testing purposes
path = os.getcwd()

#Clean file
#The file cleaning is specific to 17th century Danish documents. Adjust as needed
def clean_doc(file):
    file = file.read()
    file = file.lower() #Lower case
    file = re.sub('[/.:?;,]','',file) #Remove select special characters
    file = re.sub('=\n','',file) #Contract hyphenated words
    file = re.sub('\n',' ',file) #Substitute new line with space
    file = re.sub(' +',' ',file) #Reduce surplus spacing
    return file

for line in textwrap.wrap('This program will automatically generate a list of '
      'stopwords from a corpus. In order to run properly it assumes the '
      'existence of a subfolder containing a .txt-file for each individual ' 
      'document in your corpus, and that you run the program one level above '
      'the subfolder.', width=80):
    print(line)

print('\nIt builds the stopword list from two principles:\n')

print('1. Word forms occurring in more than x % of individual documents.')

print('2. Word forms occurring less than y times in entire corpus.\n')

print('Please enter values for x and y')
x = int(input('x = '))
y = int(input('y = '))
print()

#List subfolders
counter = 0
for items in os.scandir():
    if items.is_dir():
        dir_list.append(items)
        print (counter, items.name)
        counter += 1

foldername = dir_list[int(input('\nSelect subfolder by entering folder-number: '))]

#Get name of folder to use as naming scheme
keyword = path.split('\\')[-1]

#Generate list of filepaths to individual documents
for items in os.listdir(foldername):
    if items.endswith('.txt'):
        doc_list.append(foldername.name + '/' + items)

#Build word frequency of individual documents
for i in range(0,len(doc_list)):
    with open(doc_list[i],'r',encoding='utf-8') as file:
        file = clean_doc(file).split()
        #Build corpus dictionary
        for w in file:
            word_freqs[w] += 1
        #Build dictionary from set
        for w in set(file):
            wordfreq_doc[w] += 1
    #Keep track of files processed
    print('Completed',i+1, 'out of',len(doc_list),flush=True)
                 
#Save a new file
with open('stopword_' + keyword + '_' + str(x) + '_' + str(y) + '.txt','w',encoding='utf-8') as file:
    for k,v in sorted(wordfreq_doc.items(),key=lambda item: item[1]):
        if v >= len(doc_list)*(x/100):
            file.write(k+'\n')
    for k,v in sorted(word_freqs.items(),key=lambda item: item[1]):
        if v <= y:
            file.write(k+'\n')
