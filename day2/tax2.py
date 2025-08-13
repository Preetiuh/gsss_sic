Level2:
Level 2: Taxable Income Calculation
Objective: Calculate taxable income after standard deductions.
Tasks:
• Deduct a Standard Deduction of ₹50,000 from the annual gross salary.
• Compute the Taxable Income and display all intermediate calculations.
Output: Display gross salary, standard deduction and taxable income.

import tax1 as t1

standard_deduction = 50000  # ₹50,000 deduction

taxable_income = t1.annual_salary - standard_deduction

print("Standard Deduction:", standard_deduction)
print("Taxable Income:", taxable_income)
