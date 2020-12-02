#%%
f = open("Day2Data.txt", "r")
lines = f.readlines()

validPWs = []

for line in lines:
    line = line.split(":")
    rule = line[0]
    payload = line[1].strip()
    character = rule.split(" ")[1]
    occurance = rule.split(" ")[0]
    occuranceLo = int(occurance.split("-")[0])
    occuranceHi = int(occurance.split("-")[1])

    if payload.count(character)<=occuranceHi and payload.count(character)>=occuranceLo:
        validPWs.append(payload)
print(len(validPWs))
# %%
f = open("Day2Data.txt", "r")
lines = f.readlines()

validPWs = []

for line in lines:
    line = line.split(":")
    rule = line[0]
    payload = line[1].strip()
    character = rule.split(" ")[1]
    occurance = rule.split(" ")[0]
    indexLo = int(occurance.split("-")[0])-1
    indexHi = int(occurance.split("-")[1])-1

    if bool(payload[indexLo]==character) ^ bool(payload[indexHi]==character):
        validPWs.append(payload)
print(len(validPWs))