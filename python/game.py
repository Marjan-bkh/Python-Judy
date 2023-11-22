import random
a=1
c=99
hads= int(random.randint(a,c))
print(hads)
javab= input()


while javab !='d':
    if javab == 'k':
        c = hads
        hads = int(random.randint(a,c))
        print(hads)
    elif javab == 'b' :
        a= hads
        hads = int(random.randint(a,c))
        print(hads)
    javab = input()
print('Wooooooo.You wiiiiiin!!!')

