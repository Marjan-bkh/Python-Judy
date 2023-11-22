# def check_string(string):
#     if "AB" in string and "BA" in string:
#         if abs(string.index("AB")- string.index("BA")) >1:
#             return'YES'
#     return 'NO'

# string= input()

# print(check_string(string))


def check_string(string):
    index_ab = string.find("AB")
    print(index_ab)
    index_ba = string.find("BA")
    print(index_ba)
    if index_ab != -1 and index_ba != -1 and abs(index_ab - index_ba) > 1:
        return 'YES'
    return 'NO'

string = input()
print(check_string(string))

# def check_string(string):
#     index_ab = string.find("AB")
#     index_ba = string.find("BA")
#     while index_ab != -1 and index_ba != -1:
#         if abs(index_ab - index_ba) > 1:
#             return 'YES'
#         if index_ab < index_ba:
#             index_ab = string.find("AB", index_ab + 2)
#         else:
#             index_ba = string.find("BA", index_ba + 2)
#     return 'NO'

# string = input()
# print(check_string(string))