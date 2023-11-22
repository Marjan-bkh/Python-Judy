number = input()
reve_number = 0
if len(number) ==3:
    number = int(number)
    while number >0:
        reminder = number %10
        reve_number= reve_number*10 + reminder
        number = number //10
print (reve_number*2)