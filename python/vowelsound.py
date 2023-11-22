word = input()
word= word.lower().replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
li=[i for i in word]
print('.'+'.'.join(li))