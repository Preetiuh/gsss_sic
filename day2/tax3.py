import tax2 as t2

tax = 0

if t2.taxable_income > 300000:
    tax += (min(t2.taxable_income, 600000) - 300000) * 0.05

if t2.taxable_income > 600000:
    tax += (min(t2.taxable_income, 900000) - 600000) * 0.10

if t2.taxable_income > 900000:
    tax += (min(t2.taxable_income, 1200000) - 900000) * 0.15

if t2.taxable_income > 1200000:
    tax += (min(t2.taxable_income, 1500000) - 1200000) * 0.20

if t2.taxable_income > 1500000:
    tax += (t2.taxable_income - 1500000) * 0.30


if t2.taxable_income <= 700000:
    tax = 0

cess = tax * 0.04
total_tax = tax + cess

print("\n--- Tax Calculation ---")
if t2.taxable_income <= 700000:
    print("Total tax amount: ₹0")
else:
    print("Tax:", tax)
    print("Cess (4%):", cess)
    print("Total Tax Payable:", total_tax)
