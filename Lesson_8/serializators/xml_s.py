import xml.etree.ElementTree as ET
def xml_serializator(person_list, n):

    def xml_element(person):
        person_xml = ET.Element("Person")
        name_xml = ET.SubElement(person_xml, "name")
        name_xml.text = person.name
        interests_xml = ET.SubElement(person_xml, "interests")
        for interest in person.interests:
            interest_xml = ET.SubElement(interests_xml, "interest")
            interest_xml.text = interest
        projectToHours_xml = ET.SubElement(person_xml, "projectToHours")
        for project, hours in person.projectToHours.items():
            project_xml = ET.SubElement(projectToHours_xml, "project")
            project_xml.text = project
            hours_xml = ET.SubElement(projectToHours_xml, "hours")
            hours_xml.text = str(hours)
        age_xml = ET.SubElement(person_xml, "age")
        age_xml.text = str(person.age)
        salary_xml = ET.SubElement(person_xml, "salary")
        salary_xml.text = str(person.salary)
        xml_string = ET.tostring(person_xml)
        return xml_string

    with open(f'files/persons_{n}.xml', 'wb') as file:
        xml_strings = [xml_element(person) for person in person_list]
        file.write(b'<Persons>' + b''.join(xml_strings) + b'</Persons>')

    return f'files/persons_{n}.xml'