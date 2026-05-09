# 12 Write a Python program that accept string from user and perform following operations i. Check palindrome ii. Check substring

user_string = input("Enter a string: ")

# i. Check palindrome
rev_string = ""
for i in range(len(user_string)-1, -1, -1):
    rev_string += user_string[i]

if user_string == rev_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
# ii. Check substring
sub_str = input("Enter a substring to check: ")
if sub_str in user_string:
    print("Substring is present in the string.")
else:
    print("Substring is not present.")
