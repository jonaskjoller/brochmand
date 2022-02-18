import re
import os

wordlist = []
wordfreq_corpus = {}
wordfreq_doc = {}
file_list = []
dir_list = []
doc_list = []
keyword = ''


# List possible files in folder
counter = 0
for items in os.listdir():
    if items.endswith('.txt'):
        file_list.append(items)
        print (counter, items)
        counter += 1

filename = file_list[int(input('\nSelect corpus-file by entering file-number: '))]
print()

# #List subfolders
# counter = 0
# for items in os.scandir():
#     if items.is_dir():
#         dir_list.append(items)
#         print (counter, items.name)
#         counter += 1

# foldername = dir_list[int(input('\nSelect subfolder by entering folder-number: '))]

# #Get name of folder to use as naming scheme
# keyword = os.getcwd().split('\\')[-1]

#Clean file
with open(filename,'r',encoding='utf-8') as file:
    file = file.read()
    file = file.lower() #Lower case
    file = re.sub('[/.:?;]','',file) #Remove special characters
    file = re.sub('=\n','',file) #Contract hyphenated words
    file = re.sub('\n',' ',file) #Substitute new line with space
    file = re.sub(' +', ' ', file) #Reduce surplus spacing
    wordlist = file.split()
    
with open('word_context.txt','w',encoding='utf-8') as file:    
    for x in range(0,len(wordlist)):
        if wordlist[x].startswith('betenck'):
            if wordlist[x-1].startswith('gudelig'):
                pass
            else:             
                temp = ''
                wordlist[x] = wordlist[x].upper()
                for word in wordlist[x-5:x+6]:
                    temp += word+' '
                file.write(temp+'\n')
            
