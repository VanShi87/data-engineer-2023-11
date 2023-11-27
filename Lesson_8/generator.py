from typing import List, Dict

import faker
import numpy as np
from pydantic import BaseModel

facker_fabric = faker.Faker()
class Person(BaseModel):
    name: str
    interests: List[str]
    projectToHours: Dict[str, int]
    age: int
    salary: float


def create_person_list(n):
    person_list = []
    for i in range(n):
        name = facker_fabric.name()
        interests = facker_fabric.words(nb=np.random.randint(0,10),
                                        part_of_speech = 'noun',
                                        unique=True)
        projectToHours = {facker_fabric.paragraph(nb_sentences=1)[:-1]: np.random.randint(1, 72)
                          for _ in range(np.random.randint(0,10))
                         }
        age = np.random.randint(18, 65)
        salary = float(np.round(11500 + np.random.random()*50000))
        person = Person(name=name, interests=interests, projectToHours=projectToHours, age=age, salary=salary)
        person_list.append(person)
    return person_list


