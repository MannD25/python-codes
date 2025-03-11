#Write a program that defines a function sum_avg() to accept marks of five subjects and calculates total and average. It should return directly both values.

def sum_avg(*marks):
    return sum(marks), sum(marks)/len(marks)

print(sum_avg(90, 80, 70, 60, 50))
