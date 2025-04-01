import csv 
with open("sadf.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Printing the contents of the CSV file
    for row in reader:
        print(row)
        # Convert the row to a dictionary
        student_dict = {
            "rollno": row[0],
            "name": row[1],
            "m1": int(row[2]),
            "m2": int(row[3]),
            "m3": int(row[4])
        }
        # Calculate total marks
        total_marks = int(row[2]) + int(row[3]) + int(row[4])
        student_dict["total"] = total_marks
        # Display the dictionary data
        print(student_dict)
        # Display the total marks
        print("Total Marks:", total_marks)
        print("\n")
