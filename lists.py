# Lista är en behållare som innehåller flera saker

number = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    "Kimmo",
    "Ahola",
    None,
    True,
]  # kan stoppa in vad som helst

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(number)

number.append(11)
number.append(12)

number.insert(0, 0)

print(number)

print(number[1:10])

print(number)

counter = 0
while counter < len(number):
    print(number[counter])
    counter = counter + 1

for n in number:  # Pythonic
    print(n)

for index, n in enumerate(number):  # enumerate gives position for index
    if n % 2 == 0:
        print(f"pos: {index}, value: {n}")

print(number)
number.remove(2)
print(number)
