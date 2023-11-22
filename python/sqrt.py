import math
cnt_number= int(input())
numbers=[]
for i in range(cnt_number):
    number= int(input())
    numbers.append(number)
    
for item in numbers:
    print('{:.8f}'.format(math.sqrt(item))[:-4])
    
    
