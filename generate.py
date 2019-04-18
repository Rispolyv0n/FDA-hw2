import pandas as pd
import numpy as np
import random
from collections import Counter

# dataPath = './data.csv'
# df = pd.read_csv(dataPath)

columns = ['isStudent',  'mayNotGraduate',  'interested',  'alone',  'signUpOnline',  'attendance']
dataNum = 1000

ratio = 0.7
isStudentLst = []
for i in range(dataNum):
    if(random.random() <= ratio):
        isStudentLst.append(1)
    else:
        isStudentLst.append(0)

print(Counter(isStudentLst).keys()) # equals to list(set(words))
print(Counter(isStudentLst).values())

ratio = 0.5
aloneLst = []
for i in range(dataNum):
    if(random.random() <= ratio):
        aloneLst.append(1)
    else:
        aloneLst.append(0)

print(Counter(aloneLst).keys()) # equals to list(set(words))
print(Counter(aloneLst).values())

ratio = 0.8
signUpOnlineLst = []
for i in range(dataNum):
    if(random.random() <= ratio):
        signUpOnlineLst.append(1)
    else:
        signUpOnlineLst.append(0)

print(Counter(signUpOnlineLst).keys()) # equals to list(set(words))
print(Counter(signUpOnlineLst).values())

mayNotGraduateLst = []
ratio_1 = 0.5
ratio_2 = 0.55
ratio_3 = 0.65
ratio_4 = 0.8
for i in range(dataNum):
    getNum = random.random()
    if(getNum <= ratio_1):
        mayNotGraduateLst.append(1)
    elif(getNum <= ratio_2):
        mayNotGraduateLst.append(2)
    elif(getNum <= ratio_3):
        mayNotGraduateLst.append(3)
    elif(getNum <= ratio_4):
        mayNotGraduateLst.append(4)
    else:
        mayNotGraduateLst.append(5)

print(Counter(mayNotGraduateLst).keys()) # equals to list(set(words))
print(Counter(mayNotGraduateLst).values())

interestedLst = []
ratio_1 = 0.15
ratio_2 = 0.2
ratio_3 = 0.3
ratio_4 = 0.45
for i in range(dataNum):
    getNum = random.random()
    if(getNum <= ratio_1):
        interestedLst.append(1)
    elif(getNum <= ratio_2):
        interestedLst.append(2)
    elif(getNum <= ratio_3):
        interestedLst.append(3)
    elif(getNum <= ratio_4):
        interestedLst.append(4)
    else:
        interestedLst.append(5)

print(Counter(interestedLst).keys()) # equals to list(set(words))
print(Counter(interestedLst).values())

attendanceList = []
for i in range(dataNum):
    if(isStudentLst[i] == 1):
        if(mayNotGraduateLst[i] == 5):
            attendanceList.append(1)
        else:
            if(interestedLst[i] >= 4):
                attendanceList.append(1)
            else:
                if(aloneLst[i] == 0):
                    attendanceList.append(1)
                else:
                    if(signUpOnlineLst[i] == 0):
                        attendanceList.append(1)
                    else:
                        attendanceList.append(0)
    else:
        if(signUpOnlineLst[i] == 0):
            attendanceList.append(1)
        else:
            if(interestedLst[i] >= 3):
                if(aloneLst[i] == 0):
                    attendanceList.append(1)
                else:
                    attendanceList.append(0)
            else:
                if(aloneLst[i] == 0):
                    attendanceList.append(0)
                else:
                    attendanceList.append(1)

print(Counter(attendanceList).keys()) # equals to list(set(words))
print(Counter(attendanceList).values())

dataObj = {'isStudent': isStudentLst, 'alone': aloneLst, 'interested': interestedLst, 'mayNotGraduate': mayNotGraduateLst, 'signUpOnline': signUpOnlineLst, 'attendance': attendanceList}
df = pd.DataFrame(data=dataObj)

print(df.head())
print(df.shape)

df.to_csv(path_or_buf='test.csv', index=False, columns=['isStudent','mayNotGraduate','interested','alone','signUpOnline','attendance'])

