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

thisRow = 0
thisCol = numCols[0]
RightShiftMagnitude = 3
trees = 0

while thisRow < len(MapTopology):
    row = MapTopology[thisRow]

    print(thisRow,"-----",thisCol)
        
    if (thisRow==0):
        thisCol = thisCol
    elif (thisCol-RightShiftMagnitude)>=0: #Moving right: Normal
        thisCol -= RightShiftMagnitude
        print("norm")
    elif (thisCol-RightShiftMagnitude)<0: #Moving right: Need to wrap
        thisCol = numCols[0]+(thisCol-RightShiftMagnitude)+1 #watch out here
        print("right wrap")
    elif (thisCol-RightShiftMagnitude)>numCols[0]: #Moving left: Need to wrap
        print("left wrap")
        thisCol = ((thisCol-RightShiftMagnitude)-numCols[0])-1 #watch out here
    
    print("{:031b}".format(row))
    if (thisCol>0):
        treeYN = (row >> (thisCol-1)) & 1
        print("{:031b}".format(1<<(thisCol-1)))
    else:
        treeYN = row & 1
        print("{:031b}".format(1))
    
    print(treeYN)
    
    

    #if thisRow == 31:
        #break
    
    
    if (treeYN):
        trees = trees+1
    thisRow += 1
    print(trees)

#print(trees)
# %%
