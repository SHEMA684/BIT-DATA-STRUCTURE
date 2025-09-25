import array

# Project 101: Software License Tracker

# Step 1: Integers
licenses = [12, 8, 15, 6, 10]   # Example license counts per department
total = sum(licenses)
average = total / len(licenses)
minimum = min(licenses)
maximum = max(licenses)

print("=== Integer Calculations ===")
print(f"Total Licenses: {total}")
print(f"Average Licenses: {average:.2f}")
print(f"Minimum Licenses: {minimum}")
print(f"Maximum Licenses: {maximum}\n")

# Step 2: Strings (reports with f-strings)
report = f"Software License Tracker Report\nTotal: {total}, Average: {average:.2f}, Min: {minimum}, Max: {maximum}"
summary = f"We are tracking {len(licenses)} departments with an average of {average:.1f} licenses."
print("=== String Reports ===")
print(report)
print(summary, "\n")

# Step 3: Booleans (threshold + compound condition)
threshold = 9
if average > threshold and maximum > 12:
    status = "Above Standard"
else:
    status = "Below Standard"

print("=== Boolean Check ===")
print(f"Status: {status}\n")

# Step 4: Lists
license_list = licenses.copy()
print("=== List Operations ===")
print("Original list:", license_list)

# Add new element
license_list.append(14)
# Remove licenses less than 8
license_list = [x for x in license_list if x >= 8]
# Sort list
license_list.sort()
print("Modified list:", license_list, "\n")

# Step 5: Arrays
license_array = array.array('i', licenses)  # fixed-size numeric array
array_sum = sum(license_array)

print("=== Array Operations ===")
print("Array sum:", array_sum)
print("Compare with List sum:", sum(license_list), "\n")

# Step 6: Dictionaries
licenses_dict = [
    {"id": 1, "name": "HR", "value": 12},
    {"id": 2, "name": "Finance", "value": 8},
    {"id": 3, "name": "IT", "value": 15},
]

print("=== Dictionary Operations ===")
# Update one record (Finance value changed)
licenses_dict[1]["value"] = 11
# Delete one record (remove HR)
licenses_dict = [d for d in licenses_dict if d["id"] != 1]
# Compute total of 'value'
total_value = sum(d["value"] for d in licenses_dict)

print("Updated records:", licenses_dict)
print("Total of 'value' field:", total_value)