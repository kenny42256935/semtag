# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:49:31 2024

@author: Kenny
"""

import pandas as pd

################################################ TO READ the file names of each genre
filename = open('filename.txt','r', encoding='utf-8')     #filename.txt contains all genre files
for filenames in filename:
    filename1 = filenames.strip()
    filename2 = filename1.split('.')
    filename3 = filename2[0]               #get the filename without '.txt'

################################################ TO ADD SEMTAG to ORIGINAL FILE
    
    with open(filename3+'.txt','r', encoding='utf-8') as n:     
        while True:
            lines = n.readline()          #lines=[str]
            if not lines:
                break
            lines = lines.strip()         #chop off "\n"
            token = lines.split(',')      #convert str into list
            #print(token[1])               #now token have two list items [0] and [1]
            #print(type(token[1]))         #list items has str property
            token1=token[0]  
            token2=token[1]
    
################################################ TO RETRIVE SEMTAG
            sem1 = pd.read_csv('semtag-.csv', encoding='UTF-8', index_col = 0)     #sem1=dataframe all
            sem2 = sem1[sem1['TOKEN'] == token1]                                  #sem2=finds token match
            sem3 = sem2[sem2['POS'] == token2]                                    #sem3=finds POS match
            if sem3.empty:
                with open(filename3+'-TAG.csv','a', encoding='UTF-8') as f:
                    print(token1+','+token2+',NOT in semtag.csv,', file=f)   
                continue
            
            semA = sem3.iat[0,4]                              #0=TOKEN, 1=POS, 2=FRE, 3=SEM0, 4=SEM1, 5=SEM2
            semB = sem3.iat[0,5]                              #0=TOKEN, 1=POS, 2=FRE, 3=SEM0, 4=SEM1, 5=SEM2
            semup = str(semA)                                 #null semA and semB are float
            semdown = str(semB) 
            # print(sem5)
            # print(type(sem5))

################################################### TO WRITE TO NEW TAGGED FILE             
            with open(filename3+'-TAG.csv','a', encoding='UTF-8') as f:
                print(token1+','+token2+','+semup+','+semdown, file=f)   

#filename.close()