#%%
import string

class Group:
    def __init__(self,GroupBlock,Part):
        def GetPassengers(self,GroupBlock):
            PassengersRaw = []
            PassengersRaw = GroupBlock.split("\n")
            Passengers = []
            for PassengerBlock in PassengersRaw:
                Passengers.append(self.Passenger(PassengerBlock))
            return Passengers
        def GetGroupYesAnswers(self):
            if self.Part == 1:
                GroupYesAnswers = set()
                for p in self.Passengers:
                    GroupYesAnswers = GroupYesAnswers.union(p.YesAnswers)
            elif self.Part == 2:
                GroupYesAnswers = set(string.ascii_lowercase)
                for p in self.Passengers:
                    GroupYesAnswers = GroupYesAnswers.intersection(p.YesAnswers)
            return GroupYesAnswers
        def GetCountGroupYesAnswers(self):
            CountGroupYesAnswers = len(self.GroupYesAnswers)
            return CountGroupYesAnswers

        self.Part = Part
        self.Passengers = GetPassengers(self,GroupBlock)
        self.GroupYesAnswers = GetGroupYesAnswers(self)
        self.CountGroupYesAnswers = GetCountGroupYesAnswers(self)
        pass
    class Passenger:
        def __init__(self,PassengerBlock):
            self.YesAnswers = set(PassengerBlock)
        pass
    pass

def GetDataRaw(): # Get Raw Data.
    with open("Day6Data.txt") as f:
        DataRaw = f.read()
    return DataRaw

def GetData(DataRaw): # Pre-process Raw Data.
    Data = DataRaw.split("\n\n")
    return Data

def GetGroups(Data,Part = 1):
    Groups = []
    for GroupBlock in Data:
        Groups.append(Group(GroupBlock,Part))
    return Groups

def GetSumGroupsYesAnswers(Groups):
    SumGroupsYesAnswers = 0
    for Group in Groups:
        SumGroupsYesAnswers += Group.CountGroupYesAnswers
    return SumGroupsYesAnswers

if __name__ == "__main__":
    DataRaw = GetDataRaw()
    Data = GetData(DataRaw)
    Groups = GetGroups(Data,2)
    print(GetSumGroupsYesAnswers(Groups))
print("Done")
#%%
class Passenger:
        def __init__(self,PassengerBlock):
            self.YesAnswers = []
        pass

#%%
x = set()
y = {1,2,3,4,5}
a = x.union(y)
z = {5,6,7,8,9}
b = a.union(z)