# Make class
class PartyAnimal:
    x = 0
    # Increment x value for every call
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

# Define PartyAnimal class
animal = PartyAnimal()

# Call party function
animal.party()
animal.party()
animal.party()