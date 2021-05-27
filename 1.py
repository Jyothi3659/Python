str="This is an Umbrella"
words=str.split()
smallest=min(words, key=len)
largest=max(words, key=len)
print("smallest word is-", smallest)
print("largest word is-", largest)