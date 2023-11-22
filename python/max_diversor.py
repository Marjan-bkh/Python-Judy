def diversor(number):
    cnt= 0
    for i in range(1,number+1):
        if number % i == 0:
            cnt = cnt +1
    return (cnt)


max_cnt = 0
number =0 
for i in range(20):
    input_number = int(input())
    cnt_diversor =diversor(input_number)
    if cnt_diversor >max_cnt:
        max_cnt = cnt_diversor
        number = input_number
    elif cnt_diversor == max_cnt:
        if input_number> number:
            number = input_number
       
        
print(str(number) +' '+ str(max_cnt))