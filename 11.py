#print evey char of a string in new line using loop
#str= "python"
#newstr= str.upper()
#for char in newstr:
    #print(char)


#len of string refrigerator using len function
#str1= "Refrigerator"
#length= len("Refrigerator")
#print(length)


#check if word orange is present in string "this is orange juice"
str2= "this is orange juice"
newstr2= str2.split()
for char in newstr2:
    if 'orange' in char:
        print("Yes, 'orange' is present in given string")


#find the first and last occurrence of letter 'o' and  character ',' in string "hello,world"
str= "hello,world"
print("Occurrence of first 'o' is", str.find("o"))
print("Occurrence of last 'o' is", str.rfind("o"))
print("Occurrence of char ',' is", str.find(","))