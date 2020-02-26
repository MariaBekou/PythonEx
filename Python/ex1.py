inf= input('Open the file you want')
print(inf)
with open(inf,'r') as file:
    text = file.read()
spltxt = text.split()
letters=[]
for word in spltxt:
    letters.sort(reverse=True)

def rem_vowel(string): 
    vowels = ('a', 'e', 'i', 'o', 'u')  
    for x in string.lower(): 
        if x in vowels: 
            string = string.replace(x, "") 

def reverse(string): 
    string = string[::-1] 

lista=[]
for i in range(5):
    lista.append(reverse(spltxt[i]))

for i in lista:
    print(rem_vowel(i))    

file.close()