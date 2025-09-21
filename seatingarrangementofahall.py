"""
Assignment: Seating Arrangement in a Hall
Author:Chat gpt
Date: YYYY-MM-DD

Concepts Covered:
- Input and Output
- Strings
- Arithmetic operators (+, -, *, /, //, %)
- if-else statements
- for loops
- Factorial calculation
"""

import math

# ------------------------------
# Function to calculate factorial
# ------------------------------
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

"ഫോർ ലൂപ്പ് ഫാക്ടറിൽ ഇൽ "
# ------------------------------
# Main program
# ------------------------------
print("=== Seating Arrangement Program ===")
#ഒരു സ്ട്രിംഗ് പ്രിന്റ് ചെയ്യുന്ന വിധം 

# Input: Hall shape
shape = input("Enter hall shape (rectangle/circle/triangle): ").lower()
#ഇന്പുട് ചെയ്യുന്ന വിധം വാരിയബിൾ അസിഗ്നേമെന്റ് 
# Input: Hall dimensions based on shape
#ഇഫ് എൽസ് 
if shape == "rectangle":
    length = float(input("Enter length of hall (in feet): "))
    breadth = float(input("Enter breadth of hall (in feet): "))
    area = length * breadth
#FLOAT .. ദശാംശ സംഖ്യ കൂടി ഉൾപെടുത്താൻ 
##ഗുണന ക്രിയ 
elif shape == "circle":
    radius = float(input("Enter radius of hall (in feet): "))
    area = math.pi * radius * radius
    #പൈ ആർ സ്‌ക്വയർ 

elif shape == "triangle":
    base = float(input("Enter base of hall (in feet): "))
    height = float(input("Enter height of hall (in feet): "))
    area = 0.5 * base * height

else:
    print("Invalid shape entered. Exiting...")
    exit()
#ഇന്പുട് ERROR  ട്രാപ്പിങ് 
print(f"\nTotal hall area = {area:.2f} sq.ft")

# Input: area occupied by a single chair
chair_area = float(input("Enter area occupied by a single chair (in sq.ft): "))

# Calculate number of chairs that can fit
chairs_fit = int(area // chair_area)   # floor division
leftover_area = area % chair_area      
#മോഡുലസ് 
print(f"\nTotal chairs that can be arranged: {chairs_fit}")
print(f"Leftover area after arrangement: {leftover_area:.2f} sq.ft")

# ------------------------------
# Seating arrangement (with patterns)
# ------------------------------
print("\n--- Seating Arrangement Pattern ---")
#ഇതൊന്നും പഠിച്ചിട്ടല്ല 
if shape == "rectangle":
    # Arrange in nearly square rows/columns
    rows = int(math.sqrt(chairs_fit))
    cols = chairs_fit // rows
    print(f"\nRectangle Pattern ({rows} rows × {cols} columns):\n")
    count = 0
    for i in range(rows):
        for j in range(cols):
            print("🪑", end=" ") #ഒരു സിംബൽ പ്രിന്റ് ചെയ്യുന്ന വിധം 
            count += 1
        print()
    if chairs_fit % rows != 0:
        print("Remaining chairs:", (chairs_fit % rows))

elif shape == "circle":
    # Simple circular pattern (approximate using rows of chairs)
    print(f"\nCircle Pattern (approx {chairs_fit} chairs):\n")
    radius = int(math.sqrt(chairs_fit)) // 2
    for i in range(-radius, radius+1):
        for j in range(-radius, radius+1):
            if i*i + j*j <= radius*radius:
                print("🪑", end=" ")
            else:
                print("  ", end=" ")
        print()

elif shape == "triangle":
    # Triangular arrangement: rows with 1,2,3...
    n = 0
    total = 0
    while total + (n+1) <= chairs_fit:
        n += 1
        total += n
    print(f"\nTriangle Pattern ({n} full rows):\n")
    used = 0
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        for j in range(i):
            print("🪑 ", end="")
            used += 1
        print()
    if chairs_fit > total:
        print("Remaining chairs:", "🪑 " * (chairs_fit - total))

# ------------------------------
# Example factorial use
# ------------------------------
num = int(input("\nEnter a number to find its factorial (demo): "))
print(f"Factorial of {num} = {factorial(num)}")

print("\n=== Program Completed ===")
