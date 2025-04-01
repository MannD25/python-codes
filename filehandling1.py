import csv


data = [
    ["roll no ", "name", "cpmark","mathsII","Chemistry"],
    [1, "John Doe", 22,16,17],
    [2, "Jane Smith", 23, 18, 19],
    [3, "Alice Johnson", 21, 20, 22]
]

# File path
file_path = "eabc.csv"

# Writing to the CSV file
with open(file_path, mode="w") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file created successfully at {file_path}")