#!/usr/bin/env python3
#%%
def GetDataRaw(): # Get Raw Data.
    with open("Day10Data.txt") as f:
        DataRaw = f.read()
    return DataRaw

def GetData(DataRaw): # Pre-process Raw Data.
    Data = DataRaw.split("\n")
    Data = list(map(int,Data))
    Data.sort()
    return Data

def GetDiffArray():
    Data.insert(0,0)
    Data.append(max(Data)+3)
    DiffArray = list()
    for i in range(len(Data)-1):
        DiffArray.append(Data[i+1] - Data[i])
    return DiffArray

def GetPart1Ans(DiffArray):
    Count1 = DiffArray.count(1)
    Count3 = DiffArray.count(3)
    Ans = Count1*Count3
    return Ans

if __name__ == "__main__":
    DataRaw = GetDataRaw()
    Data = GetData(DataRaw)
    DiffArray = GetDiffArray()
    print(GetPart1Ans(DiffArray))

print("Done")
# %%
