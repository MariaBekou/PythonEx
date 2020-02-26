inf= input('Open the file you want')
print(inf)
with open(inf,'r') as file:
    script = file.read()
i=0
j=0
for word in script:
    for cnt in word:
        i+=1
        if cnt=="f" or cnt=="c" or cnt=="k" or cnt=="r" :
            i+=1
        else:
            j+=1
        if cnt.isspace() or cnt=="," or cnt==' '' '' ' or cnt==".":
            if i>j:
                print('This word is bad!')
            else:
                print('This word is good!')
            i=0
            j=0
        
file.close()

        
               
            
