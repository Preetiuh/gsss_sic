#level-1

name = input("enter employee name: ")
emp_id = input("enter employee id: ")

basic_salary = float(input("enter basic monthly salary: "))
allowances = float(input("enter special allowances (monthly): "))
bonus_percent = float(input("enter annual bonus percentage: "))

gross_monthly_salary = basic_salary + allowances

base_annual_salary = gross_monthly_salary * 12

bonus_amount = (bonus_percent / 100) * base_annual_salary

annual_salary = base_annual_salary + bonus_amount

print("\n--- Salary Details ---")
print("Name:", name)
print("Employee ID:", emp_id)
print("Gross Monthly Salary:", gross_monthly_salary)
print("Base Annual Salary:", base_annual_salary)
print("Annual Bonus Amount:", bonus_amount)
print("Annual Salary (with bonus):", annual_salary)



