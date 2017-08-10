#Note: Seconds are 0.333 seconds each, for the sake of working with whole numbers.

seconds = codesters.Line(0, -15, 0, 15, "blue")
minutes = codesters.Line(0, -30, 0, 30, "red")
hours = codesters.Line(0, -60, 0, 60, "green")
def clock():
    num_seconds = 0
    while True:
        seconds.turn_right(2)
        num_seconds += 1
        if num_seconds % 180 is 0:
            minutes.turn_right(10)
            if num_seconds% 10800 is 0:
                hours.turn_right(30)

clock()
