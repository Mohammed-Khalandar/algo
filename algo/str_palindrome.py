def isPalindrome(String):
    rev_str = String[::-1]
    if String == rev_str:
        return True
    else:
        return False

print(isPalindrome('abcdcba'))
print(isPalindrome('a'))
print(isPalindrome('ab'))
print(isPalindrome('aba'))
print(isPalindrome('abb'))
print(isPalindrome('abba'))
print(isPalindrome('abcdefghhgfedcba'))
print(isPalindrome('abcdefghihgfedcba'))
print(isPalindrome('abcdefghihgfeddcba'))