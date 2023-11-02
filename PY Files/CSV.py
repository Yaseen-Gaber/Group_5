'''
import csv
try:
    with open('D:\Personal\Yaseen\RIT (Rochester Institute of Technology)\Software Developement\PY Files\Comma Separated Values.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            print(line[0:3])
except Exception as e:
    print(f"An error occured: {e}")
'''

'''
while True:
    age = input("Enter your age: ")
    
    if age.isdigit() and 0 < int(age) <= 120:
        print(f"You entered a valid age: {age}")
        break
    else:
        print("Invalid age. Please enter a valid age between 1 and 120.")
'''

'''
import csv

def Print_GPA():
    try:
        with open('data.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  

            for row in reader:
                if len(row) >= 4:
                    student_id = row[0]
                    student_name = row[1]
                    student_lastname = row[2]
                    student_gpa = row[3]

                    print(f"Student ID: {student_id}")
                    print(f"Name: {student_name} {student_lastname}")
                    print(f"GPA: {student_gpa}\n")
                else:
                    print("Invalid row in data.csv")
    except FileNotFoundError:
        print("File 'data.csv' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

Print_GPA()
'''

'''
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

n = 4
print(f"Factorial of {n} (using recursion): {factorial_recursive(n)}")
'''

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

# Example usage:
base = 2
exponent = 3
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")