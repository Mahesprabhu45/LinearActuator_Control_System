Technical Problem 3 – Position Control Logic

Goal:
Move the actuator to a desired target position using RS-485 feedback.
The actuator should go up if the target is higher and down if lower.
Stop when it reaches the setpoint.

----------------------------------------------------

# Variables
position = 0
target = 500               # example desired position (can be changed)
UP_LIMIT = 1000
DOWN_LIMIT = 0
tolerance = 10             # acceptable range around target

OUT_UP = OFF
OUT_DOWN = OFF

while true:

    # read live position feedback
    position = read_position()

    # safety interlock (same rule as before)
    if OUT_UP == ON and OUT_DOWN == ON:
        OUT_UP = OFF
        OUT_DOWN = OFF
        print("Safety lock triggered")
        continue

    # check if already close enough
    if abs(position - target) <= tolerance:
        OUT_UP = OFF
        OUT_DOWN = OFF
        print("Target reached")
        break

    # move up if target higher
    if position < target:
        OUT_UP = ON
        OUT_DOWN = OFF

        if position >= UP_LIMIT:
            OUT_UP = OFF
            print("Reached upper limit, stopping")
            break

    # move down if target lower
    else if position > target:
        OUT_DOWN = ON
        OUT_UP = OFF

        if position <= DOWN_LIMIT:
            OUT_DOWN = OFF
            print("Reached lower limit, stopping")
            break

    wait(100 ms)
