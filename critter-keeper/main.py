class CritterKeeper:
    def __init__(self):
        self.name = input("What's the name of your critter keeper? ")
        self.hunger = 0
        self.boredom = 0
        self.happiness = 100

    def display_creature(self):
        # Simple ASCII visual based on happiness
        if self.happiness > 70:
            creature = r"""
              ^_^
             (o o)
            -(   )-
              " "
            """
        elif 40 <= self.happiness <= 70:
            creature = r"""
              -_-
             (o o)
            -(   )-
              " "
            """
        else:
            creature = r"""
              >_<
             (o o)
            -(   )-
              " "
            """
        print(f"\n{self.name}'s Current Appearance:")
        print(creature)

    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} is eating. Hunger decreased.")
        self.display_creature()

    def play(self):
        self.boredom -= 10
        if self.boredom < 0:
            self.boredom = 0
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100
        print(f"{self.name} is playing. Boredom decreased, happiness increased.")
        self.display_creature()

    def check_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Boredom: {self.boredom}")
        print(f"Happiness: {self.happiness}")
        self.display_creature()

    def tick(self):
        self.hunger += 5
        self.boredom += 5
        self.happiness -= 5
        if self.hunger > 100 or self.boredom > 100:
            print(f"{self.name} is feeling neglected, happiness fell")
        self.display_creature()

if __name__ == "__main__":
    pet = CritterKeeper()

    while True:
        action = input("What do you want to do? (feed, play, check, quit): ").lower()
        if action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "check":
            pet.check_status()
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid action.")
