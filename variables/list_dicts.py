animals = ["Dogs", "Cats", "Sheep", "Goats"]

animal_index = 0
print(f"Animal number {animal_index +1 } is: {animals[animal_index]}")

animal_index = 2
print(f"Animal number {animal_index +1 } is: {animals[animal_index]}")

print(f"Length of animals list is {len(animals)}")

print("###################################################")

print("\nList before removing animal")
print(f"Animal list {animals}")

animals.append("Giraffes")

print("\nList before removing animal")
print(f"Animal list {animals}")
print("\n")

print("################## Section 3 ########################")

print(f"Length of animals list is {len(animals)}")

animal_index = 4
print(f"Animal number {animal_index + 1} is: {animals[animal_index]}")

print("\nList before removing")
print(f"Animal list {animals}")

animals.remove("Dogs")

print("\nList after removing animal")
print(f"Animal list {animals}")