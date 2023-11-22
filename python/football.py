win = 0
equal= 0

for i in range(30):
    result = int(input())
    if result == 3:
        win = win+1
    elif result == 1:
        equal = equal+1
    

total= (win*3) + equal
print (str(total) + ' ' + str(win))


