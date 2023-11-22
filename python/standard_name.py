name_list=[]
for i in range(10):
    name= input()
    name_list.append(name)
a =[i.lower().capitalize() for i in name_list]   
print(*a,sep='\n')