# Calculate income tax for the given income by adhering rules

# pseudocode

# Define the function to calculate the income tax
def calculate_income_tax(income):
    if income <=10000:
        tax=0
    elif income <=20000:
        tax=(income-10000)*0.1
    else:
        tax=10000*0.1+(income-20000)*0.2
        return tax

# Print the calculated income tax
income=float(input("How much is your incoome?\n Enter your income: "))
tax_due=calculate_income_tax(income)
print (f"Your income tax is {tax_due}0")