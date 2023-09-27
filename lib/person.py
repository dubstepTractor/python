class Person:
    __name = ""
    __personId = 0
    __team = None

    def __init__(self, name, personId, team):
        self.name = name
        self.personId = personId
        self.team = team

    def __str__(self):
        return f"Person({self.name})"

    def __eq__(self, other):
        return self.name == other.name and self.personId == other.personId and self.team == other.team
