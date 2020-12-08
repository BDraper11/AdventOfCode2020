#!/usr/bin/env python3
#%%
'''
1) Parse data by "bags contain" to get LHS Subject Bag & RHS Subject Bag Rules - Dictionary?
2) 

NEED TO REVISIT THE CLASS SETUP
MAKE CHILD BAGS INSTANCES OF THEIR PARENT TYPES (POINTERS MAYBE?) CAN YOU DO POINTER TO A AS YET NOT DEFINED TYPE?
MAYBE A METHOD FOR USE AFTER ALL THE PARENTS HAVE BEEN DEFINED FIRST.
'''
import re
class Bag:
    def __init__(self,BagData):
        self.ParentFactor = 1
        self.Instances = 1
        self.BagType, self.Rules = BagData.split(" bags contain ")
        self.ChildBags = self.Rules.split(", ")
        self.RegEx = re.compile("(\d)+(\s)+")
        for idx,SubRule in enumerate(self.ChildBags):
            self.ChildBags[idx] = SubRule[:SubRule.find(" bag")]
            if self.ChildBags[idx] != "no other":
                x = self.ChildBags[idx].split()
                self.ChildBags[idx] = [x[0],x[1]+" "+x[2]]


def GetDataRaw(): # Get Raw Data.
    with open("Day7Data.txt") as f:
        DataRaw = f.read()
    return DataRaw

def GetData(DataRaw): # Pre-process Raw Data.
    Data = DataRaw.split("\n")
    return Data

def GetBags(Data):
    Bags = []
    for BagData in Data:
        Bags.append(Bag(BagData))
    #for Bag in Bags:

    return Bags

def GetValidBags(Rules,SearchBags):
    ValidBags = []
    CountValidBags = len(ValidBags)
    for SearchBag in SearchBags:
        for Bag,Rule in Rules:
            if any(SearchBag in pergatory for pergatory in Rule):
                #if SearchBag not in ValidBags:
                ValidBags.append(Bag)
                SearchBags.append(Bag)
    ValidBags = set(ValidBags)
    return ValidBags

def GetTotalBagsForGold(Bags,ThisLayerBags,ParentLayerFactor = [1],ThisLayerFactors = [1],FoundBags = []):
    SubLayerFactors = []
    SubLayerBags = []

    for Layeridx,LookUpBag in enumerate(ThisLayerBags): # For each Bag at this layer.

        for idx,Bag in enumerate(Bags): # Get the bag object and it's index from the library of bags.

            if Bag.BagType == LookUpBag: # Find the bag in question.
                Bag.Instances = ThisLayerFactors[Layeridx]*ParentLayerFactor[Layeridx]
                Bag.InheritedFactor = ThisLayerFactors[Layeridx] # Update the bags inherited factor.
                
                FoundBags.append(Bag) # Get Bag object if it's what we're looking for.

                #ThisLayerFactors.pop(Layeridx) # 
                #ThisLayerBags.remove(LookUpBag)
                print(idx,Bag.InheritedFactor,Bag.BagType)
                ParentLayerFactor.append(Bag.Instances)

                if Bag.Bags != ["no other"]:
                    for SubBag in Bag.Bags: # Find the count and type of sub-bags.
                        #Bags.SubBag.
                        SubLayerFactors.append(int(SubBag[0]))
                        SubLayerBags.append(SubBag[1])
    ThisLayerBags = SubLayerBags
    ThisLayerFactors = SubLayerFactors
    if ThisLayerBags == []:
        return FoundBags
    else:
        GetTotalBagsForGold(Bags,ThisLayerBags,ParentLayerFactor,ThisLayerFactors,FoundBags)
    return FoundBags



if __name__ == "__main__":
    MyBag = "shiny gold"
    SearchBags = [MyBag]
    DataRaw = GetDataRaw()
    Data = GetData(DataRaw)
    Bags = GetBags(Data)
    #print(len(GetValidBags(Bags,SearchBags))) #Doesn't work since switching to classes again. Need to fix.....
    #print(GetTotalBagsForGold(Bags,SearchBags))
    #print(len(ValidBags))
print("Done")
#%%


#%%
x = list(["a","b","c","d"])
y = list(["r","s","t"])
z = list([x,y])
print("b" in z)
print("b" in x)

#%%
x = "4 wavy gray"
y = [int(char) for char in x.split() if char.isdigit()][0]
z = ''.join([char for char in x if not char.isdigit()])
# %%
