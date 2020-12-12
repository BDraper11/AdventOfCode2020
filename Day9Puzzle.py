#!/usr/bin/env python3

#%%
def GetDataRaw(): # Get Raw Data.
    with open("Day9Data.txt") as f:
        DataRaw = f.read()
    return DataRaw

def GetData(DataRaw): # Pre-process Raw Data.
    Data = DataRaw.split("\n")
    Data = list(map(int,Data))
    return Data

def CheckValid(StartIdx,Range):
    CheckValue = Data[StartIdx+Range]
    CheckRange = Data[StartIdx:StartIdx+Range]
    AnswerRange = []
    for r in CheckRange:
        for s in CheckRange:
            AnswerRange.append(r+s)
    if CheckValue not in AnswerRange:
        return CheckValue
    return 0

def FindSumRange(Value,StartIdx,Length = 0):
    CheckRange = Data[StartIdx:StartIdx+Length] #Ini
    while sum(CheckRange) < Value:
        CheckRange = Data[StartIdx:StartIdx+Length]
        Length+=1
    
    if sum(CheckRange) == Value:
        Min = min(CheckRange)
        Max = max(CheckRange)
        return Min, Max
    return 0,0


if __name__ == "__main__":
    Range = 25

    DataRaw = GetDataRaw()
    Data = GetData(DataRaw)
    for i in range(len(Data)):
        Value = CheckValid(i,Range)
        #print(Value)
        if Value > 0:
            print(Value)
            break
    
    for i in range(len(Data)):
        Min, Max = FindSumRange(Value,i)
        if Min > 0 and Max > 0:
            print(Min, Max)
            print(sum([Min,Max]))
            break

print("Done")