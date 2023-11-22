max_num = float('-inf')
sec_num = float('-inf')
num = int(input())

while num != -1:
    if num> max_num:
        sec_num = max_num
        max_num= num
    elif num> sec_num:
        sec_num =num
    num = int(input())

print(str(max_num) +' '+str(sec_num))