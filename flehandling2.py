import csv 
with open("eabc.csv", mode="a") as file:
    writer = csv.writer(file)
    # Adding a new row to the CSV file
    writer.writerow([4, "Bob Brown", 24, 15, 16])
    print("New row added successfully.")
# Reading the CSV file
with open("eabc.csv", mode="r") as file:
    reader = csv.reader(file)
    # Printing the contents of the CSV file
    for row in reader:
        print(row)