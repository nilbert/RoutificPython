from visit import Visit
from vehicle import Vehicle
from options import Options
from response import Response
import unirest
import json

ROUTIFIC_URL = "https://api.routific.com/v1/vrp"

'''
https://api.routific.com/v1/vrp | Synchronous Vehicle Routing API

https://api.routific.com/v1/vrp-long | Long-running task for VRP

https://api.routific.com/v1/pdp | Pickup and Delivery API

https://api.routific.com/v1/pdp-long | Long-running task for PDP
'''

class Routific(object):
    def __init__(self, token):
        self.token = token
        self.visits = {}
        self.fleet = {}
        self.options = {}

    def addVisit(self, id, lat, lng, name=None, start=None, end=None, duration=None, load=None, type=None,priority=None):
        self.visits[id] = Visit(lat, lng, name, start, end, duration, load, type,priority)

    def addVehicle(self, id, startId, startLat, startLng, endId=None, endLat=None, endLng=None, startName=None,
                   endName=None, shiftStart=None, shiftEnd=None, capacity=None, speed=None, type=None, strictStart=None,
                   minVisits=None, breakStart=None, breakEnd=None, breakDuration=None):
        self.fleet[id] = Vehicle(startId, startLat, startLng, endId, endLat, endLng, startName, endName, shiftStart,
                                 shiftEnd, capacity, speed, type, strictStart, minVisits, breakStart, breakEnd,
                                 breakDuration)

    def addOptions(self, traffi, min_visits_per_vehicle, balance, min_vehicles, shortest_distance):
        self.options = Options(traffi, min_visits_per_vehicle, balance, min_vehicles, shortest_distance)

    def fetchRoute(self):
        try:
            data = json.dumps(self.dictForFetchRoute())
            # unirest.timeout(5)
            response = unirest.post(ROUTIFIC_URL,
                                    headers={"Content-Type": "application/json", "Authorization": self.token}, params=data)

            # response.code  # The HTTP status code
            # response.headers  # The HTTP headers
            # response.body  # The parsed response
            j=response.raw_body  #
            objresponse=Response(j)
            sol=objresponse.solution['vehicle_1']
            return response
        except Exception as e:
            print e.message

    def dictForFetchRoute(self):
        try:

            data = {
                "visits": {},
                "fleet": {},
                "options": {}
            }

            for key in self.visits:
                visit = self.visits[key]
                data["visits"][key] = visit.toDict()

            for key in self.fleet:
                vehicle = self.fleet[key]
                data["fleet"][key] = vehicle.toDict()
            if self.options:
                data["options"] = self.options.to_dict()

            return data
        except Exception as e:
            print e.message
