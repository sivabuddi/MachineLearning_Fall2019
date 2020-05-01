class Person:
    def __init__(self, name, gender, contact, birth_date):
        self.name = name
        self.gender = gender
        self.contact = contact
        self.birth_date = birth_date

    def get_person_info(self):
        print("name of the person {1}, gender {2}, contact number {3} and birthdate {4}".format(self.name, self.gender,
                                                                                                self.contact,
                                                                                                self.birth_date))
