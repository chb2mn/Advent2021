from icecream import ic
from copy import deepcopy

class Beacon:
    def __init__(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z


class Scanner:
    def __init__(self):
        self.beacons = []
        self.top =[]
        self.bot =[]
        self.west=[]
        self.east=[]
        self.north=[]
        self.south=[]
    def add_beacon(self, x,y,z):
        self.beacons.append((x,y,z))

    def get_perimeter(self):
        temp = deepcopy(self.beacons)
        while len(self.top) < 12:
          
        self.top=max(self.beacons, key=lambda x: x[1])
        self.bot=min(self.beacons, key=lambda x: x[1])
        self.east=max(self.beacons, key=lambda x: x[2])
        self.west=min(self.beacons, key=lambda x: x[2])
        self.north=max(self.beacons, key=lambda x: x[0])
        self.south=min(self.beacons, key=lambda x: x[0])

    def rotate(self, axis:int):
        '''
        rotate right around the {0==N/S, 1==T/B, 2==E/W axis}
        '''
        if axis == 0:
            temp = self.east
            self.east = self.top
            self.top = self.west
            self.west = self.bot
            self.bot = temp
        elif axis == 1:
            temp = self.north
            self.north = self.west
            self.west = self.south
            self.south = self.east
            self.east = temp
        elif axis == 2:
            temp = self.north
            self.north = self.top
            self.top = self.south
            self.south = self.bot
            self.bot = temp



