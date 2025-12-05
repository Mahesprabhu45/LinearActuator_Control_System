Technical Problem 2 - Actuator Programming Logic
(Using pseudocode)

Goal:
The actuator should keep moving up and down automatically based on limit values and RS-485 feedback. 
Only one direction should run at a time.

---------------------------------------------------------

# Variables
position = 0                       # live feedback value
UP_LIMIT = 1000                   # maximum allowed position
DOWN_LIMIT = 0                    # minimum allowed position

# Start direction (bonus requirement)
direction = "UP"

# Counters for number of cycles
up_cycles = 0
down_cycles = 0

# Outputs (mapped to the controller)
OUT_UP = OFF
OUT_DOWN = OFF


# Main loop (keeps running)
while true:

    # Read actuator position from RS-485 feedback
    position = read_position()

    # Safety: never allow both outputs at the same time
    if OUT_UP == ON and OUT_DOWN == ON:
        OUT_UP = OFF
        OUT_DOWN = OFF
        print("Safety interlock triggered - both signals active")
        continue

    
    # Movement logic
    if direction == "UP":
        OUT_UP = ON
        OUT_DOWN = OFF

        # Check if limit reached
        if position >= UP_LIMIT:
            OUT_UP = OFF
            direction = "DOWN"
            up_cycles = up_cycles + 1
            print("Reached top, switching direction to down")


    else if direction == "DOWN":
        OUT_DOWN = ON
        OUT_UP = OFF

        # Check if lower limit reached
        if position <= DOWN_LIMIT:
            OUT_DOWN = OFF
            direction = "UP"
            down_cycles = down_cycles + 1
            print("Reached bottom, switching direction to up")


    # Extra fault handling (bonus)
    if position > UP_LIMIT + 50 or position < DOWN_LIMIT - 50:
        OUT_UP = OFF
        OUT_DOWN = OFF
        print("Fault detected - sensor or movement error")
        break


    wait(100 ms)   # small delay before next loop iteration

---------------------------------------------------------

Notes:
- The logic keeps toggling the actuator movement up and down.
- Uses position feedback so it doesn’t rely on timing.
- Safety rule ensures only one direction is energized.
- Counts how many times the actuator went up and down.
