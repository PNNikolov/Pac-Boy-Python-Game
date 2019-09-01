import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("navy blue")
wn.title("Pac Boy")
wn.screensize(1000,1000)
wn.tracer(0)
wn.setup(width = 1.0, height = 1.0)


#Register figures
images = ["wizard_right.gif", "wizard_left.gif", 
          "treasure.gif", "wall.gif", 
          "daemon_right.gif", "daemon_left.gif", "house.gif"]
for image in images:
    turtle.register_shape(image)


#Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wizard_right.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.gold = 0
    
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 35
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() -35
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        
    def go_left(self):
        move_to_x = player.xcor() - 35
        move_to_y = player.ycor()
        
        self.shape("wizard_left.gif")
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        
    def go_right(self):
        move_to_x = player.xcor() +35
        move_to_y = player.ycor()
        
        self.shape("wizard_right.gif")
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        
    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2)+(b**2))
        
        if distance < 5:
            return True
        else:
            return False
            
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 150
        self.goto(x, y)
        
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Gate(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("house.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 150
        self._x=x
        self._y=y
        self.hideturtle()
        
        
    def show(self):
        self.showturtle()
        self.goto(self._x, self._y)
        
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
        
class Daemon(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("daemon_left.gif")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up","down","left", "right"])
        turtle.ontimer(self.move, t=250)
   
    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 35
        elif self.direction == "down":
            dx = 0
            dy = -35
            
        elif self.direction == "left":
            dx = -35
            dy = 0
            self.shape("daemon_left.gif")
        elif self.direction == "right":
             dx = 35
             dy = 0            
             self.shape("daemon_right.gif")
        else:
            dx = 0
            dy = 0
        
        #Calculate movement
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        
        
        #Check if there is a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #different direction
            self.direction = random.choice(["up","down","left","right"])
        
        #set movement timer
        turtle.ontimer(self.move, t=random.randint(100, 300))
        
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()   
        
#Create Levels list
levels = []

#Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                   X      D              X",
"X   XXXXXXX         X          XXXXXXX    X",
"X   X                                X    X",
"X P X          XXXXXXXXXXX     X     X    X",
"XXXXX               X          X     X    X",
"X      XXXXXXXX     X          XT    X    X",
"X             X     X          XXXXX X    X",
"X             X     X                     X",
"X  X          X     T                 X   X",
"X  X          XXXXXXXXXXXXXX    D     X   X",
"X  X          X            X          X   X",
"X  XXXXXXXXX  X            X   XXXXXXXX   X",
"X  X          X            X          X   X",
"X  X          XXXXXXXXXXXXXX          X   X",
"X  X   X            X                 X   X",
"X      X            X                     X",
"X      X            X   D           X XXXXX",
"X D    X            X               X     X",
"XXXXXXXX       XXXXXXXXXXXX         X  Y  X",
"XT                                  X     X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_2 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X             X     X      D              X",
"X       X     X     X  XXXXX   XXXXXXX    X",
"X   X   X     X     X    X                X",
"X P X   X     X     T    X     X     X    X",
"XXXXX   X     X     X    X     X     X    X",
"X       X                X                X",
"X XXXXXXXXXXX X     X  XXXXX   XXXXXXX    X",
"X             X     X                     X",
"X  X          X                       X   X",
"X  X          XXXXXXXXXXXXXX    D     X   X",
"X  X          X            X          X   X",
"X  TXXXXX     X            X   XXXXXXXX   X",
"X  X          X            X          X   X",
"X  X          XXXXXXXXXXXXXX          X   X",
"X  X   X            X                 X   X",
"X      X            X        X        T   X",
"X      X        XXXXX   D    X      X XXXXX",
"X D    X            X        X      X     X",
"XXXXXXXX            X        X      X  Y  X",
"X                            X      X     X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_3 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X       XXXXXXXXXXXXX                     X",
"X   X   XXXXX T XXXXX      XXXXXXXXXX     X",
"X   X   XXXX     XXXX      X        X     X",
"X P X   XXX       XXX      X        X     X",
"XXXXX   XX         XX      X        X  T  X",
"X       X           X  D   X        X     X",
"XXXXXXX XXXXXX XXXXXXXXXXXXX        X     X",
"X                                   X     X",
"X                                         X",
"XXXXXX        XXXXXXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXX        X            X   XXXXXXXXXXXX",
"XXXXXXXXXX    X            X       DXXXXXXX",
"X  TXX        X            X   XXXXXXXXXXXX",
"X  XX         XXXXXXXXXXXXXX  XXXXXXXXXXXXX",
"X  XX                    X                X",
"X  XXXXXXXXXXXX          X                X",
"X  XXD                   XXXXXXXXXX X XXXXX",
"X    XX                  X          X     X",
"X     XXXXXXXXX          X          X  Y  X",
"X                                   X     X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_4 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                                         X",
"X   X      XXXXX     X     XXXXX          X",
"X   X      X   X    XXX    X        XT    X",
"X P X      XXXXX   X D X   X       XXX    X",
"XXXXX      X       XXXXX   X        X     X",
"X          X       X   X   XXXXX       D  X",
"X                                         X",
"X                                         X",
"X                                         X",
"XXXXXXXXXXXX  XXXXXXXXXXXXXX   XXXXXXXXXXXX",
"XXXXXXXXXXXX  X            X   XXXXXXXXXXXX",
"XXXXXXXXXXXX  X            X   XXXXXXXXXXXX",
"X             X            X              X",
"X             XXXXXXXXXXXXXX              X",
"X          XXXX    XXXXX   X   X          X",
"XT         X  X    X   X   X T X          X",
"XXXXXXXXX  XXXXX   X   X   XXXXX    X XXXXX",
"X D        X   X   X   X     X      X     X",
"X          XXXXX   XXXXX     X      X  Y  X",
"X                                   X     X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_5 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X          XXXX     X     X  X     D      X",
"X   X      X  X    XXX    X  X   X    X   X",
"X   X      XXXX   X   X   XXXT  XXX  XXX  X",
"X P X      X      XXXXX   X  X   X    X   X",
"XXXXX      X      X   X   X   X           X",
"X                                         X",
"X   XXX    XXXXXXXXXXXXXXXXXXXX    XXX    X",
"X   XXX                            XXX    X",
"X   XXX                            XXX    X",
"X D XXX       XXXXXXXXXXXXXX       XXX    X",
"XXXXXXXXXXXXX X            X XXXXXXXXXXXXXX",
"XXXXXXXXXXXXX X            X XXXXXXXXXXXXXX",
"XXXXXXXXXXXXX X            X XXXXXXXXXXXXXX",
"X             XXXXXXXXXXXXXX             TX",
"X   X      XXXX    XXXXX   X   X    XXXXXXX",
"X T X      X  X    X   X   X   X          X",
"XXXXXXXXX  XXXX    X   X   XXXXX    X XXXXX",
"X D X      X   X   X   X     X      X     X",
"X   X      XXXXX   XXXXX     X      X  Y  X",
"X                                   X     X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_6 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X        XXXX   XXXX X   X XXXX X         X",
"X   X    X   X  X    X   X X    X         X",
"X   X    X    X XXX  X   X XXX  X    XXXXXX",
"X P X    X   X  X     X X  X    X         X",
"XXXXX    XXXX   XXXX   X   XXXX XXXX  D   X",
"X                                         X",
"X   XX  XXXX                 XXXX XXXX    X",
"X  X  X X  X                 X    X   X   X",
"X  X  X XXXX        D        XXXT X    X  X",
"X  X  X X     XXXXXXXXXXXXXX X    X   X   X",
"X   XX  X     X            X XXXX XXXX    X",
"X             X            X              X",
"XXXXXXXXXXXXX X            X    X XXXXXXXXX",
"X  D        X XXXXXXXXXXXXXX    X         X",
"X        X  X   XXX  X   X      X XXXXXXX X",
"X        X  X   X X  X   X      X X       X",
"XXXXXXXXTX  X   XXXX  X X       X X X XXXXX",
"XD       X      X  X   X        X X X     X",
"XXXXXXXXXX      XXXX   X        X X X  Y  X",
"X                               X XTX     X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_7 =[
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     XXXX XXXX XXXX XXXX X      X   X  X X",
"X   X X  X X  X X    X    X  D  XXX  X  X X",
"X   X XXXX XXXX XXX   X   X    X   X X  X X",
"X P X X    X X  X      X  X    XXXXX X TX X",
"XXXXX X    X  X XXXX XXXX XXXX X   X  XX  X",
"X                    X                    X",
"X  XXXXXXX   XXX     X    XXX     X X     X",
"X     X       X      X     X      X X   X X",
"X     X       X      T     X      X X   X X",
"X     X       XXXXXXXXXXXXXX      X XXXXX X",
"X     X       X            X      X    DXTX",
"X  XXXXXXX XXXX            XXXX   XXXXXXXXX",
"X             X            X              X",
"X             XXXXXXXXXXXXXX              X",
"X X   X XXX X  X XXXX X    XXXX X  X      X",
"X XX  X  X  XDX  X  X X    X  X X  X      X",
"X X X X  X  XXX  X  X X    X  X X  XX XXXXX",
"X X  XX  X  X  X X  X X    X  X X  XX     X",
"X X   X XXX X  X XXXX XXXX XXXX  XX X  Y  X",
"X                                   X     X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]


#Treasure
treasures = []

#Add deamon
daemons = []

#Add map to maps list
levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)
levels.append(level_5)
levels.append(level_6)
levels.append(level_7)
gates = []

def print_map(level):
    for y in range(len(level)):
        print(level[y])

#Create Level Setup Function
def setup_map(level):
    pen.clear()
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x,y coordinates
            #NOTE the order of y and x in the next line
            character = level[y][x]
            #Calculate the screen x,y coordinates
            screen_x = -720 + (x*35)
            screen_y = 370 - (y*35)
        
        
            #Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                
                walls.append((screen_x, screen_y))
                
            #Check if it is a P (representing Player)
            if character == "P":
                player.goto(screen_x, screen_y)
                
            #Check if it is a T (representing Treasure)    
            if character == "T":  
                treasures.append(Treasure(screen_x, screen_y))
            
            #Check if it is an D (Representing Daemon)
            if character == "D":
                daemons.append(Daemon(screen_x, screen_y))
                
            #Check if it is an Y (Representing Gate to next level)
            if character == "Y":
                gates.append(Gate(screen_x, screen_y))
                #daemons.append(Daemon(screen_x, screen_y))



for l in range(len(levels)):
    print_map(levels[l])


                
#Create clas instances
pen = Pen()
player = Player()

#Walls list
walls = []

#current Level number
level_number = 0

#Set up the level
setup_map(levels[level_number])

#Key Comands
turtle.listen()


turtle.onkeypress(player.go_left,"Left")
turtle.onkeypress(player.go_right,"Right")
turtle.onkeypress(player.go_up,"Up")
turtle.onkeypress(player.go_down,"Down")

#screen updates (Off)
wn.tracer(0)



#Main Game Loop
while True:
    #Go to the next level
    for gate in gates:
        if player.is_collision(gate):
            level_number += 1
            for daemon in daemons:
                daemon.destroy()
            
            print (level_number)
            daemons = []
            walls = []
            setup_map(levels[level_number])
            gate.destroy()
            gates.remove(gate)
                
            for gate in gates:
                gate.destroy()
            gate = []
            
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print ("Player Gold: {}".format(player.gold))
            #Desttroy treasure
            treasure.destroy()
            #Remove the treasure from the treasures list
            treasures.remove(treasure)
            if not treasures:
                for gate in gates:
                    gate.show()
    #player-daemon collides
    for daemon in daemons:
        if player.is_collision(daemon):
            print ("Game Over!")
            #pen.clear()
            #pen.write("Game Over!")
            turtle.color("red")
            turtle.setpos(-135,-75)
            turtle.write("Game Over!", move=False, align="left", font=("Arial", 39, "normal"))
            turtle.done()
            break
        else: 
            #Update screen
            wn.update()
