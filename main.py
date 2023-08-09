# Initialize a list to store employee information
employee_info = []

# Get the number of employees
num_employees = int(input("Enter the number of employees: "))

# Input employee data and calculate their earnings
for i in range(num_employees):
    print(f"\nEmployee {i + 1}")
    employee_name = input("Enter employee name: ")
    working_hours = float(input("Enter the number of working hours: "))
    hourly_rate = float(input("Enter the hourly rate: "))

    # Calculate the income
    income = working_hours * hourly_rate

    # Calculate income tax
    tax_deduction = income * 0.2

    # Calculate superannuation deduction
    superannuation_deduction = income * 0.1

    # Store employee information in the list
    employee_info.append([employee_name, income, tax_deduction, superannuation_deduction])

# Print the table header
print("\nEmployee Name | Income | Income Tax Deduction | Superannuation")
print("-" * 65)

for emp in employee_info:
    employee_name, income, tax_deduction, superannuation_deduction = emp
    print("{:<15} ${:<10.2f} ${:<20.2f} ${:<15.2f}".format(employee_name, income, tax_deduction, superannuation_deduction))
#make some changes
