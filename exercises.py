# Facit till övningarna

# Skapa funktioner för varje övning

temperature_1 = 26
temperature_2 = 15


def is_hot_or_cold(temperature_to_check):  # IsHotOrCold = PascalCase
    if temperature_to_check > 25:
        print("Hot")
    else:
        print("Cold")


is_hot_or_cold(temperature_1)
is_hot_or_cold(temperature_2)

# Övning 2

number_odd = 1
number_even = 2


def is_even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


is_even_or_odd(1)
is_even_or_odd(2)

# Övning 3

salary_1 = 50_001
salary_2 = 30_000
salary_3 = 10_000


def check_salary(salary_to_check):
    if salary_to_check > 50_000:
        print("High")
    elif salary_to_check >= 30_000 and salary_to_check < 50_000:
        print("Medium")
    else:
        print("Low")


check_salary(salary_1)
check_salary(salary_2)
check_salary(salary_3)

# Övning 4

age_1 = 17
is_student_1 = True

age_2 = 25
is_student_2 = False


def check_ticket_price(age, is_student):
    if age < 18:
        print("Child Ticket")
    elif age >= 18:  # and is_student == True
        if is_student == True:
            print("Student Discount")
        else:
            print("Full Price")
    else:
        print("Full Price")


check_ticket_price(age_1, is_student_1)
check_ticket_price(age_1, is_student_2)
check_ticket_price(age_2, is_student_1)
check_ticket_price(age_2, is_student_2)
