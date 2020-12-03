#%%
f = open("Day3Data.txt", "r")
linesRaw = f.readlines()

lines = []
numCols = []
for line in linesRaw:
    lines.append(line.strip())
    numCols.append(len(lines[0]))

NewDataStr = []
MapTopology = []

Dictionary = {
    ".":"0",
    "#":"1"}

for line in lines:
    for Dict_Key, Dict_Val in Dictionary.items():
        line = line.replace(Dict_Key, Dict_Val)
    NewDataStr.append(line)
    MapTopology.append(int(line,2))

def checkslope(DownShiftMagnitude,RightShiftMagnitude):
    thisRow = 0
    thisCol = numCols[0]-1
    
    trees = 0
    while thisRow < len(MapTopology):
        row = MapTopology[thisRow]

        ## Wrap handler
        if (thisRow==0):
            thisCol = thisCol
        elif (thisCol-RightShiftMagnitude)>=0: #Moving right: Normal
            thisCol -= RightShiftMagnitude
            #print("norm")
        elif (thisCol-RightShiftMagnitude)<0: #Moving right: Need to wrap
            thisCol = numCols[0]+(thisCol-RightShiftMagnitude)
            #print("right wrap")
        elif (thisCol-RightShiftMagnitude)>numCols[0]: #Moving left: Need to wrap
            #print("left wrap")
            thisCol = ((thisCol-RightShiftMagnitude)-numCols[0])
        
        #print("Row: ",thisRow,"-----","Column: ",thisCol)
        #print("Map Row  : ","{:031b}".format(row))
        #print("Check Row: ","{:031b}".format(1<<(thisCol)))

        treeYN = (row >> (thisCol)) & 1
        #print("Is Tree? : ",treeYN)

        if (treeYN):
            trees = trees+1
        thisRow += DownShiftMagnitude
    return trees

Runs = {
    "1":"1",
    "1":"3",
    "1":"5",
    "1":"7",
    "2":"1"}

A = checkslope(1,1)
B = checkslope(1,3)
C = checkslope(1,5)
D = checkslope(1,7)
E = checkslope(2,1)
print("Count of Trees : ",A)
print("Count of Trees : ",B)
print("Count of Trees : ",C)
print("Count of Trees : ",D)
print("Count of Trees : ",E)
ans = A*B*C*D*E
print(ans)


# %%
