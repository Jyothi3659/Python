#find the occurence after first "," and last ","
str= "hello,Good,Morning.World"
print(str[str.find(','):])
print(str[str.rfind(','):])