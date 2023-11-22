word= input()
len_word= len(word)
cnt_upper=0
for char in word:
    if char.isupper():
        cnt_upper +=1

if cnt_upper > len_word//2:
    print(word.upper())
else:
    print(word.lower())

