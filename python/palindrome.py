word = input()
if(word.lower()[::-1]) == word.lower():
    print("palindrome")
else:
    print("not palindrome")
