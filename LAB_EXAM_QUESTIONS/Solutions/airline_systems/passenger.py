from .person import Person


class Passenger(Person):
    def __init__(self, name, gender, contact, birth_date, source, destination, travel_class):
        super(Passenger, self).__init__(name, gender, contact, birth_date)
        self.source = source
        self.destination = destination
        self.travel_class = travel_class


def ask_passenger_info():
    passenger_info = {"name": input("Enter your name"), "gender": input("Enter your gender"),
                      "contact": input("Enter your contact"), "birth_date": input("Enter your birth_date")}
    return passenger_info
