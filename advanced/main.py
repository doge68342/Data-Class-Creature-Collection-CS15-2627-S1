from dataclasses import dataclass

def get_user_input(prompt, data_type, max):
    if data_type == "string":
        return input(prompt)
    elif data_type == "int":
        try:
            output = int(input(prompt))
            if output <= max and output > 0 or max == 0:
                return output
            else:
                print(f"Please input an integer between 1 and {max}")
                return get_user_input(prompt, data_type, max)
        except ValueError:
            print("Please input integer and try again")
            return (get_user_input(prompt, data_type, max))
    elif data_type == "float":
        try:
            output = float(input(prompt))
            return output
        except ValueError:
            print("Please input float and try again")
            return (get_user_input(prompt, data_type, max))

@dataclass
class Creature:
    name: str
    species: str
    level: int
    health: float

creature_1 = Creature("fella", "fellian", 0, 0.1)
creature_2 = Creature("john", "Doe", 100, 10)
creature_3 = Creature("toast", "cat", 10, 0.01)

print(f"Creature 1 name: {creature_1.name}, species: {creature_1.species}, level: {creature_1.level}, health: {creature_1.health}")
print(f"Creature 2 name: {creature_2.name}, species: {creature_2.species}, level: {creature_2.level}, health: {creature_2.health}")
print(f"Creature 3 name: {creature_3.name}, species: {creature_3.species}, level: {creature_3.level}, health: {creature_3.health}")

print("Create new creature")
name = get_user_input("Name: ", "string", None)
species = get_user_input("Species: ", "string", None)
level = get_user_input("Level: ", "int", 0)
health = get_user_input("Health: ", "float", None)
my_creature = Creature(name, species, level, health)

print(f"Your creature name: {my_creature.name}, species: {my_creature.species}, level: {my_creature.level}, health: {my_creature.health}")