#!/usr/bin/env python3
#%%
import math
from itertools import permutations
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

def Part2(Data,DiffArray):
    def fact(n):
        if (n <= 1):
            return 1
        return n * fact(n - 1) 
    def nPr(n, r):
        return math.floor(fact(n) / fact(n - r))

    StartIdx = 0
    EndIdx = 0
    RangeIdxs = list()

    Data = Data[1:-1]
    DiffArray = DiffArray[1:-1]
    ## Determine blocks of data parsed by 3-gaps.
    for i,r in enumerate(DiffArray):
        if r == 3:
            EndIdx = i
            RangeIdxs.append([StartIdx,EndIdx])
            StartIdx = EndIdx+1
        if r !=3 and i+1 == len(DiffArray):
            EndIdx = i+1
            RangeIdxs.append([StartIdx,EndIdx])
            StartIdx = EndIdx+1
    ## Determine the maximum width before 3-gap
    MaxRangeLength = 0
    NumPerms = []
    for n in RangeIdxs: #For each of the 3-gap separated groups.
        RangeLength = (n[1]-n[0])+1
        MaxRangeLength = max(RangeLength,MaxRangeLength)
        for r in range(1,RangeLength):
            print(r)
            m = n[:r]
            ThisPerm = permutations(m)
            if ThisPerm
    return 0

if __name__ == "__main__":
    DataRaw = GetDataRaw()
    Data = GetData(DataRaw)
    DiffArray = GetDiffArray()
    print(GetPart1Ans(DiffArray))
    Part2(Data,DiffArray)

print("Done")
#%%
x = list(range(1,5+1))
print(x)
y = [2,3,4,5,6]
z = y[:3]
print(z)
from collections import Counter  
c = Counter({0:1})
print (c)
# %%
from collections import Counter  
data = sorted([int(x.strip()) for x in open("Day10Data.txt")] + [0])  
c = Counter({0:1})  
for x in data:  
    c[x+1] += c[x]  
    c[x+2] += c[x]  
    c[x+3] += c[x] 
print("Part 2:", c[max(data) + 3])
# %%
