import re
import os
import textwrap

wordlist = []
wordfreq_corpus = {}
wordfreq_doc = {}
file_list = []
dir_list = []
doc_list = []

#os.chdir('../ss-winter/') #For testing purposes only

for line in textwrap.wrap('This program will automatically generate a list of '
      'stopwords from a corpus. In order to run properly it assumes the '
      'existence of a single .txt-file containing your entire corpus, a '
      'subfolder containing a .txt-file for each individual document in your '
      'corpus, and that you run the program in the same folder which contains '
      'the single-file corpus.', width=80):
    print(line)

print('\nIt builds the stopword list from two principles:\n')

print('1. Word forms occurring in more than x% of individual documents.')

print('2. Word forms occurring less than y times in entire corpus.\n')

print('Please enter values for x and y')
x = int(input('x = '))
y = int(input('y = '))
print()

# List possible files in folder
counter = 0
for items in os.listdir():
    if items.endswith('.txt'):
        file_list.append(items)
        print (counter, items)
        counter += 1

filename = file_list[int(input('\nSelect corpus-file by entering file-number: '))]
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

#Build word frequency of corpus
for w in wordlist:
    wordfreq_corpus[w] =  wordfreq_corpus.get(w,0) + 1

#Generate list of filepaths to individual documents
for items in os.listdir(foldername):
    if items.endswith('.txt'):
        doc_list.append(foldername.name + '/' + items)

#Build word frequency of individual documents
counter = 0
for items in doc_list:
    with open(items,'r',encoding='utf-8') as file:
        #Generate dictionary of unique word forms in file
        file_dic = {}
        for w in file.read().split():
            file_dic[w] = file_dic.get(w,0) +1
        #Compare word forms in file and corpus
        for k in wordfreq_corpus:
            for i in file_dic:
                if k == i:
                    wordfreq_doc[k] = wordfreq_doc.get(k,0) + 1
    #Keep track of files processed
    counter += 1
    print('Completed',counter, 'out of',len(doc_list),flush=True)
                 
#Save a new file
with open('stopword_' + keyword + '_' + str(x) + '_' + str(y) + '.txt','w',encoding='utf-8') as file:
    for k,v in sorted(wordfreq_doc.items(),key=lambda item: item[1]):
        if v >= len(doc_list)*(x/100):
            file.write(k+'\n')
    for k,v in sorted(wordfreq_corpus.items(),key=lambda item: item[1]):
        if v <= y:
            file.write(k+'\n')
