#counting vowels and consonents in a string
str= input("enter a string:")
str.casefold()
vcount,ccount,dcount,scount= 0,0,0,0
vowels=["a","e",'i','o','u']
consonants= "bcdfghjklmnpqrstvwxyz"
digits= "0123456789"
spacechar= " "
for char in str:
    if char in vowels:
        vcount=vcount+1
    if char in consonants:
            ccount=ccount+1
    if char in digits:
                dcount=dcount+1
    elif char in spacechar:
                scount=scount+1
print("No,of vowels:",vcount)
print("No.of consonants:", ccount)
print("No.of digits:", dcount)
print("no.of space char:", scount)
