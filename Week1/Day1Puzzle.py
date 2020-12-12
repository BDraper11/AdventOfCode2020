#%%
tgt = 2020
f = open("Day1Data.txt", "r")
data = []
for line in f:
  data.append(int(line.strip('\n')))

for x in data:
  #print(x)
  if x != 1010:
    for y in data:
      if (x + y) == tgt:
        A = x
        B = y
        break

print(A)
print(B)
print(A+B)
print(A*B)

# %%
tgt = 2020
f = open("Day1Data.txt", "r")
data = []
for line in f:
  data.append(int(line.strip('\n')))

for x in data:
  for y in data:
    for z in data:
      if (x+y+z)==tgt:
        A=x
        B=y
        C=z
        break

print(A)
print(B)
print(C)
print(A+B+C)
print(A*B*C)
# %%
