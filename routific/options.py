import json


class Options(object):
    def __init__(self, traffic=None, min_visits_per_vehicle=None, balance=None, min_vehicles=None,
                 shortest_distance=None):
        self.traffic = traffic
        self.min_visits_per_vehicle = min_visits_per_vehicle
        self.balance = balance
        self.min_vehicles = min_vehicles
        self.shortest_distance = shortest_distance


'''
  Serialize object to dictionary
  '''


def to_dict(self):
    options = {}

    if self.traffic:                options["traffic"] = self.min_visits_per_vehicle
    if self.min_visits_per_vehicle: options["min_visits_per_vehicle"] = self.min_visits_per_vehicle
    if self.balance:                options["balance"] = self.balance
    if self.min_vehicles:           options["min_vehicles"] = self.min_vehicles
    if self.shortest_distance:      options["shortest_distance"] = self.shortest_distance

    return options


def to_json(self):
    return json.dumps(self.toDict())
