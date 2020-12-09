#!/usr/bin/env python3
'''
For every instruction in set
    find if instr == nop or jmp
        if nop <==> jmp
        if jmp <==> nop
    run instrset
    check if finished
        yes -> break
        no -> cont
    refresh instrset
    next line
'''
#%%
def GetDataRaw(): # Get Raw Data.
    with open("Day8Data.txt") as f:
        DataRaw = f.read()
    return DataRaw

def GetData(DataRaw): # Pre-process Raw Data.
    Data = DataRaw.split("\n")
    return Data

def ReadCodePart1(Line = 0):
        ExecutedInstrLine = []
        ThisLine = Line
        ThisInstr = InstructionSet[ThisLine]
        Acc = 0

        while ThisLine not in ExecutedInstrLine:
            ExecutedInstrLine.append(ThisLine)
            Operation,Magnitude = ThisInstr.split(" ")
            if Operation == "nop":
                ThisLine +=1
            elif Operation == "acc":
                ThisLine +=1
                Acc += int(Magnitude)
            elif Operation == "jmp":
                ThisLine += int(Magnitude)
            else:
                print("Error: Invalid Operation")
                break

            ThisInstr = InstructionSet[ThisLine]

        return Acc

def ReadCodePart2(Line = 0):
    ExecutedInstrLine = []
    ThisLine = Line
    ThisInstr = InstructionSet[ThisLine]
    Acc = 0
    
    while ThisLine not in ExecutedInstrLine: # Infinte Loop Blocker
        ExecutedInstrLine.append(ThisLine)
        Operation,Magnitude = ThisInstr.split(" ")
        if Operation == "nop":
            ThisLine +=1
        elif Operation == "acc":
            ThisLine +=1
            Acc += int(Magnitude)
        elif Operation == "jmp":
            ThisLine += int(Magnitude)
        else:
            print("Error: Invalid Operation")
            break
        if ThisLine >= len(InstructionSet): # End of file successful break condition.
            return Acc
        ThisInstr = InstructionSet[ThisLine]
    return 0

if __name__ == "__main__":
    
    DataRaw = GetDataRaw()
    InstructionSet = GetData(DataRaw)

    Part = 2
    if Part == 1:
        print(ReadCodePart1())
    elif Part == 2:
        Acc = 0
        OrigInstructionSet = list(InstructionSet)
        for idx,ThisInstr in enumerate(InstructionSet): # For every instruction in the set
            Operation,Magnitude = ThisInstr.split(" ")
            if Operation == "jmp":
                InstructionSet[idx] = ThisInstr.replace("jmp","nop",1)
            if Operation == "nop":
                InstructionSet[idx] = ThisInstr.replace("nop","jmp",1)
            Acc = ReadCodePart2()
            if Acc > 0:
                print(Acc)
                break
            InstructionSet = list(OrigInstructionSet)
print("Done")