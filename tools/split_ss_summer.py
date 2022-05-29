# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:51:21 2021

@author: jonas
"""
import re
import os

# =============================================================================
#Save temporarily stored text to a file
def save_temp():
    global file_counter, file_temp, file_name
    
    #Create file
    print(file_counter)
    filename = directory[0] + str(file_counter).zfill(2) + '_' + descriptor[file_counter-30] + '.txt'
    filename_E = directory[1] + str(file_counter).zfill(2) + '_' + descriptor[file_counter-30] + '_E.txt'        
    filename_G = directory[2] + str(file_counter).zfill(2) + '_' + descriptor[file_counter-30] + '_G.txt' 
    filename_P = directory[3] + str(file_counter).zfill(2) + '_' + descriptor[file_counter-30] + '_P.txt'
    
    #Clean the file
    file_temp = file_temp.lower() #Lower case
    file_temp = re.sub('[/.:?]','',file_temp) #Remove special characters
    file_temp = re.sub('=\n','',file_temp) #Contract hyphenated words
    file_temp = re.sub('\n',' ',file_temp) #Substitute new line with space
    file_temp = re.sub(' +', ' ', file_temp) #Reduce surplus spacing
    
    keyword_1 = 'dette hellige evangelium'
    if file_counter == 36:
        keyword_2 = 'bønnen'
    else:
        keyword_2 = 'bønen'
    
    #Exceptions noted by order of appearance
    pos_1 = re.search(keyword_1,file_temp).start()
    pos_2 = []
    for match in re.finditer(keyword_2,file_temp):
        pos_2.append(match.start())
        
    save_split(filename_E,file_temp,0,pos_1)
    save_split(filename_G,file_temp,pos_1,pos_2[-1])
    save_split(filename_P,file_temp,pos_2[-1],len(file_temp))
        
    save_split(filename,file_temp,0,len(file_temp))
    
    file_counter += 1
    file_temp = ''
# =============================================================================        
def save_split(file,text,pos_1,pos_2):
    with open(file,'w',encoding='utf-8') as output:
        output.write(text[pos_1:pos_2])
# =============================================================================            
descriptor = ['Easter','2aftEas','3aftEas','1SafEas','2SafEas','3SafEas',
              '4SafEas','5SafEas','Ascension','6SafEas','Pentecost','2aftPent',
              '3aftPent','Trinity','1SaftTrin','2SaftTrin','3SaftTrin',
              'StJohBap','4SaftTrin','MaryVisit','5SaftTrin','6SaftTrin',
              '7SaftTrin','8SaftTrin','9SaftTrin','10SaftTrin','11SaftTrin',
              '12SaftTrin','13SaftTrin','14SaftTrin','15SaftTrin','16SaftTrin',
              'StMichael','17SaftTrin','18SaftTrin','19SaftTrin','20SaftTrin',
              '21SaftTrin','AllSaints','22SaftTrin','23SaftTrin','24SaftTrin',
              '25SaftTrin','26SaftTrin','27SaftTrin']

directory = ['output_ss_summer_sunfeast/','output_ss_summer_sermons_e/',
             'output_ss_summer_sermons_g/','output_ss_summer_prayer/']

file_name = ''
file_counter = 30
file_temp = '' #Temporarily stores text for next file save

section_counter_pri = False #Switch for preparing a save after 'prayer' section
section_counter_sec = False #Switch for when a key term occurs multiple times before file save
    
os.chdir('../ss-summer/')
file = open('Sabbati_Sanctificatio_Sommer_(Brochmand).txt','r',encoding='utf-8')
# =============================================================================

#Create directory
for i in range(4):
    try:
        os.mkdir(directory[i])
    except:
        pass

for line in file:
    #Main trigger
    if 'Amen' in line or 'AMEN' in line or 'men.\n' in line:
        if section_counter_pri == True:
            section_counter_pri = False
            file_temp += line
            save_temp()
        else:
            file_temp += line
    elif 'Bønen.\n' in line or 'Bønnen.\n' in line:
        section_counter_pri = True
        file_temp += line
    #Exceptions
    else:
        file_temp += line

save_temp() #Saves the last remaining file

file.close()
