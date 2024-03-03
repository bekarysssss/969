def is_palindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    
    return s == s[::-1]

x = input("")
if is_palindrome(x):
    print("Palindrome!")
else:
    print("Not palindrome!")