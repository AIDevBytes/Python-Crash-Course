person_1 = {
    "first_name": "Alice",
    "last_name" : "Jones",
    "age" : 35,
    "email" : "alice@xyz.com"
}

print("################## Section 1 ########################")

print(f"Person 1: {person_1}")

print("\n")

print("################## Section 2 ########################")

person_2 = {
    "first_name": "Tim",
    "last_name" : "Smith",
    "age" : 21,
    "email" : "tim@xyz.com"
}

print(f"Person 2: {person_2['first_name']} {person_2['last_name']} is {person_2['age']} and email is {person_2['email']}")

print("\n")

person_2['first_name'] = "Alex"
person_2['last_name'] = "Price"
person_2['age'] = 50
person_2['email'] = "alex@xyz.com"

print(f"Person 2: {person_2['first_name']} {person_2['last_name']} is {person_2['age']} and email is {person_2['email']}")

print("\n")

print("################## Section 3 ########################")

print(f"Keys for person_2 {person_2.keys()}")

print("\n")

print(f"Values for person_2 {person_2.values()}")

print("\n")

print("################## Section 4 ########################")

person_2.pop("email")

print(person_2)

print("\n")