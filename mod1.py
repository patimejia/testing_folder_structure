import csv

# Load the data from samples1.csv
with open("input/samples1.csv") as f:
    reader = csv.reader(f)
    next(reader)  # skip the header row
    data = [[float(cell) for cell in row[2:]] for row in reader]

# Print the sum of each column
print(f"pH: {sum(row[0] for row in data)}")
print(f"Nitrogen: {sum(row[1] for row in data)}")
print(f"Phosphorus: {sum(row[2] for row in data)}")
print(f"Potassium: {sum(row[3] for row in data)}")

# Load the data from samples2.csv
with open("input/samples2.csv") as f:
    reader = csv.reader(f)
    next(reader)  # skip the header row
    data = [[float(cell) for cell in row[2:]] for row in reader]

# Print the sum of each column
print(f"pH: {sum(row[0] for row in data)}")
print(f"Nitrogen: {sum(row[1] for row in data)}")
print(f"Phosphorus: {sum(row[2] for row in data)}")
print(f"Potassium: {sum(row[3] for row in data)}")
