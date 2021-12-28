from ursina import *

class Blob(Entity):
    def __init__(self, position=(0,0,0), goto='', age = 0):
        super().__init__()
        self.position       = position
        self.model          = 'circle'
        self.color          = color.rgb(0, 128, 255, a=255)  
        self.gotoendpoint   = goto
        self.age            = age
        self.visible        = True

class Wall(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__()
        self.position       = position
        self.model          = 'quad'
        self.color          = color.rgb(160, 160, 160, a=255) 

class Endpoint(Entity):
    def __init__(self, position=(0,0,0), name=''):
        super().__init__()
        self.position       = position
        self.model          = 'circle'
        self.color          = color.rgb(204, 0, 0, a=255) 
        self.endpointname   = name
        self.scale          = 2
