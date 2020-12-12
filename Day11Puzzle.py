#!/usr/bin/env python3
#%%
from collections import defaultdict
class Graph:
    def __init__(self,Data):
        pass
    
    def BuildGraph(self,Data):
        self.graph = defaultdict()
        
        pass


def GetDataRaw(): # Get Raw Data.
    with open("Day11Data.txt") as f:
        DataRaw = f.read()
    return DataRaw

def GetData(DataRaw): # Pre-process Raw Data.
    Data = DataRaw.split("\n")
    return Data

def Part1():
    Grid = Data
    OccupiedSeats = []
    EmptySeats = []
    FloorAddresses = []
    for row in Grid:
        for address in row:
            if address == "L"



    return 0

if __name__ == "__main__":
    DataRaw = GetDataRaw()
    Data = GetData(DataRaw)
    print(len(Data[0]),"x",len(Data),"=",len(Data[0])*len(Data),"Seats")

print("Done")