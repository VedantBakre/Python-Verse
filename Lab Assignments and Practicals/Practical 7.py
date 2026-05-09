# 7 Write a Python program to create a dictionary to store class test marks of 15 students. And print the highest and lowest score in a dictionary.

student_marks = {
    "Student1": 85, "Student2": 92, "Student3": 78, "Student4": 65, "Student5": 90,
    "Student6": 88, "Student7": 76, "Student8": 95, "Student9": 82, "Student10": 89,
    "Student11": 70, "Student12": 98, "Student13": 84, "Student14": 91, "Student15": 73
}

highest = max(student_marks.values())
lowest = min(student_marks.values())

print("Highest score:", highest)
print("Lowest score:", lowest)
