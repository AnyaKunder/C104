import csv 
from collections import Counter
with open ("heightWeight.csv",newline='')as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    n_num = fileData[i][2]
    newData.append(float(n_num))

data = Counter(newData)
modeDataForRange={
    '70-110':0, '110-140':0, '140-170':0
}
for height, occurence in data.items():
    if 70<float (height)<110:
        modeDataForRange['70-110']+=occurence
    elif 110<float (height)<140:
        modeDataForRange['110-140']+=occurence
    elif 140<float (height)<170:
        modeDataForRange['140-170']+=occurence
modeRange, modeOccurence=0,0
for range,occurence in modeDataForRange.items():
    if occurence>modeOccurence:
        modeRange, modeOccurence=[int(range.split('-')[0]),int(range.split("-")[1])],occurence
mode=float((modeRange[0]+modeRange[1])/2)
print("mode",mode)


    
    
        