import pgzrun
from random import randint

WIDTH = 853
HEIGHT = 480

bg_color = "background0"

level = 1
speed = 1

alien = Actor('alien')
zombie = Actor('zombie')


alien.pos = 30,300
zombie.pos = WIDTH - 100,HEIGHT -174
dead = False

def draw():
    global level,dead
    if dead:
        screen.blit(bg_color,(0,0))
        screen.draw.text("Zombie Ate You !!!",((WIDTH//2-100),HEIGHT//2),fontsize=30, color="white")
    else:
        screen.blit(bg_color,(0,0))
        zombie.draw()
        alien.draw()
        screen.draw.text("Level : {}".format(str(level)),(10,10),fontsize=30, color="white")
        
    
def update():
    global bg_color,dead,level,speed
    if not dead:
        alien.left +=3
        zombie.left -= speed
        if alien.right >= WIDTH:
                bg_color = "background{}".format(randint(0,4))
                screen.blit(bg_color,(0,0))
                alien.pos = 30,randint(30,306)
                zombie.pos = 753,randint(30,306)
                level +=1
                speed +=0.5
            
        if zombie.colliderect(alien):
            dead = True

def on_key_down(key):
    if key == keys.UP:
        alien.pos=alien.x ,alien.y-30
    if key == keys.DOWN:
        alien.pos=alien.x ,alien.y+30
        
pgzrun.go()
