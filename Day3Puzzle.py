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


sizeCol = numCols[0]
trees = 0
RightShiftMagnitude = 0 #Dont spin the barrel on the first iteration.
tempRow = []
for row in MapTopology:
    print("{:032b}".format(row))
    tempMapTopology = [] #Reset tempMapTopology
    for row in MapTopology:
        tempRow = (row << RightShiftMagnitude) | (row >> (sizeCol - RightShiftMagnitude))
        tempMapTopology.append(tempRow)
    MapTopology = tempMapTopology
    print("{:032b}".format(row))
    if (row >> (sizeCol-1)):
        trees = trees+1
    RightShiftMagnitude = 3 #Spin the barrel this far on all subsequent iterations.
print(trees)
# %%
