#%%
class IDDoc:
    def __init__(self, block):
        block = block.split()

        def GetEntry(self,block,SearchString):
            for entry in block:
                if entry.find(SearchString)!=-1:
                    EntryReturn = entry.split(":")[1]
                    break
                else:
                    EntryReturn = ''
            return EntryReturn
        def GetBirthYear(self, block):
            BirthYear = GetEntry(self,block,"byr")
            return BirthYear
        def GetIssueYear(self, block):
            IssueYear = GetEntry(self,block,"iyr")
            return IssueYear
        def GetExpiryYear(self, block):
            ExpiryYear = GetEntry(self,block,"eyr")
            return ExpiryYear
        def GetHeight(self, block):
            Height = GetEntry(self,block,"hgt")
            return Height
        def GetHairColour(self, block):
            HairColour = GetEntry(self,block,"hcl")
            return HairColour
        def GetEyeColour(self, block):
            EyeColour = GetEntry(self,block,"ecl")
            return EyeColour
        def GetPassportID(self, block):
            PassportID = GetEntry(self,block,"pid")
            return PassportID
        def GetCountryID(self, block):
            CountryID = GetEntry(self,block,"cid")
            return CountryID
        def GetValidIDDocStatus(self):
            ValidStatus = 1
            for attribute, value in self.__dict__.items():
                #print(attribute,value)
                if attribute != "CountryID":
                    if value == '':
                        ValidStatus = 0
            return ValidStatus

        self.BirthYear = GetBirthYear(self, block)
        self.IssueYear = GetIssueYear(self, block)
        self.ExpiryYear = GetExpiryYear(self, block)
        self.Height = GetHeight(self, block)
        self.HairColour = GetHairColour(self, block)
        self.EyeColour = GetEyeColour(self, block)
        self.PassportID = GetPassportID(self, block)
        self.CountryID = GetCountryID(self, block)
        self.ValidIDDocStatus = GetValidIDDocStatus(self)

def GetBlocks():
    with open("Day4Data.txt") as f:
        lines = f.read()
        blocks = lines.split("\n\n")
    return blocks

def GetIDDocs(blocks):
    IDDocs = []
    for block in blocks:
        IDDocs.append(IDDoc(block))
    return IDDocs

def GetCountValidIDDocs(IDDocs):
    CountValidIDDocs = 0
    for IDDoc in IDDocs:
        if IDDoc.ValidIDDocStatus:
            CountValidIDDocs += 1
    return CountValidIDDocs


blocks = GetBlocks()
IDDocs = GetIDDocs(blocks)
print("Number of valid ID documents : ",GetCountValidIDDocs(IDDocs))
print("Done")


# %%
