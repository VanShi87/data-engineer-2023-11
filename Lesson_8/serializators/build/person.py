from protobuf3.message import Message
from protobuf3.fields import StringField, MessageField, FloatField, Int32Field


class Person(Message):

    class ProjectToHoursEntry(Message):
        pass

Person.ProjectToHoursEntry.add_field('key', StringField(field_number=1, optional=True))
Person.ProjectToHoursEntry.add_field('value', Int32Field(field_number=2, optional=True))
Person.add_field('name', StringField(field_number=1, optional=True))
Person.add_field('interests', StringField(field_number=2, repeated=True))
Person.add_field('projectToHours', MessageField(field_number=3, repeated=True, message_cls=Person.ProjectToHoursEntry))
Person.add_field('age', Int32Field(field_number=4, optional=True))
Person.add_field('salary', FloatField(field_number=5, optional=True))
