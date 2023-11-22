def check_string(string):
    if "AB" in string and "BA" in string:
        if abs(string.index("AB")- string.index("BA")) >1:
            return'YES'
    return 'NO'

string= input()

print(check_string(string))

# import re
# string = input().upper()
# substring_1 = 'AB'
# substring_2 = 'BA'
# print(re.search(substring_1,string))
# print( re.search(substring_2,string))

# if re.search(substring_1,string) and re.search(substring_2,string):
#     print('YES')
# else:
#     print('NO')s
