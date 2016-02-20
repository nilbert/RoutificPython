from visit import Visit
from vehicle import Vehicle
import urllib2
import urllib
import json

ROUTIFIC_URL = "https://api.routific.com/v1/vrp"

class Routific(object):
    def __init__(self, token):
        self.token = token
        self.visits = {}
        self.fleet = {}

    def addVisit(self,id, lat,lng,name=None,start=None,end=None,duration=None,load=None,type=None):
        self.visits[id] = Visit(lat,lng,name,start,end,duration,load,type)

    def addVehicle(self, id, startId, startLat, startLng, endId = None, endLat = None, endLng = None, startName = None,  endName = None, shiftStart = None, shiftEnd = None, capacity = None, speed = None, type = None, strictStart = None, minVisits = None, breakStart = None, breakEnd = None, breakDuration = None):
        self.fleet[id] = Vehicle(startId, startLat, startLng, endId, endLat, endLng, startName, endName, shiftStart, shiftEnd, capacity, speed, type, strictStart, minVisits, breakStart, breakEnd, breakDuration)

    def fetchRoute(self):

        data = json.dumps(self.dictForFetchRoute())
        req = urllib2.Request(ROUTIFIC_URL,data)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Authorization', self.token)

        return urllib2.urlopen(req).read()

    def dictForFetchRoute(self):
        data = {
            "visits":{},
            "fleet":{}
        }

        for key in self.visits:
            visit = self.visits[key]
            data["visits"][key] = visit.toDict()

        for key in self.fleet:
            vehicle = self.fleet[key]
            data["fleet"][key] = vehicle.toDict()

        return data