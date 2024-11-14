import random

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    @property # this is a getter
    def house(self):
        # need to add _ to the property name so python doesnt get confused
        return self._house # "instance variable" is called house but the "object property" is house (no underscore) 
    
    @house.setter # setter: needs this decorator; now when assigning value to the property (obj.house = "this house"), it will execute this function
    def house(self, house):
        self._house = house  # also the underscore signifies "private" (but there's no encapsulation/visibility)

class Hat:
    houses = ["h1", "h2", "h3"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

    Hat.sort("aly") # kind of a singleton

def get_student():
    student = Student("pancho", "villa")
    return student
    