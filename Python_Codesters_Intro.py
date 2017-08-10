#1. Create variable "x" with value 10.
#2. Get a sprite and a background.
#3. Make the sprite move to 3 different positions.  For an extra challenge, make the positions random.
#4. Print out “Hello world!” to the console.
#5. Print out your variable “x” to the console.
#6. Print out the x and y coordinate of the sprite in the console.
#7. Print out the numbers 1 through 10 to the console.  Hint: Use a loop.
#8. Make the sprite always go to the mouse pointer.
#9. Add in another sprite that goes to a new random position every 2 seconds.  Every time it moves it should print out its new location in the console.
#10. Add in the functionality to check if the sprites hit one another.  If they hit each other, one of them should say “ouch”.
#11. Add in a variable that keeps track of how many times the sprites have hit each other.
#12. If the sprites have hit each other 10 times, they should stop moving and text saying game over should appear on the screen.
#13. Get a number input from the user and print it out to the console with the text “ Number:  “.
#14. Add in a display so that there is always text on the screen displaying the number of times that the sprites have hit one another.
#15. Get a number input from the user and check if it is even or odd.  If it is even print out "even number".  Otherwise, print out "odd number".


# Exercise 2
sprite = codesters.Sprite("spaceship")
stage.set_background("mars")

# Exercise 8
def mouse_move():
    x = stage.mouse_x()
    y = stage.mouse_y()
    sprite.set_position(x, y)

stage.event_mouse_move(mouse_move)

# Exercise 9
ufo = codesters.Sprite("ufo")

def interval():
    ufo.go_to(random.randint(-250, 250), random.randint(-250, 250))

stage.event_interval(interval, 2)

# Exercises 10, 11, 12, 14
hits = 0
hits_text = codesters.Text("Hits:  0", 0, 200)
def collision(sprite, hit_sprite):
    global hits
    ufo.go_to(random.randint(-250, 250), random.randint(-250, 250))
    sprite.say("Ouch", 0.5)
    hits += 1
    hits_text.set_text("Hits: " + str(hits))
    if hits >= 10:
        game_over = codesters.Text("Game Over", 0, 0)
        stage.remove_sprite(sprite)

sprite.event_collision(collision)

# Exercise 15
num = int(input("Enter a number:  "))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")

