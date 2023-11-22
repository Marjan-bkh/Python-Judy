cnt= int(input())
dic={}
for i in range(cnt):
    word, meaning= input().split()
    dic[word]= meaning
sentence= input()    
sentence_list= sentence.split()
translate_list=[]
for item in sentence_list:
    if item in dic.keys():
        translate_list.append(dic[item])
    else:
        translate_list.append(item)
print(' '.join(translate_list))

# print(sentence_translate)