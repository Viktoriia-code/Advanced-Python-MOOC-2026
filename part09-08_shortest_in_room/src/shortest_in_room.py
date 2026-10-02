# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
    
    def add(self, person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        if len(self.persons) == 0:
            return True
        return False

    def print_contents(self):
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")
    
    def shortest(self):
        if self.is_empty():
            return None
        shortest_person = self.persons[0]
        for person in self.persons:
            if person.height < shortest_person.height:
                shortest_person = person
        return shortest_person
    
    def remove_shortest(self):
        if self.is_empty():
            return None
        shortest_person = self.shortest()
        self.persons.remove(shortest_person)
        return shortest_person