#%%
DEBUG = False

def GetMapTopology():
    f = open("Day3Data.txt", "r")
    linesRaw = f.readlines()
    
    lines = []
    
    for line in linesRaw:
        lines.append(line.strip())

    Dictionary = {
        ".":"0",
        "#":"1"}

    MapTopology = []
    for line in lines:
        for Dict_Find, Dict_Repl in Dictionary.items():
            line = line.replace(Dict_Find, Dict_Repl)
        MapTopology.append(int(line,2))
    
    def GetPisteWidth():
        PisteWidth = len(lines[0])
        return PisteWidth
    
    PisteWidth = GetPisteWidth()

    return MapTopology,PisteWidth

def GetTreesOnRun(DownShiftMagnitude,RightShiftMagnitude,PisteWidth):
    thisRow = 0
    thisCol = PisteWidth-1
    
    TreesOnRun = 0
    while thisRow < len(MapTopology):
        row = MapTopology[thisRow]

        ## Wrap handler
        if (thisRow==0):
            thisCol = thisCol
        elif (thisCol-RightShiftMagnitude)>=0: #Moving right: Normal
            thisCol -= RightShiftMagnitude
            if(DEBUG): print("norm")
        elif (thisCol-RightShiftMagnitude)<0: #Moving right: Need to wrap
            thisCol = PisteWidth+(thisCol-RightShiftMagnitude)
            if(DEBUG): print("right wrap")
        elif (thisCol-RightShiftMagnitude)>PisteWidth: #Moving left: Need to wrap
            if(DEBUG): print("left wrap")
            thisCol = ((thisCol-RightShiftMagnitude)-PisteWidth)
        
        if(DEBUG): print("Row: ",thisRow,"-----","Column: ",thisCol)
        if(DEBUG): print("Map Row  : ","{:031b}".format(row))
        if(DEBUG): print("Check Row: ","{:031b}".format(1<<(thisCol)))

        treeYN = (row >> (thisCol)) & 1
        if(DEBUG): print("Is Tree? : ",treeYN)

        if (treeYN):
            TreesOnRun = TreesOnRun+1
        thisRow += DownShiftMagnitude
    return TreesOnRun

MapTopology,PisteWidth = GetMapTopology()

Runs = [
    [1,1],
    [1,3],
    [1,5],
    [1,7],
    [2,1]]

TreesPerRun = []
for down, right in Runs:
    TreesOnRun = GetTreesOnRun(int(down),int(right),PisteWidth)
    print("Count of Trees : ",TreesOnRun)
    TreesPerRun.append(TreesOnRun)
ProductOfTrees = 1
for x in TreesPerRun:
    ProductOfTrees *= x
print("Product of Trees : ",ProductOfTrees)

# %%
