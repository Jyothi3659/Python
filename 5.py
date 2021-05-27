str1 = input("enter first word:")
str2 = input("enter second word:")
if sorted(str1)==sorted(str2):
    print("the word is anagram")
else:
    print("the word is not anagram")