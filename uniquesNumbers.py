numbers = [1, 2, 2, 5, 1, 5, 3, 7, 8, 9]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
