class Ticket:
    def __init__(self, passenger, employee, flight):
        self.passenger = passenger
        self.employee = employee
        self.flight = flight

    def print_travel_iternary(self):
        print("Hello {0}, your ticket from {1} to {2} has been confirmed, \nPlease find internary details below".format(
            self.passenger.name, self.passenger.source, self.passenger.destination))
        print(
            "you flight starts at {0} and reaches to destination at {1},please reach airport 3 hrs early to departure"
                .format(self.flight.start_time, self.flight.end_time))
        print("Mr {0} would be your pilot, rest assure he has flying experince of about {1} airmiles".format(
            self.employee.name, self.employee.miles_travelled))
