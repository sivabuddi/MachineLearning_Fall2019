"""
Problem 3 :
Airline   Booking   Reservation   System   (e.g.   classes   Flight,   Person, Employee,   Passenger etc.)
"""
import json
from airline_systems.passenger import ask_passenger_info
from airline_systems.object_handler import handle_objects
from airline_systems.employee import Employee

with open('config.json') as json_data_file:
    data = json.load(json_data_file)


def interactive_console():
    print("welcome to our {0} , Please choose which service would you like with us ".format(data['name']))
    print("Note: Please use option number to select the services")
    print_services_info("airlineServices")
    option = input("Enter your choice of Service")
    serve_customer(option)


def print_services_info(key):
    for (k, v) in data[key].items():
        print(k, v)


def book_tickets():
    passenger_info = ask_passenger_info()
    print_services_info("class")
    class_info = input("Choose travel class from below")
    passenger_info["travel_class"] = data["class"][class_info]
    chosen = {}
    print("we currently operate at below sources")
    print_services_info("originCity")
    print("we currently deliver to below destinations")
    print_services_info("destinationCity")
    source = input("enter your source city")
    destination = input("enter your destination city")
    for (k, v) in data["flights"].items():
        if v["source"] == source and v["destination"] == destination:
            chosen = v
    handle_objects(data, chosen, passenger_info)


def get_flight_info():
    pilot_id = input("Enter your pilot id")
    pilot_dict = data["pilot"][pilot_id]
    pilot = Employee(pilot_dict["name"], pilot_dict["gender"], pilot_dict["contact"], pilot_dict["birth_date"],
                     pilot_dict["miles_travelled"], pilot_id)
    pilot.print_flights_info(data)


def serve_customer(option):
    if option == "1":
        book_tickets()
    if option == "2":
        get_flight_info()


interactive_console()
