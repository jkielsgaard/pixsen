from ursina  import *
from objects import *
from random  import randrange, choice
from time    import sleep


app = Ursina()

window.borderless   = False
camera.orthographic = True
camera.fov          = 110
camera.position     = (50, 50)


## Endpoints
numb_endpoint = 10
endpoints = []
for i in range(numb_endpoint):
    endpoints.append( 
        Endpoint( 
            position    = ( randrange(0, 100), randrange(0, 100), 0 ), 
            name        = i
        ) 
    )


## Walls
num_wall = 20
walls = []
for i in range(num_wall):
    xwall = randrange(10, 90)
    ywall = randrange(10, 90)
    xywall = random.choice(['X', 'Y'])
    
    for w in range(4):
        if xywall == 'X': xwall += 1
        if xywall == 'Y': ywall += 1

        walls.append( 
            Wall(
                position    = ( xwall, ywall, 0 ) 
            ) 
        )


## Blobs
blobpopulation = 1
blobs = []
for i in range(blobpopulation):
    blobs.append( 
        Blob( 
            position    = ( randrange(10, 90), randrange(10, 90), 0 ), 
            goto        = randrange(0, 10), 
            age         = randrange(0, 150) 
        )
    )


## Engine
def update():
    time.sleep(0.1)

    for blob in blobs:
        
        if blob.x == endpoints[blob.gotoendpoint].x and blob.y == endpoints[blob.gotoendpoint].y: blob.gotoendpoint = randrange(0, 10)

        # for wall in walls:
        #     if blob.x - 1 == wall.x: blob.y += 1
        #     if blob.x + 1 == wall.x: blob.y -= 1


        if blob.x > endpoints[blob.gotoendpoint].x: blob.x -= 1
        if blob.y > endpoints[blob.gotoendpoint].y: blob.y -= 1
        if blob.x < endpoints[blob.gotoendpoint].x: blob.x += 1
        if blob.y < endpoints[blob.gotoendpoint].y: blob.y += 1

        

        blob.age += 1
        # blob.color = color.rgb(blob.age, blob.age, 255, a=255)  
        #if blob.age == 250: blob.visible = False


app.run()