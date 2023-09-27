from .person import Person

class Mage(Person):
    __level = 0
    __skills = []

    def __init__(self, name, personId, team, level = 0, skills = []):
        super().__init__(name, personId, team)
        self.level = level
        self.skills = skills
    
    def new_level(self, level):
        self.level = level
        print(f"{self.name} is now level {level}")

    def get_skills(self, skills):
        self.skills = skills
        print(f"{self.name} has learned {skills}")
