monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - total_monthly_expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are: {monthly_savings}")
print(f"Your projected savings afer one year, with interest) are: {projected_savings}")