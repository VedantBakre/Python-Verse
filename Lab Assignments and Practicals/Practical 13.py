# 13 Write a Python program to concatenate two strings in a third string. Do not use +operator.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Using string formatting
str3 = "%s%s" % (str1, str2)

print("Concatenated string:", str3)
