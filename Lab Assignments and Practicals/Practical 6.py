# 6 Write a Python program for creating a list of first ten letters of the alphabet, then using the slice operation do the following operations
# a. Print the first three letters from the list
# b. Print any three letters from the middle
# c. Print the letters from any particular index to the end of the list.

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print("Original list:", alphabet_list)

# a. Print the first three letters
print("a. First three letters:", alphabet_list[:3])

# b. Print any three letters from the middle
print("b. Three letters from middle:", alphabet_list[3:6])

# c. Print the letters from any particular index to the end
print("c. Letters from index 5 to end:", alphabet_list[5:])
