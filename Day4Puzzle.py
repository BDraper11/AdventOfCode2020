#%%
import re

class IDDoc:
    def __init__(self, block,ExtdValidityChecksOn = 0):
        block = block.split()

        def GetEntry(self,block,SearchString):
            for entry in block:
                if entry.find(SearchString)!=-1:
                    EntryReturn = entry.split(":")[1]
                    break
                else:
                    EntryReturn = None
            return EntryReturn
        def GetBirthYear(self, block):
            BirthYear = GetEntry(self,block,"byr")
            if ExtdValidityChecksOn:
                r = re.compile('\d{4}')
                if BirthYear == None:
                    return None
                elif r.match(BirthYear) is None:
                    return None
                elif int(BirthYear)>=1920 and int(BirthYear)<=2002:
                    return BirthYear
                else:
                    return None
            else:
                return BirthYear
        def GetIssueYear(self, block):
            IssueYear = GetEntry(self,block,"iyr")
            if ExtdValidityChecksOn:
                r = re.compile('\d{4}')
                if IssueYear == None:
                    return None
                elif r.match(IssueYear) is None:
                    return None
                elif int(IssueYear)>=2010 and int(IssueYear)<=2020:
                    return IssueYear
                else:
                    return None
            else:
                return IssueYear
        def GetExpiryYear(self, block):
            ExpiryYear = GetEntry(self,block,"eyr")
            if ExtdValidityChecksOn:
                r = re.compile('\d{4}')
                if ExpiryYear == None:
                    return None
                elif r.match(ExpiryYear) is None:
                    return None
                elif int(ExpiryYear)>=2020 and int(ExpiryYear)<=2030:
                    return ExpiryYear
                else:
                    return None
            else:
                return ExpiryYear
        def GetHeight(self, block):
            Height = GetEntry(self,block,"hgt")
            if ExtdValidityChecksOn:
                r = re.compile('\d+\w{2}')
                if Height == None:
                    return None
                elif r.match(Height) is None:
                    return None
                elif r.match(Height) is not None:
                    if Height.find("cm")!=-1:
                        ThresLow = 150
                        ThresHigh = 193
                        Height = Height[:-2]
                    elif Height.find("in")!=-1:
                        ThresLow = 59
                        ThresHigh = 76
                        Height = Height[:-2]
                    else:
                        return None
                    if int(Height)>=ThresLow and int(Height)<=ThresHigh:
                        return Height
                    else:
                        return None
                else:
                    return None
            else:
                return Height
        def GetHairColour(self, block):
            HairColour = GetEntry(self,block,"hcl")
            if ExtdValidityChecksOn:
                r = re.compile('#\w{6}')
                if HairColour == None:
                    return None
                elif r.match(HairColour) is None:
                    return None
                else:
                    return HairColour
            else:
                return HairColour
        def GetEyeColour(self, block):
            EyeColour = GetEntry(self,block,"ecl")
            if ExtdValidityChecksOn:
                PassList = ['amb','blu','brn','gry','grn','hzl','oth']
                if EyeColour == None:
                    return None
                elif EyeColour not in PassList:
                    return None
                else:
                    return EyeColour
            else:
                return EyeColour
        def GetPassportID(self, block):
            PassportID = GetEntry(self,block,"pid")
            if ExtdValidityChecksOn:
                r = re.compile('\d{9}')
                if PassportID == None:
                    return None
                elif r.match(PassportID) is None:
                    return None
                elif len(PassportID) != 9:
                    return None
                else:
                    return PassportID
            else:
                return PassportID
        def GetCountryID(self, block):
            CountryID = GetEntry(self,block,"cid")
            return CountryID
        def GetValidIDDocStatus(self):
            ValidStatus = 1
            for attribute, value in self.__dict__.items():
                #print(attribute,value)
                if attribute != "CountryID":
                    if value == None:
                        return 0
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
        IDDocs.append(IDDoc(block,1))
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
