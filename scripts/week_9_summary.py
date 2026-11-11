import csv

def read_rows(file_name):
    with open(file_name, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def clean_values(rows, column):
    values = []

    for row in rows:
        raw = row[column].strip()

        if raw == "":
            continue

        values.append(float(raw))

    return values


def summarise_values(values):
    if len(values) == 0:
        return {
            "count": 0,
            "smallest": None,
            "largest": None,
            "average": None
        }

    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values)
    }


def summarise_all(file_name, columns):
    rows = read_rows(file_name)
    report = {}

    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise_values(values)

    return report


file_name = "paved_roads.csv"
columns = ["length", "speed_estimate"]

report = summarise_all(file_name, columns)

for column, stats in report.items():
    print(
        f"{column}: "
        f"count={stats['count']}, "
        f"smallest={stats['smallest']}, "
        f"largest={stats['largest']}, "
        f"average={stats['average']}"
    )

# week 8 code re-written
# def inspect_column(filename, column):
#     with open(filename, encoding="utf-8-sig") as f:
#         rows = list(csv.DictReader(f))

#     values = []
#     skipped = 0
#     for row in rows:
#         raw = row[column].strip().replace(",", "")
#         if raw == "" or raw.upper() == "NA":
#             skipped += 1
#             continue
#         values.append(float(raw))

#     return {
#         "rows": len(rows),
#         "count": len(values),
#         "skipped": skipped,
#         "smallest": min(values),
#         "largest": max(values),
#         "average": sum(values) / len(values),
#     }

# print(inspect_column("paved_roads.csv", "speed_estimate"))
# print(inspect_column("paved_roads.csv", "length"))