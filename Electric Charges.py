# Prompt user for input
kw_hours = int(input("Enter the KW hours used: "))

# Calculate the hours belonging to each tier
tier1_hours = min(kw_hours, 1000)
tier2_hours = max(0, kw_hours - 1000)

# Calculate total
amount_owed = (tier1_hours * 0.07633) + (tier2_hours * 0.09259)

# Display the output
print(f"Amount owed is ${amount_owed}")
