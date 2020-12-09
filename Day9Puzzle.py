#!/usr/bin/env python3
#%%
def GetDataRaw(): # Get Raw Data.
    with open("Day9Data.txt") as f:
        DataRaw = f.read()
    return DataRaw

def GetData(DataRaw): # Pre-process Raw Data.
    Data = DataRaw.split("\n")
    return Data

def CheckValid():
    

if __name__ == "__main__":
    Range = 25

    DataRaw = GetDataRaw()
    Data = GetData(DataRaw)

print("Done")