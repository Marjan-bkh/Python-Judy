# word= input()
# if word.find('hello') != -1:
#     print('YES')
# else:
#     print('NO')

import re

string = input()
substring = "h.*e.*l.*l.*o"

if re.search(substring, string):
    print("YES")
else:
    print("NO")