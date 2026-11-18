from dataclasses import dataclass

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

creature_1.level = 100
creature_1.health = 20
print(f"Creature 1 name: {creature_1.name}, species: {creature_1.species}, level: {creature_1.level}, health: {creature_1.health}")
