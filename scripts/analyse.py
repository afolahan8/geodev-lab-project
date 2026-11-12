
# Step 1: Open and read the CSV file
with open("states.csv") as f:
    lines = f.readlines()

# Step 2: Print the number of lines
print("Number of lines:", len(lines))

print("\nSTATE AREA ANALYSIS")
print("-------------------")

# Step 3: Loop through the data, skipping the header
for line in lines[1:]:

    # Step 4: Remove whitespace and split the row
    parts = line.strip().split(",")

    # Step 5: Extract the state name and area
    state = parts[0].strip()
    area_km2 = float(parts[-1].strip())

    # Step 6: Convert square kilometres to hectares
    area_ha = area_km2 * 100

    # Step 7: Classify the state
    if area_km2 > 9:
        size = "Large"
    else:
        size = "Small"

    # Step 8: Display the results
    print(
        f"{state}: {area_km2:.1f} km², "
        f"{area_ha:.1f} hectares, "
        f"Classification: {size}"
    )
