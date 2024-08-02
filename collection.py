from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'Name':[],'Address':[],'Phone No.':[]}


def sorted_dir_list():
    temp = [int(i.split(".")[0]) for i in os.listdir("SchoolData")]
    temp = []
    final_list = [f"{i}.html" for i in temp]
    return final_list


cnt =0

for file in os.listdir("SchoolData"):
    try:
        with open(f"SchoolData/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc,'html.parser')

        cnt+=1
        N = soup.find('span',class_='OSrXXb')
        Name = N.get_text()


        adds = soup.find_all('div')
        i=0
        for add in adds:
            if(i==7):
                Add=add.get_text() #if adds else "N/A"
            if(i==8):
                no = add.get_text() # if adds else "N/A"
            i+=1

        #print(file)
        # print(Name)
        #print(Add)
        # print(no)    
        d['Name'].append(Name)
        d['Address'].append(Add)
        d['Phone No.'].append(no)
    except Exception as e:
        print("e") 
print(cnt)
try:
    df=pd.DataFrame(data=d)           
    df.to_csv("School.csv")
except Exception as e:
    print(e)    
