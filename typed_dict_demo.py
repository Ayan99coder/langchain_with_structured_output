from typing import TypedDict
class Person(TypedDict):
    name : str
    age : int

    new_person: Person = {'name':'ayan','age':'16'}

    print(new_person)