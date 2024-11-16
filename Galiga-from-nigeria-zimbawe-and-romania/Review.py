'''
Palindrome number problem:

ex.
A palindrome is a word that's the same forwards as it is backwards.
racecar
racecar
anna
lol

Given an number x, return true if it is a palindrome, return false if not


ex. 121 -> return True

ex. -34 -> 43- => return False

ex. -343 -> 343- => return False


def isPalindrome(x):



hint: check if the reverse is the same as the normal x.
how to find the reverse

'''


def isPalindrome(x):
  new_string = str(x)
  reverse = ""

  for i in range(len(new_string) -1, -1, -1):
    
    reverse += new_string[i]

  if reverse == new_string:
    return True
  return False

print(isPalindrome(121))
print(isPalindrome(-345))
print(isPalindrome(-121))
print(isPalindrome(898989898989898989898989890))
print(isPalindrome(121212121212121212121212121212121))
print(isPalindrome("string"))
