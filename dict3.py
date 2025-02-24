

employees = {
    101: [(1, 50000), (2, 60000), (3, 55000)],
    102: [(4, 70000), (5, 75000), (6, 72000)],
    103: [(7, 40000), (8, 42000), (9, 41000)]
}

min_salary = {}
max_salary = {}

for dept, emp_list in employees.items():
    min_sal = emp_list[0][1]  
    max_sal = emp_list[0][1]

    for emp in emp_list:
        if emp[1] < min_sal:
            min_sal = emp[1]
        if emp[1] > max_sal:
            max_sal = emp[1]

    min_salary[dept] = min_sal
    max_salary[dept] = max_sal

print("Minimum salaries by department:", min_salary)
print("Maximum salaries by department:", max_salary)
