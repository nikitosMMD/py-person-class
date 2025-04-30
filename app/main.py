from typing import List, Dict, Optional, Union


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[self.name] = self


def create_person_list(people: List[Dict[str, Union[str, int, None]]]) -> List[Person]:
    total_list: List[Person] = []

    for person in people:
        name: str = person["name"]  # type: ignore
        age: int = person["age"]    # type: ignore
        person_instance = Person(name, age)
        total_list.append(person_instance)

    for person in people:
        current_person = Person.people[person["name"]]
        spouse_name = person.get("wife") or person.get("husband")
        if spouse_name is not None:
            if "wife" in person:
                current_person.wife = Person.people[spouse_name]
            elif "husband" in person:
                current_person.husband = Person.people[spouse_name]

    return total_list