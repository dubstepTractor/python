from .person import Person

class Paladin(Person):
    def __init__(self, name, personId, team):
        super().__init__(name, personId, team)
    
    def go_to_mage(self, mage):
        self.team = mage.team
        print(f"{self.name} is now on team {self.team}")
