import json

'''
status	|"success"	A sanity check, will always be success when the HTTP code is 200.
total_travel_time |	Number (minutes)	Total travel time of the entire fleet in minutes.
total_idle_time |	Number (minutes)	Total number of minutes that the entire fleet in waiting idle.
num_unserved |	Number	Number of visits that could not be scheduled.
unserved |	Object	Visits that could not be scheduled, with their reasons.
solution |	Object	The optimized schedule, where the keys reference the vehicle IDs and the values are ordered arrays of visits (and estimated arrival and finish times).
'''


class RouteResponse(object):
    def __init__(self, json=None, location_id=None, location_name=None, arrival_time=None):
        self.location_id = location_id
        self.location_name = location_name
        self.arrival_time = arrival_time

    def load_json(self,json=None):
        if json:
            self.__dict__ = json.loads(json)


class VehicleResponse(object):
    def __init__(self, json=None, routesresponse=None):
        self.routesresponse = routesresponse

    def load_json(self, json=None):
        if json:
            self.__dict__ = json.loads(json)


class Response(object):
    def __init__(self, j=None, status=None, total_travel_time=None, total_idle_time=None, num_unserved=None,
                 unserved=None, solution=None):
        self.status = status
        self.total_travel_time = total_travel_time
        self.total_idle_time = total_idle_time
        self.num_unserved = num_unserved
        self.unserved = unserved
        self.solution = solution
        if j:
            self.__dict__ = json.loads(j)


    def load_json(self):
        return json.loads(self.solution)
