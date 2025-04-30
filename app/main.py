from typing import List, Dict

class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people: List[Dict[str, object]]) -> List[Person]:
    total_list: List[Person] = []

    for person in people:
        name = person["name"]
        age = person["age"]
        instance = Person(name, age)
        total_list.append(instance)

    for person in people:
        instance = Person.people[person["name"]]
        if "husband" in person and person["husband"] is not None:
            instance.husband = Person.people[person["husband"]]
        elif "wife" in person and person["wife"] is not None:
            instance.wife = Person.people[person["wife"]]

    return total_list