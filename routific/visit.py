from location import Location
import json

'''
location |	Location object	required
start |	String ("hh:mm")	optional
end |	String ("hh:mm")	optional
duration |	Number (minutes)	optional
load |	Number (any unit)	optional
type |	String or Array	optional
priority |	String (low, regular(default), high)	optional
'''


class Visit(object):
    '''
    (String(hh:mm))     start
    (String(hh:mm))     end
    (Number (minutes))  duration
    (Number (any unit)) load
    (String or Array)   type
    '''

    def __init__(self, lat, lng, name=None, start=None, end=None, duration=None, load=None, type=None,priority=None):
        # TODO: Type check parameters
        self.location = Location(lat, lng, name)
        self.start = start
        self.end = end
        self.duration = duration
        self.load = load
        self.type = type
        self.priority = priority

    '''
    Serialize object to dictionary
    '''

    def toDict(self):
        visit = {}

        if self.location: visit["location"] = self.location.toDict()
        if self.start:    visit["start"] = self.start
        if self.end:      visit["end"] = self.end
        if self.duration: visit["duration"] = self.duration
        if self.load:     visit["load"] = self.load
        if self.type:     visit["type"] = self.type
        if self.priority:     visit["priority"] = self.priority

        return visit

    def toJson(self):
        return json.dumps(self.toDict())
