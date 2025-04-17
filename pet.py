# Define the Pet class
class Pet:
    # Constructor to initialize pet attributes when a Pet object is created
    def __init__(self, name):
        self.name = name                # Pet's name
        self.hunger = 5                 # Hunger level (0 = full, 10 = very hungry)
        self.energy = 5                 # Energy level (0 = tired, 10 = fully rested)
        self.happiness = 5             # Happiness level (0–10)
        self.tricks = []               # List to store tricks the pet learns

    # Method for the pet to eat
    def eat(self):
        # Reduce hunger by 3, not going below 0
        self.hunger = max(0, self.hunger - 3)
        # Increase happiness by 1, not exceeding 10
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} eats and looks happier!")

    # Method for the pet to sleep
    def sleep(self):
        # Increase energy by 5, not exceeding 10
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} takes a nap and feels refreshed.")

    # Method for the pet to play
    def play(self):
        # Check if pet has enough energy to play
        if self.energy >= 2:
            self.energy -= 2                         # Playing reduces energy
            self.happiness = min(10, self.happiness + 2)  # Playing increases happiness
            self.hunger = min(10, self.hunger + 1)        # Playing makes the pet hungrier
            print(f"{self.name} plays and has fun!")
        else:
            print(f"{self.name} is too tired to play. Let them rest.")

    # Bonus method: teach the pet a new trick
    def train(self, trick):
        self.tricks.append(trick)                     # Add the trick to the list
        self.happiness = min(10, self.happiness + 1)  # Learning makes the pet happy
        print(f"{self.name} learned how to {trick}!")

    # Bonus method: display all tricks the pet has learned
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

    # Method to print the current status of the pet
    def get_status(self):
        print(f"\n🐾 {self.name}'s Current Status:")
        print(f"🦴 Hunger: {self.hunger}/10")
        print(f"💤 Energy: {self.energy}/10")
        print(f"😊 Happiness: {self.happiness}/10\n")
