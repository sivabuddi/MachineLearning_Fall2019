class Flight:

    def __init__(self, flight_id, source, destination, fare, start_time, end_time):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.fare = fare
        self.start_time = start_time
        self.end_time = end_time

    def get_flight_details(self):
        print("Flight No:", self.flight_id)
        print("Flight Originating city:", self.origin)
        print("Flight Destination City:", self.destination)
