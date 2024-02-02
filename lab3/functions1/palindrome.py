def palindrome(s):
    str = ''.join(s.lower().split())
    return str == str[::-1]

input = "madam"
result = palindrome(input)

if result:
    print(f"Palindrome")
else:
    print(f"Not a palindrome")