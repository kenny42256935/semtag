# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:31:37 2024

@author: Kenny
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:55:05 2021

@author: kenny
"""


################################ TO READ the file names of file
filename = open('filename-COUNT.txt','r', encoding='utf-8')     #filename.txt contains all genre files

############印出所有TAG name, file=m 在最後面
m = open('filename-COUNT.csv', 'a',encoding='utf-8')    #Target file to write to
print("tag-count,filename,substantiality,positive-emo,negative-emo,neutral-emo,acts,static,\
external,habitual,state,status,spatial,temporal,quantity,abstract,social,\
observation,judgment,\
animal,human,organization,Food&Beverage,clothing,amusement,transportation,\
body-part,activity,place,item,academics,plant,building,health,tool,environment,\
communication,wh-pronoun,joy,trust,surprise,anticipation,acknowledgment,fear,sadness,disgust,anger,\
disappointment,moment,number,idea,lifestyle,event,impingement,action,process,measurement,\
moving,motion,emotive,denial,ambient,psych,possession,factual,expectation,cognition,\
sensation,experience,gratitude,light,color,sound,taste,smell,surface,pattern,efficiency,\
action-style,smoothness,composition,type,stability,consistency,ripeness,dampness,purity,\
gravity,physics,chemistry,temperature,alive,affliction,desire,appearance,position,\
dimension,direction,location,origin,distribution,form,present,distance,demonstrative,time,velocity,\
age,sequence,modal,amount,cost,profit,frequency,perception,intelligence,knowledge,\
human-like,animal-like,discipline,skill,sympathy,inclination,method,luck,wh-adverb,class,\
institution,religion,racial,requirement,function,purpose,relation,sameness,format,benefit,\
compare,evaluation,validity,certainty,effectiveness,difficulty,security,order,accuracy,\
degree,quality", file=m)



###################處理多檔案循環
for filenames in filename:
    filename1 = filenames.strip()
     
    f = open(filename1, 'r', encoding='utf-8')        #Target file to read
    word = f.read()                                        #word=content in 'f'
    
    
    #計算TAG數量列在第一格文件行數就是字數
    words = len(word.split('\n'))                           #'len'計算行數-換行符號 就是字數)
    print(str(words)+',', end='', file=m)
    
    #Each text, text name
    filename = filename1.split('.')
    print(str(filename[0])+',', end='', file=m)
    
    sub = ",substantiality";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",positive-emo";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",negative-emo";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",neutral-emo";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",acts";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",static";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",external";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",habitual";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",state";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",status";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",spatial";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",temporal";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",quantity";
    print(str(word.count(sub))+',', end='', file = m)
    
    sub = ",abstract";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",social";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",observation";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",judgment";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",animal";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",human";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",organization";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",Food&Beverage";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",clothing";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",amusement";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",transportation";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",body-part";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",activity";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",place";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",item";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",academics";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",plant";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",building";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",health";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",tool";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",environment";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",communication";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",wh-pronoun";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",joy";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",trust";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",surprise";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",anticipation";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",acknowledgment";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",fear";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",sadness";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",disgust";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",anger";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",disappointment";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",moment";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",number";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",idea";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",lifestyle";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",event";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",impingement";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",action";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",process";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",measurement";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",moving";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",motion";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",emotive";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",denial";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",ambient";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",psych";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",possession";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",factual";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",expectation";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",cognition";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",sensation";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",experience";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",gratitude";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",light";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",color";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",sound";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",taste";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",smell";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",surface";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",pattern";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",efficiency";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",action-style";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",smoothness";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",composition";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",type";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",stability";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",consistency";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",ripeness";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",dampness";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",purity";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",gravity";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",physics";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",chemistry";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",temperature";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",alive";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",affliction";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",desire";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",appearance";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",position";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",dimension";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",direction";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",location";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",origin";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",distribution";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",form";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",present";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",distance";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",demonstrative";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",time";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",velocity";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",age";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",sequence";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",modal";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",amount";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",cost";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",profit";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",frequency";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",perception";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",intelligence";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",knowledge";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",human-like";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",animal-like";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",discipline";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",skill";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",sympathy";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",inclination";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",method";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",luck";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",wh-adverb";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",class";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",institution";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",religion";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",racial";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",requirement";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",function";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",purpose";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",relation";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",sameness";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",format";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",benefit";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",compare";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",evaluation";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",validity";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",certainty";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",effectiveness";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",difficulty";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",security";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",order";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",accuracy";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",degree";
    print(str(word.count(sub))+',', end='', file = m)

    sub = ",quality";
    print(str(word.count(sub))+',', file = m)

  
    
f.close()
m.close()    
