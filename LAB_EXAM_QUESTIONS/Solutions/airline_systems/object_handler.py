from airline_systems.passenger import Passenger
from airline_systems.employee import Employee
from airline_systems.flight import Flight
from airline_systems.ticket import Ticket


def handle_objects(config_data, chosen_dict, person_info_dict):
    passenger = setup_passenger(config_data, chosen_dict, person_info_dict)
    pilot = setup_pilot(config_data,chosen_dict)
    flight = setup_flight(passenger, chosen_dict)
    ticket = Ticket(passenger, pilot, flight)
    ticket.print_travel_iternary()


def setup_passenger(config_data, chosen_dict, passenger_info):
    source = config_data["originCity"][chosen_dict["source"]]
    destination = config_data["destinationCity"][chosen_dict["destination"]]
    name = passenger_info["name"]
    gender = passenger_info["gender"]
    contact = passenger_info["contact"]
    travel_class = passenger_info["travel_class"]
    birth_date = passenger_info["birth_date"]
    passenger = Passenger(name, gender, contact, birth_date, source, destination, travel_class)
    return passenger


def setup_flight(passenger, chosen_dict):
    flight = Flight(chosen_dict["flight_id"], passenger.source, passenger.destination, chosen_dict["fare"],
                    chosen_dict["start_time"], chosen_dict["end_time"])
    return flight


def setup_pilot(config_data, chosen_dict):
    pilot_dict = config_data["pilot"][chosen_dict["pilot_id"]]
    pilot = Employee(pilot_dict["name"], pilot_dict["gender"], pilot_dict["contact"], pilot_dict["birth_date"],
                     pilot_dict["miles_travelled"], chosen_dict["pilot_id"])
    return pilot
