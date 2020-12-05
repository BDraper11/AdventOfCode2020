#%%
class BoardingPass():
    def __init__(self,thispass,ClassDebugOn = 0):
        rowMap = thispass[:7]
        colMap = thispass[7:]
        if ClassDebugOn:
            print(thispass)
            print(rowMap)
            print(colMap)
        
        def RangeFinder(RangeMap,UpperKey,LowerKey,SizeOfRange,StartOfRange = 0):
            thisrange = list(range(StartOfRange,SizeOfRange))
            for split in RangeMap:
                midpoint = int(len(thisrange)/2)
                if split == UpperKey:
                    thisrange = thisrange[midpoint:]
                elif split == LowerKey:
                    thisrange = thisrange[:midpoint]
                else:
                    return None
            return thisrange[0]

        def GetRow(self,rowMap):
            return RangeFinder(rowMap,"B","F",128)
        def GetCol(self,colMap):
            return RangeFinder(colMap,"R","L",8)
        def GetIndex(self):
            return self.SeatRow*8+self.SeatCol

        self.SeatRow = GetRow(self,rowMap)
        self.SeatCol = GetCol(self,colMap)
        self.SeatIndex = GetIndex(self)
 
def GetPasses():
    with open("Day5Data.txt") as f:
        passesRaw = f.read().splitlines()
        passes = []
        for thispass in passesRaw:
            passes.append(BoardingPass(thispass,0))
    return passes

def GetPlaneStatus(passes):
    print(max(x.SeatIndex for x in passes))

def FindSeat(passes):
    AllSeats = []
    AllSeats.append(x.SeatIndex for x in passes)
    AllSeats.sort()
    pass


if __name__ == "__main__":
    passes = GetPasses()
    GetPlaneStatus(passes)
    FindSeat(passes)


print("Done")
# %%
rows = list(range(0,128))
            for split in rowMap:
                midpoint = int(len(rows)/2)
                if split == "B":
                    rows = rows[midpoint:]
                elif split == "F":
                    rows = rows[:midpoint]
                else:
                    return None
            return rows[0]