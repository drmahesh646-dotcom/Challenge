# Input marks for 5 subjects
sub1 = float(input("Enter marks for Subject 1 (out of 100): "))
sub2 = float(input("Enter marks for Subject 2 (out of 100): "))
sub3 = float(input("Enter marks for Subject 3 (out of 100): "))
sub4 = float(input("Enter marks for Subject 4 (out of 100): "))
sub5 = float(input("Enter marks for Subject 5 (out of 100): "))

# Calculate total and percentage
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

# Assign grade based on percentage
if percentage < 40:
    grade = "Failed"
elif 40 <= percentage < 50:
    grade = "C+"
elif 50 <= percentage < 60:
    grade = "C"
elif 60 <= percentage < 70:
    grade = "B"
elif 70 <= percentage < 80:
    grade = "B+"
elif 80 <= percentage < 90:
    grade = "A"
elif 90 <= percentage <= 100:
    grade = "A+"
else:
    grade = "Invalid marks"

# Print results
print(f"\nTotal Marks: {total} / 500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
