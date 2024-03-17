
name = input("Employee's name: ")
num_shifts = int(input("Number of Shifts: "))
num_transations = int(input("Number of transactions: "))
transaction_value = float(input("Transaction dollar value: "))

productivity_score = (transaction_value / num_transations)/num_shifts;
bonus = 50.0;

if productivity_score > 30 and productivity_score <= 69:
    bonus = 75.0
elif productivity_score > 70 and productivity_score <= 199: 
    bonus = 100.0
elif productivity_score > 199:
    bonus = 200.0

print(f"Employee Name: {name}")
print(f"Employee Bonus: ${bonus}")