import pandas as pd
data = pd.read_csv("sample.txt")

lines=[]
a=[]
c=0

for line in pd.read_csv('sample.txt', encoding='utf-8', header=None, chunksize=1):
   lines.append(line.iloc[0,0])
for line in lines:
    c=c+1 # This counts the total number of lines
count=0
for line in lines:
    a=list(line)
    for i in range(0,len(a)-1):
        if a[i] == "/" and a[i+1]=="/":
            count=count+1
        elif a[i] == "/" and a[i+1] == "*" :
            count=count+1
        elif a[i].isalpha():
            continue
 print(c-count) #Lines of code       
