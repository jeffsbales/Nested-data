from dataclasses import dataclass

@dataclass
class Person:
    name: str
    pets: int

@dataclass
class House:
    address: str
    owner: Person

@dataclass
class Neighborhood:
    name: str
    houses: list[House]

green_acres = Neighborhood("Green Acres", [
  House("14 Sun Drive", Person("Mary", 1)),
  House("15 Sun Drive", Person("Jenny", 0)),
  House("16 Sun Drive", Person("Jim", 5)),
])

print(green_acres.houses[0].owner.pets)