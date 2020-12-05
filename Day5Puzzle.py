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
    return max(x.SeatIndex for x in passes)

def FindSeat(passes):
    AllSeatsOccupied = []
    for x in passes:
        AllSeatsOccupied.append(x.SeatIndex)
    AllSeatsOccupied.sort()
    AllSeatsOccupied = set(AllSeatsOccupied)
    AllSeats = set(range(min(x.SeatIndex for x in passes),max(x.SeatIndex for x in passes)+1))
    return next(iter(AllSeats.difference(AllSeatsOccupied)))

if __name__ == "__main__":
    passes = GetPasses()
    print(GetPlaneStatus(passes))
    print(FindSeat(passes))

print("Done")