import csv

with open("paved_roads.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    
print("Number of rows:", len(rows))
print("Number of columns:", len(rows[0]))
print("Column names:", list(rows[0].keys()))

#Inspecting numerical columns
# values = []
# skipped = []

# for row in rows:
#     value = float(row["speed_estimate"].strip())
#     values.append(value)
    
# print("Largest values: ", max(values))
# print("Smallest values: ", min(values))
# print("Count: ", len(values))


# #Handling missing values in the practical
values1 = []
skipped1 = []

for row in rows:
    raw = row["length"].strip()

    if raw == "":
        skipped1.append(row)
        continue

    raw = raw.replace(",", "")

    values1.append(float(raw))

print("Processed values:", values1)
print("Skipped records:", skipped1)

print("Largest value:", max(values1))
print("Smallest value:", min(values1))
print("Count:", len(values1))

#Alternative code to handle missing values
def inspect_column(filename, column):
    with open("paved_roads.csv", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    values = []
    skipped = 0
    for row in rows:
        raw = row["length"].strip().replace(",", "")
        if raw == "" or raw.upper() == "NA":
            skipped += 1
            continue
        values.append(float(raw))

    return {
        "rows": len(rows),
        "columns": list(rows[0].keys()),
        "count": len(values),
        "skipped": skipped,
        "smallest": min(values),
        "largest": max(values),
    }

print(inspect_column("paved_roads.csv", "speed_estimate"))
print(inspect_column("paved_roads.csv", "length_m"))
