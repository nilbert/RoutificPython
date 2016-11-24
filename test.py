from routific.routific import Routific

tok = 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ODJmMzcyYjRjZDllNzY5MGE2OTZmNWUiLCJpYXQiOjE0Nzk0ODkzMjN9.9uE0can0APyhv_8vkkZtGCfbEaQ6l-AD3DpVJJpegLk'

routic = Routific(token=tok)

'''
  "driver_1": {
    "start_location": {
      "id": "depot",
      "name": "800 Kingsway",
      "lat": 49.2553636,
      "lng": -123.0873365
    },
    "end_location": {
      "id": "depot",
      "name": "800 Kingsway",
      "lat": 49.2553636,
      "lng": -123.0873365
    },
    "shift_start": "8:00",
    "shift_end": "17:00",
    "min_visits": 14,
    "capacity": 10,
    "type": ["A", "B"],
    "strict_start": true,
    "break_start": "12:00",
    "break_end": "13:30",
    "break_duration": 30
  }
'''

routic.addVehicle("vehicle_1","depot",49.2553636,-123.0873365,"depot",49.2553636,-123.0873365,
                  "800 Kingsway","800 Kingsway","8:00","17:00",None,None,["A","B"], None,None,"12:00","13:30",30)
# routic.addVehicle("vehicle_2", "depot", 49.2553636, -123.0873365, "depot", 49.2553636, -123.0873365,
#                   "800 Kingsway", "800 Kingsway", "8:00", "17:00", None, None, ["A", "B"], None, 10, "12:00", "13:30",
#                   30)

'''
"visits": {
  "order_1": {
    "location": {
      "name": "6800 Cambie",
      "lat": 49.227107,
      "lng": -123.1163085
    },
    "start": "9:00",
    "end": "12:00",
    "duration": 10,
    "load": 1,
    "type": "A",
    "priority": "high"
  }
}

'''

routic.addVisit("order_1",49.227107, -123.1163085,"6800 Cambie","9:00","12:00",10,1,"A")

response=routic.fetchRoute()
