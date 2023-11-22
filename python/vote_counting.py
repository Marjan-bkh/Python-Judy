import collections
cnt= int(input())
country_list=[]
for i in range(cnt):
    x= input()
    country_list.append(x)
    
dic={item:country_list.count(item) for item in country_list}
dic= collections.OrderedDict(sorted(dic.items()))
for key,value in dic.items():
    print (key + ' '+str(value))
