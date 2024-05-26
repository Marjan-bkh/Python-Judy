def check_string(string):
    index_ab = string.find("AB")
    # print(index_ab)
    if index_ab != -1:
        string= string[:index_ab] + string[index_ab + 2:]
    index_ba = string.find("BA")
    # print(index_ba)
    if index_ba !=-1:
         return 'YES'
    else:
        return 'NO'
 

# string = input()
# print(check_string(string))
