from airline_systems.person import Person


class Employee(Person):
    def __init__(self, name, gender, contact, birth_date, miles_travelled, pilot_id):
        super(Employee, self).__init__(name, gender, contact, birth_date)
        self.miles_travelled = miles_travelled
        self.pilot_id = pilot_id

    def print_flights_info(self, config_dict):
        print(
            "Mr. {0} your details are Gender: {1},contact {2}, birth_date{3},pilot_id {4}, current miles travelled {5}".format(
                self.name, self.gender, self.contact, self.birth_date, self.pilot_id, self.miles_travelled))

        for (k, v) in config_dict["flights"].items():
            if v["pilot_id"] == self.pilot_id:
                print("##############################################################################")
                print("flight id {0}".format(v["flight_id"]))
                print("Source City {0}".format(config_dict["originCity"][v["source"]]))
                print("Destination City {0}".format(config_dict["destinationCity"][v["destination"]]))
                print("starts at {0} ends travel at {1}".format(v["start_time"], v["end_time"]))
