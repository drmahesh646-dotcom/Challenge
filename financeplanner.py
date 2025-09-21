"""
Assignment: Personal Expense Tracker with Budget Analysis
Author: Student Name
Date: YYYY-MM-DD
"""

# Step 1: Read Inputs
budget = float(input("Enter your monthly budget (in $): "))
if budget <= 0:
    print("Error: Budget must be a positive number.")
    exit()

num_categories = int(input("Enter number of expense categories (1-10): "))
if num_categories < 1 or num_categories > 10:
    print("Error: Number of categories must be between 1 and 10.")
    exit()

expenses = []
total = 0

# Step 2: Process each category
for i in range(1, num_categories + 1):
    print(f"\nCategory {i}:")
    name = input("  Name: ")
    amount = float(input("  Amount: "))
    if amount < 0:
        print("Error: Expense amount cannot be negative.")
        exit()
    total += amount
    percentage = (amount / budget) * 100
    # Spending level
    if percentage > 100:
        level = "Over"
    elif percentage >= 70:
        level = "High"
    elif percentage >= 30:
        level = "Moderate"
    else:
        level = "Low"
    expenses.append((name, amount, percentage, level))

# Step 3: Print category reports
print()
for name, amount, percentage, level in expenses:
    print(f"{name}: ${amount:.2f} ({percentage:.1f}% of budget) - {level}")

# Step 4: Budget summary
remaining = budget - total
if remaining > 0:
    status = "Surplus"
elif remaining == 0:
    status = "Balanced"
else:
    status = "Deficit"

print("\nBudget Summary:")
print(f"- Total Expenses: ${total:.2f}")
print(f"- Remaining Budget: ${remaining:.2f}")
print(f"- Status: {status}")

# Step 5: Recommendations
for name, _, perc, level in expenses:
    if level == "Over":
        print(f"Recommendation: Reduce spending in {name}")

if total > budget:
    print("Recommendation: Consider increasing your budget")
elif remaining > 0.2 * budget:
    print("Recommendation: You could allocate more to savings")
