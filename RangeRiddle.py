# Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i in range(len(days_of_week)):
    if i % 2 == 0:
        print("=" * 50,"\n")
        print(i, "=", days_of_week[i],"\n")