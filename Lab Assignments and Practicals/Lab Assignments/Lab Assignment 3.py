# 3 Write Program in Python to calculate the salary of an employee given his Basic Pay. Let DA be 80% of Basic Pay, HRA be 10 % of basicpay and TA be 5% of basic pay. Calculate gross salary of employee. Professional tax is to be deducted from gross salary as 2% of gross salary. Calculate salary payable after deductions.

basic_pay = float(input("Enter Basic Pay: "))

da = 0.80 * basic_pay
hra = 0.10 * basic_pay
ta = 0.05 * basic_pay

gross_salary = basic_pay + da + hra + ta
print("Gross Salary:", gross_salary)

professional_tax = 0.02 * gross_salary
print("Professional Tax Deducted:", professional_tax)

salary_payable = gross_salary - professional_tax
print("Salary Payable:", salary_payable)
