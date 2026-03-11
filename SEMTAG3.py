# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 13:58:23 2026

@author: user
"""

import pandas as pd

for i in range(13,16,1):  #最高數字要減一(1~3 最高要用4)
    with open("SEMTAG-3-0"+str(i)+"-output.csv", 'a', encoding='utf-8') as m:
    
        df = pd.read_excel("SEMTAG-0"+str(i)+".xlsx", sheet_name="工作表1")
        
    
        for index, row in df.iterrows():
    
            for label, value in row.items():
                     
                TOKEN = f"{label}:{value}"
                print(TOKEN)
    
                
                from ollama import Client
                client = Client(
                    host='http://localhost:11434',
                    headers={'x-some-header': 'some-value'}
                    )
                response = client.chat(model='gemma3', messages=[
                    {'role': 'system', 'content': '請根據輸入的詞，翻譯成英文，只需要輸出3個以內結果，用逗點連接，不需要其他說明'},
                    {'role': 'user', 'content': TOKEN },
                    ])
                print(response.message.content)
                print(TOKEN +","+ response.message.content, file=m)