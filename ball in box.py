from vpython import*

##objects
ball = sphere(pos=vector(0,0,0),radius=0.6,color = color.orange)##orange ball here!
wallr = box(pos=vector(6,0,3),size=vector(0.5,12,12),color = color.green)
walll = box(pos=vector(-6,0,3),size=vector(0.5,12,12),color = color.green)
wallt = box(pos=vector(0,6,3),size=vector(12,0.5,12),color = color.red)
wallb = box(pos=vector(0,-6,3),size=vector(12,0.5,12),color = color.red)
wallf = box(pos=vector(0,0,-3),size=vector(12,12,0.5),color = color.cyan)
wallc = box(pos=vector(0,0,9),size=vector(12,12,0.5),color = color.cyan, opacity=0.1)
ball.trail=curve(color=ball.color)
##initial conditions
ball.v = vector(25,5,15)##'v' is the objects velocity.
t = 0
deltat = 0.009
vscale = 0.08
var = arrow(pos=ball.pos,axis= vscale*ball.v,color=color.magenta)
scene.autoscale=0
r=0.6+0.25##'r' is a value of the addition of the ball's radius and the wall's (1/2*width).
##calculations
while 1:
    rate(100)

    if ball.pos.x+r > wallr.pos.x:##ball does not go past this position.
        ball.v.x = -ball.v.x
    if ball.pos.y+r > wallt.pos.y:#Here I used the value 'r; to modify the conditions in order to prevent the ball from going through the walls.
        ball.v.y = -ball.v.y
    if ball.pos.y-r< wallb.pos.y:
        ball.v.y = -ball.v.y
    if ball.pos.x -r< walll.pos.x:
        ball.v.x = -ball.v.x
    if ball.pos.z-r < wallf.pos.z:
        ball.v.z = -ball.v.z
    if ball.pos.z+r > wallc.pos.z:##instead of just coding for the ball to not go past a position in the 'z' direction, I used 'opacity=0.1' in order to see through the wall. 
        ball.v.z = -ball.v.z 

    ball.trail.append(pos=ball.pos)
    ball.pos = ball.pos + ball.v*deltat
    t = t + deltat
    var.pos=ball.pos
    var.axis=ball.v*vscale##update the arrow's axis.
