#!/usr/bin/env python3
#%%
class Bag:
    def __init__(self,BagName):
        self.BagName = BagName
        self.Parent = []
        self.ParentFactor = []
        self.Instances = []
        self.BagsContained = 0
    def SetParent(self,Parent):
        self.Parent = Parent
    def SetParentFactor(self,ParentFactor):
        self.ParentFactor = ParentFactor
    def SetInstances(self,Instances):
        self.Instances = Instances
    def SetBagsContained(self,BagsContained):
        self.BagsContained = BagsContained

def GetDataRaw(): # Get Raw Data.
    with open("Day7Data.txt") as f:
        DataRaw = f.read()
    return DataRaw

def GetData(DataRaw): # Pre-process Raw Data.
    Data = DataRaw.split("\n")
    return Data

def ParseBagData(BagData):
    #Bag == Node; AdjacentNodes == AdjacentNodes
    AdjacentNodes = []
    AdjacentNodesFactors = []

    Bag, Rules = BagData.split(" bags contain ") #Parse Node from adjacent nodes.
    if "no other" in Rules: #Check if there are no adjacent nodes.
        pass
    else:
        AllAdjacentNodes = Rules.split(", ") #Parse out each adjacent node
        for ThisAdjacentNode in AllAdjacentNodes: #For each adjacent node
            ThisAdjacentNode = ThisAdjacentNode[:ThisAdjacentNode.find(" bag")] #Trim the bag bit off the end
            ThisAdjacentNode = ThisAdjacentNode.split() #Break it up by spaces to extract the Factor and the adjacent node name
            AdjacentNodesFactors.append(int(ThisAdjacentNode[0])) #Split the factor off, need to do this first.
            AdjacentNodes.append(ThisAdjacentNode[1]+" "+ThisAdjacentNode[2]) #Take the adjacent node name.
    return Bag, AdjacentNodes,AdjacentNodesFactors

def GetBags(Data):
    Bags = dict()
    for BagData in Data:
        Bag, AdjacentNodes,AdjacentNodesFactors = ParseBagData(BagData)
        Bags[Bag] = [AdjacentNodes,AdjacentNodesFactors]
    return Bags

def DFS(Bags,Start,Path = [],PathBags = [],Instances = 1,Parent = [],ParentFactor = 1):
    #print("Testing --->  ",Start)
    if Start not in Path: #If we've not been here before....
        PathBags.append(Bag(Start))
        PathBags[-1].SetInstances(Instances)
        PathBags[-1].SetParent(Parent)
        ParentFactor = ParentFactor*Instances
        PathBags[-1].SetParentFactor(ParentFactor)
        Path.append(Start)
        if Start not in Bags:
            # leaf node, backtrack
            return Path,PathBags
        #print(Bags[Start][0])
        if Bags[Start][0] == []:
            return Path,PathBags
        for idx,Child in enumerate(Bags[Start][0]): #For each child bag.
            #print(Child,Path,PathBags,Bags[Start][1][idx],Start,ParentFactor)
            Path,PathBags = DFS(Bags,Child,Path,PathBags,Bags[Start][1][idx],Start,ParentFactor)
    return Path,PathBags

def GetPart2Answer(PathBags):
    Ans = 0
    for Bag in PathBags:
        Ans += Bag.ParentFactor
    return Ans

if __name__ == "__main__":
    MyBag = "shiny gold"

    DataRaw = GetDataRaw()
    Data = GetData(DataRaw)
    Bags = GetBags(Data)
    Path,PathBags = DFS(Bags,MyBag)
    print(GetPart2Answer(PathBags))
print("Done")