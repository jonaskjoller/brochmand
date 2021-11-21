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
for file in os.listdir():
    if file.endswith('.txt'):
        file_list.append(file)
        print (counter, file)
        counter += 1

filename = file_list[int(input('\nSelect corpus-file by entering file-number: '))]
print()

#List subfolders
counter = 0
for folder in os.scandir():
    if folder.is_dir():
        dir_list.append(folder)
        print (counter, folder.name)
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
for word in wordlist:
    wordfreq_corpus[word] =  wordfreq_corpus.get(word,0) + 1

#Generate list of filepaths to individual documents
for file in os.listdir(foldername):
    if file.endswith('.txt'):
        doc_list.append(foldername.name + '/' + file)

#Build word frequency of individual documents
counter = 0
for document in doc_list:
    with open(document,'r',encoding='utf-8') as file:
        #Generate dictionary of unique word forms in file
        file_dic = {}
        for word in file.read().split():
            file_dic[word] = file_dic.get(word,0) +1
        #Compare word forms in file and corpus
        for key_1 in wordfreq_corpus:
            for key_2 in file_dic:
                if key_1 == key_2:
                    wordfreq_doc[key_1] = wordfreq_doc.get(key_1,0) + 1
    #Keep track of files processed
    counter += 1
    print('Completed',counter, 'out of',len(doc_list),flush=True)
                 
#Save a new file
with open('stopword_' + keyword + '_' + str(x) + '_' + str(y) + '.txt','w',encoding='utf-8') as file:
    for key,value in wordfreq_doc.items():
        if value >= len(doc_list)*(x/100):
            file.write(key+'\n')
    for key,value in wordfreq_corpus.items():
        if value <= y:
            file.write(key+'\n')
