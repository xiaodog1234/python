camel_case = input("camelCase: ")

for letter in camel_case:
    if letter.isupper():
        camel_case = camel_case.replace(letter, "_"+letter.lower())
print("snake_case: ", camel_case)
