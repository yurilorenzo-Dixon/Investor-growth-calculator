git init
git add .
git commit -m "Initial commit - investment calculator"
git branch -M main
git remote add origin https://github.com/your-username/investment-calculator.git
git push -u origin main


principal = 1000
rate = 0.07

print("Investment Growth Over 30 Years")
print("--------------------------------")

for year in range(1, 31):
    
    amount = principal * (1 + rate) ** year
    
    print(f"Year {year}: ${amount:,.2f}")

amount_10 = principal * (1 + rate) ** 10
amount_20 = principal * (1 + rate) ** 20
amount_30 = principal * (1 + rate) ** 30

print("\nSummary:")
print(f"After 10 years: ${amount_10:,.2f}")
print(f"After 20 years: ${amount_20:,.2f}")
print(f"After 30 years: ${amount_30:,.2f}")
