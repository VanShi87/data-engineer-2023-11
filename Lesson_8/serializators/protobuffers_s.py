from protobuf3.message import Message
from protobuf3.fields import StringField, MessageField, FloatField, Int32Field


class Person_protobuf(Message):

    class ProjectToHoursEntry(Message):
        pass

Person_protobuf.ProjectToHoursEntry.add_field('key', StringField(field_number=1, optional=True))
Person_protobuf.ProjectToHoursEntry.add_field('value', Int32Field(field_number=2, optional=True))
Person_protobuf.add_field('name', StringField(field_number=1, optional=False))
Person_protobuf.add_field('interests', StringField(field_number=2, repeated=True))
Person_protobuf.add_field('projectToHours', MessageField(field_number=3, repeated=True, message_cls=Person_protobuf.ProjectToHoursEntry))
Person_protobuf.add_field('age', Int32Field(field_number=4, optional=False))
Person_protobuf.add_field('salary', FloatField(field_number=5, optional=False))

def protobuffers_serializator(person_list):
    with open('files/person.protobuf', 'wb') as file:
        for person in person_list:
            person_protobuf = Person_protobuf()
            person_protobuf.name = person.name
            person_protobuf.interests.extend(person.interests)
            for key, value in person.projectToHours.items():
                field = Person_protobuf.ProjectToHoursEntry()
                field.key = key
                field.value = value
                person_protobuf.projectToHours.append(field)
            person_protobuf.age = person.age
            person_protobuf.salary = person.salary
            serialized_data = person_protobuf.encode_to_bytes()
            file.write(serialized_data)

