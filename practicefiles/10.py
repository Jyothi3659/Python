#deleting consonants froom the string
str= "Hello, have a good day"
newstr= str.casefold()
consonants= "bcdfghjklmpqrstvwxyz"
for char in newstr:
   if char in consonants:
      newstr= newstr.replace(char,"")
print(newstr)


