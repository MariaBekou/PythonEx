inf= input('Open the file you want')
print(inf)
with open(inf,'r') as file:
    script = file.read()
splscr = script.split()
lgth = 3
for wrd in splscr:
    if len(wrd) > lgth:
        wrd = wrd[1:] + wrd[0:1] + "ay"
        print(wrd)

file.close()