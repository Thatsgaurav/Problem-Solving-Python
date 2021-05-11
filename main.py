class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(
    f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")


# OOP
class playerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_thing(cls, num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Gaurav', 20)

print(player1.adding_thing(2, 3))
