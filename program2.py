import sys


if len(sys.argv) < 2:
    print("Error: Please provide salary as a command-line argument.")
    print("Usage: python salary_bonus.py <salary>")
    sys.exit(1)

salary = float(sys.argv[1])

bonus = salary * 0.10
total_salary = salary + bonus

print("Employee Salary :", salary)
print("Bonus (10%)     :", bonus)
print("Total Salary    :", total_salary)
