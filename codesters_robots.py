#define game variables
score = 0
sprite_list = []
display = codesters.Text("Score:", 0, 200, "red")

#on-click function for robot sprites
def click(sprite):
    global score
    score += sprite.points
    display.set_text("Score: {}".format(score))
    sprite.set_x(random.randint(-220, 220))
    sprite.set_y(random.randint(-220, 220))
    
#create four sprites
def sprite_creation():
    for num in range (2):
        sprite = codesters.Sprite("robot", random.randint(-220, 220), random.randint(-220, 220))
        sprite.points = num + 1
        sprite.event_click(click)
        sprite_list.append(sprite)

def sprite_creation2():
    for num in range (2):
        sprite = codesters.Sprite("robot", random.randint(-220, 220), random.randint(-220, 220))
        sprite.points = num + 1
        sprite.event_click(click)
        sprite_list.append(sprite)

#sprite's "while" loop         
def game():
    sprite_creation()
    while score < 25:
        for sprite in sprite_list:
            sprite.set_x(random.randint(-220, 220))
            sprite.set_y(random.randint(-220, 220))
        stage.wait(2)
    sprite.say("You Win!")

game()
