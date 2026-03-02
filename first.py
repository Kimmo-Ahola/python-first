# # x = "Kimmo"

# # print(x)

# # yTest_test123 = "Kimmo"
# # age = 34

# # print("Namnet är: ", yTest_test123, "Åldern är: ", age)
# # x = 12

# # name = "Kimmo"
# # age = 34

# # z = name + "Ahola"

# # x_2 = 1 # integer
# # x_3 = 1.0 # float
# # boolean = True # boolean, False fungerar också

# # result = x_2 + x_3
# # print(result + boolean)
# # # kommentar
# # null = None

# # print(null)

# """
# kommentar
# på
# flera
# rader
# """

# name = "kimmo"
# age = 34

# f_string = f"{name} {(age+1)//2}"
# print(3**6)

# class Person(): # tabell? ORM -> omvandlar klasser till tabeller
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def print(self):
#         print(f"Namnet är: {self.name}. Åldern är: {self.age}")

# kimmo = Person("Kimmo", 34)

# # kimmo.print()

# my_string = "kimmo ahola"
# my_string = my_string.title()

# # print(my_string)

# # Jag vill ha små bokstäver igen
# my_string = my_string.lower()

# my_number = 1

# # Expressions

# expression = (5+4) > 3
# # print(expression)

# # Jämförelseoperatorer

# # Equals to skrivs ==

# # print("apple" > "Apple")

# # truthy = "typ sant"
# if 5: # True = 1, False = 0
#     print("5 is larger than 4?")
#     print("")
#     if 5 > 4:
#         print("")
# elif 5 > 4:
#     print("5 is larger than 4!!!!!")

x = "kimmo"


def my_capitalize(my_string):
    x = my_string.upper()
    print("In my function", x)
    return x


x = my_capitalize(x)  # x = my_string
print(x)
