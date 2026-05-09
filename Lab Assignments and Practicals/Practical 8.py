# 8 Write a Python program that has a dictionary of your friend’s name (as keys) and their birthdays. Print the items in the dictionary in a sorted order. Prompt the user to enter a name and check if it is present in the dictionary. If the name does not exist, then ask the user to enter Date of Birth. Add the details in the dictionary.

birthdays = {
    "Alice": "2000-01-15",
    "Charlie": "2001-08-10",
    "Bob": "1999-05-20"
}

print("Current birthdays (sorted):")
for name in sorted(birthdays.keys()):
    print(name, ":", birthdays[name])
    
name_to_check = input("\nEnter a friend's name: ")

if name_to_check in birthdays:
    print(name_to_check, "'s birthday is", birthdays[name_to_check])
else:
    dob = input("Name not found. Enter Date of Birth: ")
    birthdays[name_to_check] = dob
    print("Added details to dictionary.")
    
    print("\nUpdated birthdays (sorted):")
    for name in sorted(birthdays.keys()):
        print(name, ":", birthdays[name])
