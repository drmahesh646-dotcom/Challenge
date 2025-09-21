# Ayurvedic Sirodhara Oscillator Automation System

# Step 1: Read inputs
temp = float(input("Enter initial oil temperature (°C): "))
oil = int(input("Enter initial oil volume (ml): "))
duration = int(input("Enter treatment duration (minutes): "))

# Step 2: Validate inputs
if temp < 35 or temp > 45:
    print("Error: Temperature must be between 35°C and 45°C.")
    exit()
if oil < 100:
    print("Error: Oil volume must be at least 100 ml.")
    exit()
if duration < 10 or duration > 60:
    print("Error: Duration must be between 10 and 60 minutes.")
    exit()

print("\n--- Starting Sirodhara Treatment ---\n")

# Step 3: Simulate treatment
minutes_completed = 0
for minute in range(1, duration + 1):
    # Update values
    oil -= 5
    temp -= 0.2
    minutes_completed = minute

    # Print status
    print(f"Minute {minute}: Temp = {temp:.1f}°C, Oil = {oil}ml")

    # Step 4: Termination conditions
    if oil < 50:
        print("STOP: Insufficient oil!")
        break
    if temp < 35:
        print("STOP: Oil too cold!")
        break
else:
    print("Treatment completed successfully!")

# Step 5: Output summary
print("\n--- Treatment Summary ---")
print(f"- Minutes completed: {minutes_completed}")
print(f"- Final temperature: {temp:.1f}°C")
print(f"- Final oil volume: {oil}ml")
