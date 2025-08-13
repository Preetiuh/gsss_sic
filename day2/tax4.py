Level 4: Net Salary Calculation
Objective: Calculate annual net salary after tax deductions.
Tasks:
1. Compute Net Salary = Annual Gross Salary - Total Tax Payable.
2. Display:
o Annual Gross Salary
o Total Tax Payable (including cess)
o Annual Net Salary

import tax3 as t3,tax1 as t1
net_salary = t1.annual_salary -t3.total_tax

print("\n--- Net Salary ---")
print("Annual Gross Salary:", t1.annual_salary)
print("Total Tax Payable:", t3.total_tax)
print("Annual Net Salary:", net_salary)
