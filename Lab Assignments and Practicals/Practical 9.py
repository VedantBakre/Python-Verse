# 9 Write program in Python to accept integer between 1 and 12 to represent the month number and function to display corresponding month in words.

def display_month(m):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    if 1 <= m <= 12:
        print("The month is", months[m-1])
    else:
        print("Invalid month number.")

month_num = int(input("Enter a month number (1-12): "))
display_month(month_num)
